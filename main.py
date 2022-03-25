import scrapetube
import pandas

df = pandas.read_excel('DataBase.xlsx')
urls = df['link to channle'].tolist()
for url in urls:
    revser = url[::-1]
    first_slash = revser.index('/')
    print(scrapetube.get_channel(url[len(url)-first_slash:]))
    # work from here
