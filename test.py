import pydaisi as pyd

ytbuddy = pyd.Daisi("realhardik18/ytbuddy")

# print(ytbuddy.test().value)
print(ytbuddy.infoOfVideo(
    'https://www.youtube.com/watch?v=SpbpD0qDSho&ab_channel=DonutMedia').value)
