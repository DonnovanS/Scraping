from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>My Flask1</h1>'
@app.route("/urlscra", methods=["POST"])
def urlscra():
    json=request.get_json(force=True)

if __name__ == '__main__':
    app.run()