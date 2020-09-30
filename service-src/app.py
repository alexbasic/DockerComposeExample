from flask import Flask
from redis import Redis
import requests
import os

redis_address = os.environ['REDIS_ADDRESS']
dependent_endpoint = os.environ['DEPENDENT_ENDPOINT']
external_endpoint = os.environ['EXTERNAL_ENDPOINT']
google_endpoint = os.environ['GOOGLE_ENDPOINT']

app = Flask(__name__)
redis = Redis(host=redis_address, port=6379)

@app.route('/')
def get():
    redis.incr('hits')
    return 'Helo World! I have been seen %s times.' % redis.get('hits')

@app.route('/dependent')
def get_dependent():
    response = requests.get(dependent_endpoint)
    if response:
        return 'Dependent service is available. Content is: %s' % response.content
    else:
        return 'Error! Dependent service is not available.'

@app.route('/external')
def get_external():
    response = requests.get(external_endpoint)
    if response:
        return 'External service is available. Content is: %s' % response.content
    else:
        return 'Error! External service is not available.'

@app.route('/google')
def get_google():
    response = requests.get(google_endpoint)
    if response:
        return 'Google is available. Content is: %s' % response.content
    else:
        return 'Error! Google is not available.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)