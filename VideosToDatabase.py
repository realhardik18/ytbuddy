import scrapetube
from VideoInfoGetter import info

url_to_channle = 'https://www.youtube.com/channel/UCJBtCUf_GEvlYeOwUSnCC0Q'
c = 0
all_vids = []
videos = scrapetube.get_channel(
    url_to_channle[len(url_to_channle)-url_to_channle[::-1].index('/'):])
for video in videos:
    all_vids.append(f"https://youtube.com/watch?v={video['videoId']}")
    print(f"https://youtube.com/watch?v={video['videoId']}")
    c += 1
print(f'done! total video count:-{c}')

# print(info(all_vids[0]))
# work on site aspect now
