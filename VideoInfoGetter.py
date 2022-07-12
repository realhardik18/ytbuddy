from pytube import YouTube
import scrapetube


def infoOfVideo(video_link):
    information = {}
    yt = YouTube(video_link)
    information['video_link'] = video_link
    information['description'] = yt.description
    information['duration'] = yt.length
    information['date'] = yt.publish_date
    information['title'] = yt.title
    information['views'] = yt.views
    information['author'] = yt.author
    information['thumbnail'] = yt.thumbnail_url

    return information


def infoOfAllVids(url_to_channle):
    all_vids = list()
    videos = scrapetube.get_channel(
        url_to_channle[len(url_to_channle)-url_to_channle[::-1].index('/'):])
    return list(videos)[0]
    '''        
    for video in videos:
        all_vids.append(f"https://youtube.com/watch?v={video['videoId']}")
        # print(f"https://youtube.com/watch?v={video['videoId']}")
    all_data = []
    for video in all_vids:
        all_data.append(infoOfVideo(video))
    return all_data
    '''
# print(info(all_vids[0]))
# work on site aspect now
