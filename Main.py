from bs4 import BeautifulSoup
import requests

# city = input()
def getWeatherData(city):
    url = "https://www.google.com/search?q="+city+"+weather"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    # print(soup.prettify())

    data = {}

    temp = soup.find("div", class_ = "BNeawe iBp4i AP7Wnd")
    region = soup.find("span", class_ = "BNeawe tAd8D AP7Wnd")
    time_and_condition = soup.find("div", class_ = "BNeawe tAd8D AP7Wnd")
    # print(temp.text)
    # print(time_and_condition.text)
    # print(region.text)
    data['temperature'] = temp.text
    data['time_and_condition'] = time_and_condition.text.split('\n')
    # data['time_and_condition'] = time_and_condition.text
    data['region'] = region.text

    return data