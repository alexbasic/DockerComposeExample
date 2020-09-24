from flask import Flask
from reds import Redis
import requests
import os

dependent_address = os.environ['DEPENDENT_ADDRESS']
redis_address =  = os.environ['REDIS_ADDRESS']
external_address =  = os.environ['EXTERNAL_ADDRESS']

app = Flask(__name__)
redis = Resdis(host=redis_address, port=6379)

@app.route('/')
def get():
    redis.incr('hits')
    return 'Helo World! I have been seen %s times.' % redis.get('hits')

@app.route('/dependent')
def get_dependent():
    response = requests.get(dependent_address)
    if response:
        return 'Dependent service is available. Content is: %s' % response.content
    else:
        return 'Error! Dependent service is not available.'

@app.route('/external')
def get_external():
    response = requests.get(external_address)
    if response:
        return 'External service is available. Content is: %s' % response.content
    else:
        return 'Error! External service is not available.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)