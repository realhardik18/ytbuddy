import scrapetube
import pandas

videos = scrapetube.get_channel("UCMiY4t431lhXY4QtPZtzftQ")

for video in videos:
    print(video['videoId'])
# work on getting ids of channle from data sheet
'''
df = pandas.read_excel('DataBase.xlsx')
channel_ids = []
urls = df['link to channle'].tolist()
for url in urls[1:]:
    revser = url[::-1]
    first_slash = revser.index('/')
    channel_ids.append(url[len(url)-first_slash:])
print(channel_ids)
'''
