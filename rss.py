import feedparser

rss_url = "https://tw.news.yahoo.com/rss/"  # 可換成其他 RSS

feed = feedparser.parse(rss_url)

with open("rss_output.txt", "w", encoding="utf-8") as f:
# *************************************************************  請修改程式碼內容 (將最新的5個新聞寫入txt檔案中)
    for entry in feed.entries[:5]:
        f.write(f"標題: {entry.title}\n")
        f.write(f"連結: {entry.link}\n")
        f.write(f"時間: {entry.published}\n")
        f.write("-" * 40 + "\n")
# *************************************************************

print ( "已完成新聞抓取" )
