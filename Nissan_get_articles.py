import csv
import urllib

import requests
from bs4 import BeautifulSoup

r = requests.get("https://global.nissannews.com/ja-JP/channels/notices")

title_url = []

soup = BeautifulSoup(r.text, "html.parser")


# まずは記事一覧を取得

article_list = soup.find("div", {"class": "paginated-content-container"})
# 続いてさらに絞り込み。Article記事を取得。
cards = article_list.find_all(
    "article", {"class": "release-item release-item--with-thumbnail row"}
)

result = [["title", "absolute_url"]]

for card in cards:
    title = card.find("h5").text.splitlines()[1]
    relative_url = ".." + card.find("a").get("href")
    base_url = "https://global.nissannews.com/"
    absolute_url = urllib.parse.urljoin(base_url, relative_url)
    result.append([title, absolute_url])


with open("Nissan_articles.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerows(result)
