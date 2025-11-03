from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
response = requests.get('https://movie.douban.com/top250',headers = headers)

html = response.text
soup = BeautifulSoup(html, "html.parser")