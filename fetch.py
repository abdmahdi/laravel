import requests
import wget

fetch = wget.download(
    'https://phpapilaravel.herokuapp.com/images/1655997907.Bilan_annul M1 GL 2021 2022 session normale_1.xls', '/Users/abderahmanemahdigharzouli/Desktop/')


# for re in res['data']:
#     print(re['attributs'])
#     for tag in re['attributs']['tags']:
#         print(tag)

# url = "http://127.0.0.1:8000/api/posts"
# data = {'title': 'Alice', 'description': 'Bob', 'tags': 'We,did,it!'}
# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
# r = requests.post(url, data=data, headers=headers)
# print(r.json())