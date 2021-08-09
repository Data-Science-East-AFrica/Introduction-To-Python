from flask import Flask 

app = Flask(__name__) 


@app.route("/<username>")
def index(username):
    return f"welcome to {username} blog"


if __name__ == '__main__':
    app.run(debug = True)