#!/usr/bin/python3
from urllib.parse import unquote
import requests as req
import sys
import os
import time,re
from time import sleep
os.system('clear')

logo = ('''
    +-----------------------+
    | FACEBOOK | DOWNLOADER |
    +-----------------------+ ''')


def down(url, path):
    testing = 1024
    content = req.get(url)
    size = round(int(content.headers.get('Content-Length'))/testing)
    print(f'\n[-] Video Size: {size} KB')
    with open(path, 'wb') as a:
        for data in content.iter_content(chunk_size=testing):
            a.write(data)
    print('[√] Download successfuly')

def parse(url):
    res = req.get(url).text
    if 'video_redirect' in res:
        url_video = re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"', res)
        return unquote(url_video.group(1)).replace(';', '&')
    else:
        exit('[!] Video Not Found')

if __name__ == '__main__':
    print (logo)
    print ('\n[?] Please insert a valid Video URL:')
    url = parse(input('=>: ').replace('www', 'mbasic'))
    path = input('[?] Save File To: ')
    if '.mp4' in path:
        down(url, path)
    else:
        print ('Example:')
        print ('Save To: /sdcard/video/nama_video.mp4')
        sys.exit()
