from flask import Flask

app = Flask(__name__)

@app.route("/")
def home ():
    return "Hello, Farhad Docker v.1 is running"


@app.route("/health")
def health ():
    return "Application is healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
