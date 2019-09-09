# flask-yelp-reviews

This is a spaCy+scattertext NLP app hosted on Heroku.

# About the app

**Go to the app**   
https://yelp-reviews.herokuapp.com/   
**Call API**     
https://yelp-reviews.herokuapp.com/api/terms  

**Request JSON example**    
```
{"yelp_url": "https://www.yelp.com/biz/aunt-jakes-new-york"}
```   
**Response JSON example**   
```
{
    "0": {
        "highratingscore": 1.0,
        "poorratingscore": 0.0,
        "term": "spot"
    },
    "1": {
        "highratingscore": 1.0,
        "poorratingscore": 0.03,
        "term": "omg"
    },
    "2": {
        "highratingscore": 1.0,
        "poorratingscore": 0.03,
        "term": "homemade"
    },
    "3": {
        "highratingscore": 1.0,
        "poorratingscore": 0.03,
        "term": "pancakes"
    },
    "4": {
        "highratingscore": 1.0,
        "poorratingscore": 0.03,
        "term": "event"
    },
    "5": {
        "highratingscore": 0.01,
        "poorratingscore": 1.0,
        "term": "completely"
    },
    "6": {
        "highratingscore": 0.01,
        "poorratingscore": 1.0,
        "term": "minutes to"
    },
    "7": {
        "highratingscore": 0.01,
        "poorratingscore": 1.0,
        "term": "10 minutes"
    },
    "8": {
        "highratingscore": 0.01,
        "poorratingscore": 1.0,
        "term": "host"
    },
    "9": {
        "highratingscore": 0.11,
        "poorratingscore": 1.0,
        "term": "45 minutes"
    }
}
```

# Logs 

2019-09-08 repo created and deployed on Heroku

# Links

Go to deployment page   
https://dashboard.heroku.com/apps/yelp-reviews/deploy/github  
Google Colab notebook   
https://colab.research.google.com/drive/1nvnFu8SjFz30tMVnP7zcksUrkCSodqc_   
Scattertext   
https://github.com/JasonKessler/scattertext  

# Examples

Web scraping  
<img src="https://github.com/Nov05/pictures/blob/master/pic001/2019-09-08%2022_12_18-2019-09-07%20yelp%20reviews%20flask%20app.ipynb%20-%20Colaboratory.png?raw=true" width=700>  

Scattertext NLP  
<img src="https://github.com/Nov05/pictures/blob/master/pic001/2019-09-08%2022_01_04-2019-09-07%20yelp%20reviews%20flask%20app.ipynb%20-%20Colaboratory.png?raw=true" width=700>  

Scattertext NLP  
<img src="https://github.com/Nov05/pictures/blob/master/pic001/2019-09-08%2021_59_17-2019-09-07%20yelp%20reviews%20flask%20app.ipynb%20-%20Colaboratory.png?raw=true" width=700> 

Scattertext NLP   
<img src="https://github.com/Nov05/pictures/blob/master/pic001/2019-09-08%2021_58_39-2019-09-07%20yelp%20reviews%20flask%20app.ipynb%20-%20Colaboratory.png?raw=true" width=700> 

