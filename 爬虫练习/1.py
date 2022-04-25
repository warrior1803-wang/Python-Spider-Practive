import requests
import logging
import re


url = 'https://loudmurmursfm.com/feed/audio.xml'

    # 模拟浏览器发送http请求#
logging.captureWarnings(True)
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
    # 目标小说主页的网页源代码#
html = response.text
title = 'link'

    # 新建小说文件，保存小说内容
# fb = open('%s.txt' % title, 'w', encoding='utf-8')
# dl = re.findall(r'<ul class="list header">.*?</ul>', html, re.S)[0]
# podcast_info_list = re.findall(r'<a href="(.*?)">(.*?)</a>', dl)
# for podcast_info in podcast_info_list:
#     podcast_url, podcast_title = podcast_info
#     podcast_url = "https://www.surplusvalue.club/episodes/%s" % podcast_url
#     podcast_url = podcast_url.replace(' ', '')
#     podcast_response = requests.get(podcast_url, verify=False)
#     podcast_response.encoding = 'utf-8'
#     podcast_html = podcast_response.text
#     podcast_content = re.findall(r'<audio class="fsplyr-element fsplyr-sr-only" preload="none">(.*?)</audio>',podcast_html,re.S)[0]
#     podcast_content = podcast_content.replace('<source src="','')
#     podcast_content = podcast_content.replace('" type="audio/mpeg" />','')
#     podcast_content = podcast_content.replace(' Your browser does not support the audio tag.','')
#     print(podcast_title,podcast_content)











