#1T
# print("软工二、2018888888、汪关智\n-----------\n")

#2T
# n = str(input())
# print(n[6:14])

#3T
# for i in range(0,101):
#     if i%2==0:
#         print(i)

#4T
import requests
from bs4 import BeautifulSoup 
HEADERS = {
    "User-Agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_2 ) AppleWebKit/537.36(KHTML, like Gecko) Chrome/60.0.3202.62 Safari/537.36"
}

def html(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "再爬你就进去了"
    soup = BeautifulSoup(r.text,'html.parser')  
    all = soup.find('div',attrs={'class':'book_img'})
    for i in all.findall('div'):
        name = soup.find('div',attrs={'class':'bookauthor'}) 
    print(name)

if __name__ == "__main__":
    url = "http://www.hbcbs.com.cn/Art/List_5_0/1/"
    html(url)