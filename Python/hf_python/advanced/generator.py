from url_utils import gen_from_urls

urls = ('https://www.facebook.com','https://www.cnn.com','https://www.twitter.com')


for resp_len,status,url in gen_from_urls(urls):
    print(resp_len, '->', status,url)





"""

for resp in [ requests.get(url) for url in urls]:
    print(len(resp.content),'->',resp.status_code,resp.url)


#using generator to process the URLs 

for resp in (requests.get(url) for url in urls):
    print(len(resp.content),'->',resp.status_code,resp.url)

"""