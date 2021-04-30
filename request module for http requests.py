import requests

r = requests.get("https://financialmodelingprep.com/")
# print(r.text)
print(r.status_code)

# url = "www.sonething.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.get(url=url, data=data)