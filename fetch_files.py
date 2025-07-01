#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : starnight_cyber
# @Github  : https://github.com/starnightcyber
# @File    : fetch_docs.py

import requests
import urllib3
import ssl
import time
import json
import subprocess

# Do not support ssl and disable warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
timestamp = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def fetch_files():
    headers = {
        'Host': 'www.gmbz.org.cn',
        'Content-Length': '2781',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.gmbz.org.cn',
        'Referer': 'http://www.gmbz.org.cn/main/bzlb.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close'
    }
    data = 'draw=1&columns%5B0%5D%5Bdata%5D=NORM_ISO_ID&columns%5B0%5D%5Bname%5D=NORM_ISO_ID&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=NORM_NAME_C&columns%5B1%5D%5Bname%5D=NORM_NAME_C&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=NORM_ZT_NAME&columns%5B2%5D%5Bname%5D=NORM_ZT&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=NORM_FLAG_NAME&columns%5B3%5D%5Bname%5D=NORM_FLAG_NAME&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=NORM_NAME_E&columns%5B4%5D%5Bname%5D=NORM_NAME_E&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=NORM_CO_NAME&columns%5B5%5D%5Bname%5D=NORM_CO_NAME&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=NORM_CA_NAME&columns%5B6%5D%5Bname%5D=NORM_CA_NAME&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=NORM_PUB_DATE&columns%5B7%5D%5Bname%5D=NORM_PUB_DATE&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=NORM_IMP_DATE&columns%5B8%5D%5Bname%5D=NORM_IMP_DATE&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=UP_GB_FLAG&columns%5B9%5D%5Bname%5D=UP_GB_FLAG&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=10&columns%5B10%5D%5Bname%5D=&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=200&search%5Bvalue%5D=&search%5Bregex%5D=false&norm_iso_id=&norm_flag=&norm_name_c=&norm_name_e=&norm_co_name=&norm_zt=&norm_pub_date_begin=&norm_pub_date_end=&norm_imp_date_begin=&norm_imp_date_end='
    response = requests.request('POST', url='http://www.gmbz.org.cn/main/normsearch.json', data=data, headers=headers)
    # print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
    content_json = json.loads(response.text)

    with open('./README.md', 'w', encoding='utf8') as readme_file:
        readme_file.write(
'''
# gmbz_docs
国密标准文档

官网链接
http://www.gmbz.org.cn/main/bzlb.html?from=groupmessage

|index|行标号|标准中文名称|类别|状态|发布|实施|文档下载|
| - | - | - | - | - | - | - | - |
''')

        index = 0
        for line in content_json['data']:
            index += 1
            NORM_ID = line['NORM_ID']
            NORM_NAME_C = line['NORM_NAME_C']
            NORM_ZT_NAME = line['NORM_ZT_NAME'] if line['NORM_ZT_NAME'] else '--'
            NORM_FLAG_NAME = line['NORM_FLAG_NAME'] if line['NORM_FLAG_NAME'] else '--'
            # NORM_CO_NAME = line['NORM_CO_NAME']
            # NORM_CA_NAME = line['NORM_CA_NAME']
            NORM_PUB_DATE = line['NORM_PUB_DATE']
            NORM_IMP_DATE = line['NORM_IMP_DATE']
            NORM_APP_ADDR = line['NORM_APP_ADDR']

            download = 'http://www.gmbz.org.cn/file/{}'.format(NORM_APP_ADDR)

            # csv_line = [index, NORM_ID, NORM_NAME_C, NORM_ZT_NAME, NORM_FLAG_NAME, NORM_CO_NAME, NORM_CA_NAME, NORM_PUB_DATE, NORM_IMP_DATE, download]
            # csv_line = [index, NORM_ID, NORM_NAME_C, NORM_ZT_NAME, NORM_FLAG_NAME, NORM_PUB_DATE, NORM_IMP_DATE, download]
            new_line = '|'.join([str(index), NORM_ID, NORM_NAME_C, NORM_ZT_NAME, NORM_FLAG_NAME, NORM_PUB_DATE, NORM_IMP_DATE, download])
            readme_file.write('|' + new_line + '|\n')

            # download file
            
            # out_file = '{} {}.pdf'.format(NORM_ID.replace('/', ''), NORM_NAME_C.replace(' ', ''))
            # print('[*] out_file => {}'.format(out_file))
            # try:
            #     download_cmd = 'curl {} -o "{}"'.format(download, out_file)
            #     print('[*] {}'.format(download_cmd))
            #     p = subprocess.Popen(download_cmd, shell=True)
            #     p.wait()
            # except:
            #     pass
           


if __name__ == '__main__':
    fetch_files()