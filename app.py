from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="API dziala")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/add/<int:a>/<int:b>")
def add(a: int, b: int):
    return jsonify(a=a, b=b, result=a + b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
