from pytube import YouTube
import youtube_dl


def test():
    return 'hello world'


def stats(video_link):
    yt = YouTube(video_link)
    information = dict()
    information['18+'] = yt.age_restricted
    information['author'] = yt.author
    information['url_to_author'] = yt.channel_url
    information['description'] = yt.description
    information['lenght_in_seconds'] = yt.length
    information['publish_data'] = yt.publish_date
    information['thumbnail_url'] = yt.thumbnail_url
    information['title'] = yt.title
    information['views'] = yt.views
    return information


def download_as_mp3(link_to_video):

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    print('starting download')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link_to_video])
    return 'finished!'
