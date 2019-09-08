import pandas as pd
import requests
from lxml import html

def scraper(url_yelp, num_reviews=20):
    
    # get business id
    url_yelp = url_yelp.split('?')[0]
    biz = url_yelp.replace('https://www.yelp.com/biz/', '')
    # get url
    url_base = "https://www.yelp.com/biz/" 
    url_api = "/review_feed?sort_by=date_desc&start="
    url = url_base + biz + url_api + str(num_reviews * 5)

    colnames = ['date', 'text', 'rating']
    df_reviews = pd.DataFrame(columns=colnames)
    with requests.get(url, timeout=20) as r: 
        response = r.json()
        div = html.fromstring(response['review_list'])
        dates = div.xpath("//div[@class='review-content']/descendant::span[@class='rating-qualifier']/text()")
        texts = [e.text for e in div.xpath("//div[@class='review-content']/p")]
        ratings = div.xpath("//div[@class='review-content']/descendant::div[@class='biz-rating__stars']/div/@title")
        df = pd.DataFrame([dates, texts, ratings]).T
        df.columns = colnames
        df['date'] = df['date'].apply(lambda x: x.strip())
        df_reviews = pd.concat([df_reviews, df], 
                               ignore_index=True)
        del df
   
    return df_reviews