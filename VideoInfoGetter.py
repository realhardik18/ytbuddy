from pytube import YouTube


def info(video_link):
    information = {}
    yt = YouTube(video_link)
    information['video_link'] = video_link
    information['description'] = yt.description
    information['duration'] = yt.length
    information['date'] = yt.publish_date
    information['title'] = yt.title
    information['views'] = yt.views
    information['author'] = yt.author

    return information
