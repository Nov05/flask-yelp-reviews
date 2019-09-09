# flask-yelp-reviews

This is a spaCy+scattertext NLP app hosted on Heroku.

# About the app

**Go to the app**   
https://yelp-reviews.herokuapp.com/   
**Call API**     
https://yelp-reviews.herokuapp.com/api/terms  

**Request JSON example**    
`{"yelp_url": "https://www.yelp.com/biz/aunt-jakes-new-york"}`  
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

