import scrapetube
import pandas

df = pandas.read_excel('DataBase.xlsx')
channel_ids = []
urls = df['link to channle'].tolist()
for url in urls[1:]:
    revser = url[::-1]
    first_slash = revser.index('/')
    videos = scrapetube.get_channel(url[len(url)-first_slash:])
    for video in videos:
        print(f"https://youtube.com/watch?v={video['videoId']}")
# work on checking validity of data by clicking random links
