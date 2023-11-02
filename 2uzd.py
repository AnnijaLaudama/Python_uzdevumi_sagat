"""
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

Kas ir RSS?

"""

import feedparser 

# 1) Norādīd RSS plūsmas URL(vietrādis), kas satur google.lv ziņas

rss_url='https://news.google.com/rss?hl=lv&gl=LV&ceid=LV:lv'

# 2) lejupielādēju un analizēju RSS plūsmu
feed=feedparser.parse(rss_url)

# 3) Parādīšana
for entry in feed.entries:
    print("virsraksts", entry.title)
    print("Saite", entry.link)
    print("n/a")

# ielogoties ar google un tad paskaties ja interesē
