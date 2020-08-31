import requests
from bs4 import BeautifulSoup as bs
import os
import time

time_stamp = time.strftime("_%Y_%m%d", time.localtime())

target_url = 'https://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/'
page_content = requests.get(target_url)
parsed_page = bs(page_content.text, 'html.parser')
target_tag_parent = parsed_page.find_all('a')
target_tag = target_tag_parent[-1]
target_link = requests.get(target_url + target_tag['href'])

old_file = open('./BeautifulSoup_Ref/bs4.tar.gz', 'rb')
old_hash = hash(old_file.read())
old_file.close()
new_hash = hash(target_link.content)

print('old_hash:', old_hash)
print('new_hash:', new_hash)

if(old_hash != new_hash):
    print('package updated!')
    print('start downloading.')
    try:
        target_file = open('./BeautifulSoup_Ref/bs4' + time_stamp + '.tar.gz', 'wb')
        target_file.write(target_link.content)
        target_file.close()
        print('Successfully downloaded!')
    except:
        print('Some Error...')

else:
    print('no update, exit.')
    exit()
