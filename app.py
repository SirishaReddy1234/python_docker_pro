app = Flask(__name__)

@app.route("/")
def welcome():
    return """
    <html>
        <body style="background-color: lightblue;">
            <h1 style="text-align: center; color: white;">Welcome to my web page!</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
