import os
import re
import math
import tqdm
import requests
import zlib
from collections import namedtuple

Downloaded_file = namedtuple('Downloaded_file', 'path basename crc32')

def download_file(URL, dirname, chunk_size=8192):
    
    with requests.get(URL, stream=True) as res:

        res.raise_for_status()
        
        try:
            base_name = re.findall("filename=\"(.+)\"", res.headers['Content-Disposition'])[0]
        except KeyError:
            print("URL Header does not contain a filename. Reverting to URL string.")
            base_name = URL.split("/")[-1]
        finally:
            file_path = os.path.join(dirname, base_name)

        try:
            file_size = int(res.headers['Content-Length'])
        except KeyError as err:
            msg = 'The URL Header does not contain a file-length: {}'.format(err)
            raise KeyError(msg)
        else:
            chunk_size = min(file_size, chunk_size)
            total_chunks = file_size // chunk_size
            unit_scale = chunk_size / 10**6
            fs_digits = int(math.log10(file_size)) + 1
            bar_format = '{{l_bar}}{{bar}}| {{n_fmt:.{width}}}/{{total_fmt:.{width}}}{{postfix}} [{{elapsed}}<{{remaining}}, ' '{{rate_fmt}}{{postfix}}]'.format(
                                    width = fs_digits - 4 )

        with open(file_path, 'wb') as f:
            stream = tqdm.tqdm(res.iter_content(chunk_size=chunk_size), desc=base_name, unit="MB", unit_scale=unit_scale,
                                    unit_divisor=1000, total=total_chunks, bar_format=bar_format)

            crc = 0

            for chunk in stream: 
                if chunk:
                    f.write(chunk)
                    crc = zlib.crc32(chunk, crc)

    return Downloaded_file(file_path, base_name, "%X"%(crc & 0xFFFFFFFF) )



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='''
    A file downloader, which returns the full filepath, basename, and CRC32 hash for the downloaded file - if successful.
    ''')

    parser.add_argument("URL", help="URL to be downloaded", type=str)
    
    parser.add_argument("-d", "--dirname", help="Directory to download to. [d]", type=str, default=os.getcwd())
    parser.add_argument("-cs", "--chunk_size", help="Chunksize in bytes.", type=int, default=8192)

    args = parser.parse_args()

    try:
        download = download_file(**vars(args))
    except:
        print("Download not successful!")
        raise
    else:
        print("Download successsfully finished!")
        print("File saved as: {}".format(download.path))
        print("CRC32:         {}".format(download.crc32))