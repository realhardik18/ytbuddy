from pytube import YouTube
import scrapetube
from operator import itemgetter
# this is to get info about the give video url


def infoOfVideo(video_link):
    information = {}
    yt = YouTube(video_link)
    information['author'] = yt.author
    information['link_to_channle'] = yt.channel_url
    information['description'] = yt.description
    information['keywords'] = yt.keywords
    information['date_relased'] = yt.publish_date
    information['rating'] = yt.rating
    information['thumbnail_url'] = yt.thumbnail_url
    information['title'] = yt.title
    information['views'] = yt.views
    information['vid_link'] = video_link

    return information


# this gives all the videos of a youtube channle
def infoOfAllVids(url_to_channle):
    all_vids = list()
    videos = scrapetube.get_channel(
        url_to_channle[len(url_to_channle)-url_to_channle[::-1].index('/'):])
    for video in videos:
        all_vids.append(f"https://youtube.com/watch?v={video['videoId']}")
        # print(f"https://youtube.com/watch?v={video['videoId']}")
    all_data = []
    for video in all_vids:
        all_data.append(infoOfVideo(video))
    return all_data

# this returns the top 15 most vewied videos of a youtube channle


def Top15MostVeiwed(url_to_channle):
    data = infoOfAllVids(url_to_channle)
    newlist = sorted(data, key=itemgetter('views'))[::-1]
    return newlist[:15]

# this returns the 15 least vewied videos


def Top15LeastVeiwed(url_to_channle):
    data = infoOfAllVids(url_to_channle)
    newlist = sorted(data, key=itemgetter('views'))
    return newlist[:15]


def test():
    return 'hello im working'
# print(info(all_vids[0]))
# work on site aspect now
