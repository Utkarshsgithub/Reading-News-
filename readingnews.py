import json

import requests

def speak(str):

    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

# nws = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-08-09&sortBy=publishedAt&apiKey=029aa119daba4ae2927638a6f1aa35d3")
# news_dict = nws.text

params = {
    'source':'newsapi',
    'sortBy':'top',
    'apiKey':'029aa119daba4ae2927638a6f1aa35d3'
}

# base_url = 'https://newsapi.org/v2/everything?q=apple&from=2021-09-08&to=2021-09-08&sortBy=popularity&apiKey=029aa119daba4ae2927638a6f1aa35d3'

# ------------------ G E E K   F O R   G E E K S  ----------------------

# response = requests.get(base_url,params=params)
# open_news = response.json()
# content = open_news['articles']
# print(content)
#
# result = []
#
# for line in content:
#     result.append(line['content'])
#
# for i in range(len(result)):
#     print(i + 1, result[i])
#
# print(result)
# ho_gya_kya = str(result)
# speak(ho_gya_kya)
# speak("Program ended!")
# -----------------------------------------------------------------------

# ------------------ C O D E W I T H H A R R Y  ----------------------------

# Kya mast hai ye wala

try:

    base_url = 'https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=029aa119daba4ae2927638a6f1aa35d3'
    news = requests.get(base_url).text
    json_news = json.loads(news)  # ab ye ek dict ban chuka hai
    print(json_news['articles'])
    articles = json_news['articles']
    speak('reading todays news')
    n = 1
    for article in articles:
        print(f"{n}.{article['title']}")
        speak(article['title'])
        n += 1
        speak("Moving onto the next news... Listen carefully")
    speak(r'You are now caught up to taday"s headlines')

except Exception as e:
    print('Check your internet connection')

# --------------------------------------------------------------------------


