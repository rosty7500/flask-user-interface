from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home/")
def home():
    #return "welcome " + username
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)