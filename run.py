from flask import Flask
# from config import DEBUG

app = Flask(__name__)
app.config.from_object('config')

print(app.config['DEBUG'])

@app.route("/hello")
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])