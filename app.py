from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4f200774b8404cd390dae6eec8909905')
    data = json.loads(req.content)
    
    # loads convert the data into the python object
   
    return render_template('index.html', data = data)

@app.route('/termsandservice')
def termsofservice():
    return render_template('termsandservice.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


