

#小说的名字
title=re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>',html)[0]
#新建小说文件，保存小说内容
fb = open('%s.txt'% title, 'w',encoding= 'utf-8')
#获取每一章信息（章节，url）
dl = re.findall(r'<div id="list">.*?</div>',html,re.S)[0]
chapter_info_list=re.findall(r'<a href="(.*?)">(.*?)</a>',dl)
#循环每一个章节，分别去下载
for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url = "https://www.shujy.com/5200/242860/%s" % chapter_url
    chapter_url = chapter_url.replace(' ','')
    #下载章节内容
    chapter_response = requests.get(chapter_url,verify = False)
    chapter_response.encoding = 'gdk'
    chapter_html = chapter_response.text
    #提取章节内容
    chapter_content = re.findall(r'<div id="content">(.*?)</div>', chapter_html,re.S)[0]
    chapter_content = chapter_content.replace('&nbsp;', '')
    chapter_content = chapter_content.replace('<br />', '')
    chapter_content = chapter_content.replace('&amp;t;', '')
    chapter_content = chapter_content.replace('&emsp;&emsp;','')
    fb.write(chapter_title)
    fb.write('\n')
    fb.write(chapter_content)
    fb.write('\n')
    print(chapter_url, chapter_title)






