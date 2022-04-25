import re
import requests
songId = []
songName = []
for n in range(0,5):
    url = 'https://media.fireside.fm/file/fireside-audio/podcasts/audio/6/695c2adc-8702-4736-9c8a-d23ec3d712a5/episodes/{}%.mp3'.format(n)
    print(url,end='\n')
    html = requests.get(url)
    import requests
    import logging
    import re

    url = 'https://www.surplusvalue.club/episodes'

    # 模拟浏览器发送http请求#
    logging.captureWarnings(True)
    response = requests.get(url, verify=False)
    response.encoding = 'utf-8'
    # 目标小说主页的网页源代码#
    html = response.text
    title = re.findall(r'<meta name="title" content="(.*?)"/>', html)
    # 新建小说文件，保存小说内容
    fb = open('%s.txt' % title, 'w', encoding='utf-8')
    dl = re.findall(r'<ul class="list header">.*?</ul>', html, re.S)[0]
    podcast_info_list = re.findall(r'<a href="(.*?)">(.*?)</a>', dl)
    for podcast_info in podcast_info_list:
        podcast_url, podcast_title = podcast_info
        podcast_url = "https://www.surplusvalue.club/episodes/%s" % podcast_url
        podcast_url = podcast_url.replace(' ', '')
        podcast_response = requests.get(podcast_url, verify=False)
        podcast_response.encoding = 'utf-8'
        podcast_html = podcast_response.text
        podcast_content = re.findall(r'<section class="split">(.*?)</section>', podcast_html, re.S)[0]
        podcast_content = podcast_content.replace('''<div class="split-primary prose">
        <header class="section-header">
          <h3>
            About this Episode
          </h3>
        </header>''', '')
        podcast_content = podcast_content.replace(''' </div>

      <aside class="split-secondary">
      </aside>
    ''', '')
        podcast_content = podcast_content.replace('<br>', '')
        podcast_content = podcast_content.replace('<p>', '')
        podcast_content = podcast_content.replace('</p>', '')
        podcast_content = podcast_content.replace('<li>', '')
        podcast_content = podcast_content.replace('</li>', '')
        podcast_content = podcast_content.replace('<ul>', '')
        podcast_content = podcast_content.replace('</ul>', '')
        fb.write(podcast_title)
        fb.write('\n')
        fb.write(podcast_content)
        fb.write('\n')
        print(podcast_url, podcast_title)














