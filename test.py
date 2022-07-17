import pydaisi as pyd

ytbuddy = pyd.Daisi("realhardik18/ytbuddy")

# print(ytbuddy.test().value)
# print(ytbuddy.endpoints.keys())
print(ytbuddy.infoOfAllVids(
    'https://www.youtube.com/channel/UCJBtCUf_GEvlYeOwUSnCC0Q').value)
