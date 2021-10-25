from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Fill me in
    return jsonify({})


@app.route('/update-model', methods=['POST'])
def update_model():
    # Fill me in
    return jsonify({})


if __name__ == '__main__':
    app.run(debug=True)
