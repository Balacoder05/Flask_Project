from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home_page():
    print("Flask Project")
    print("Automatic Server")
    return render_template('home.html')

@app.route('/about')
def about_page():
    print(request.args)
    print(request.args['name'])
    print(request.args['age'])
    return render_template('about.html')

@app.route('/contact/<int:age>')
def contact_page(age):
    print(age)
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(port=5001,debug=True)