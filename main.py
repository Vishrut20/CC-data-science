from flask import Flask, render_template, request, redirect
import short_url_generator  # Replace with the actual module for generating short URLs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form["long_url"]
        short_url = short_url_generator.getshorturl(long_url)  # Replace with your actual URL shortening function
        return render_template("index.html", short_url=short_url)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
