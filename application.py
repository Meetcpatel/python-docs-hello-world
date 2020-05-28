import flask
import requests
from bs4 import BeautifulSoup
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.


@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is Index Page</h1>'''


@app.route('/application', methods=['POST'])
def api_id():
      data = request.json
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    #if 'id' in request.args:
     #   id = request.args['id']
    #else:
     #   return "Error: No id field provided. Please specify an id."
   # id= 'https://www.instagram.com/p/CAknIJGld6J';
    #start_url = id#In this example, the link is https://www.instagram.com/p/BdLhfC-HWIi/?taken-by=arianagrande
    response = requests.get(id)
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    photo_url = soup.find("meta", property="og:image")['content']
    #print(photo_url)

    dict = {
            'URL': photo_url,   
            }
   # return dict
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return data

#port = int(os.environ.get("PORT", 5000))
   
#app.run()
#app.run(host='0.0.0.0', port=80)
