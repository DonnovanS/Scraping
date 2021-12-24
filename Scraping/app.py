from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Prueba</h1>'
@app.route("/urlscra", methods=["POST"])
def urlscra():
    json=request.get_json(force=True)

if __name__ == '__main__':
    app.run()