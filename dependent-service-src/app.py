from flask import Flask

app = Flask(__name__)

@app.route('/abc')
def get_abc():
    return 'Hello world from dependent service!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)