import requests
from bs4 import BeautifulSoup
import json
# 爬取貼文的網址
url = 'https://www.ptt.cc/bbs/NBA/index.html'
# 儲存貼文的列表
articles = []
# 爬取前3頁貼文資料
for i in range(3):
# 發送GET請求
    response = requests.get(url)
# 解析HTML
    soup = BeautifulSoup(response.text, 'lxml')
 # 取得貼文列表
    posts = soup.select('.r-ent')
 # 走訪每一筆貼文
    for post in posts:
        # 取得推文數
        push = post.select_one('.nrecspan')
        push_count= push.text if push else '0'
        # 取得文章標題和網址
        title = post.select_one('.title a')
        if title:
            title_text= title.text
            url_text= 'https://www.ptt.cc' + title['href']
        else:
            title_text= '已刪除的文章'
            url_text= ''
        #**************************************************************** 驗收一修改區域
        # 取得日期和作者
        date = post.select_one('.meta .date')
        author = post.select_one('.meta .author')
        # 將資料加入列表
        article = {'推文數': push_count, '文章標題': title_text, '文章網址': url_text, '日期': date.text, '作者': author.text}
        #****************************************************************
        articles.append(article)
        # 取得前一頁的網址
        paging = soup.select('.btn-group-paging a')
        url= 'https://www.ptt.cc' + paging[1]['href']
# 儲存為JSON檔案
with open('ptt_NBA.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)