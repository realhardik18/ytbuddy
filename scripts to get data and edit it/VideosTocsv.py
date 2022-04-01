from VideoInfoGetter import info

with open(r'C:\Users\hardik\OneDrive\Documents\GitHub\YoutubeShortsToInstaReels\scripts to get data and edit it\ALLVideosLinks.txt', 'r') as f:
    videos = []
    vids = f.readlines()
    for vid in vids:
        videos.append(vid.strip('\n'))
c = 1

for video in videos:
    information = info(video)
    with open(r'C:\Users\hardik\OneDrive\Documents\GitHub\YoutubeShortsToInstaReels\AllVideoInfo.txt', 'a+') as file:
        # print(information)
        file.write(
            f"{video},{information['duration']},{information['title']},{information['views']},{information['author']}\n")
        file.close()
        print(f'written data line number {c}')
        c += 1
