from flask import Flask, render_template, \
                  request, jsonify
from flask_cors import CORS

from py_scraper import scraper
from py_processor import processor

app=Flask(__name__)
CORS(app)

@app.route('/') 
@app.route('/index')
def index():
    return render_template('index.html')

############################################################
# API - terms
############################################################
@app.route('/api/terms', methods = ['POST'])
def api_terms():
    if request.method == 'POST':
        data_in = request.get_json(force=True)
        # e.g. "https://www.yelp.com/biz/aunt-jakes-new-york"
        url_yelp = data_in['yelp_url']
        df_reviews = scraper(url_yelp)
        df_terms = processor(df_reviews)
        data_out = df_terms.to_json(orient='index')

        return data_out

if __name__ == '__main__':
    app.run(debug=True)