from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    with open('data.json') as data_file:        
    data = json.load(data_file)
    for item in data:
        print item['id']
    return data

def create_app():
   return app
