import requests
news_url = "https://www.bbc.com"

response = requests.get(news_url)

if response.status_code == 200:
    page_content = response.text
    
    sentences = page_content.split("<h2")
    
for sentence in sentences:
        headline = sentence.split("</h2>")[0]
        if len(headline) < 200 and len(headline) > 100:
            headline = headline.split(">")[1]
            headline = headline.replace('&#x27;', '')
            print(headline)
    
   