import scrapetube
import pandas

df = pandas.read_excel('DataBase.xlsx')
channel_ids = []
urls = df['link to channle'].tolist()
c = 0
for url in urls[1:]:
    revser = url[::-1]
    first_slash = revser.index('/')
    videos = scrapetube.get_channel(url[len(url)-first_slash:])
    for video in videos:
        with open('ALLVideosLinks.txt', 'a') as file:
            file.write(f"https://youtube.com/watch?v={video['videoId']}\n")
            print(f'we at {c} videos!')
            c += 1
print(f'done! total video count:-{c}')
