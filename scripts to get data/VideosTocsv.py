from VideoInfoGetter import info

with open('ALLVideosLinks.txt', 'r') as f:
    videos = []
    vids = f.readlines()
    for vid in vids:
        videos.append(vid.strip('\n'))
c = 1

for video in videos:
    information = info(video)
    with open('AllVideoInfo.txt', 'a+') as file:
        # print(information)
        file.write(
            f"{video},{information['description']},{information['duration']},{information['date']},{information['title']},{information['views']},{information['author']}\n")
        file.close()
        print(f'written data line number {c}')
        c += 1
