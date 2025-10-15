from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_data():
    return "<h1>This is Flask Project.</h1>"

if __name__ == '__main__':
    app.run(debug=True)