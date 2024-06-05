import sys
import joblib
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def predict(model_path, heure):
    model = joblib.load(model_path)
    prediction = model.predict([[int(heure)]])
    return prediction[0]

@app.route('/api/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    heure = data['heure']
    model_path = 'random_forest_model.pkl'  # Assurez-vous que ce chemin est correct
    prediction = predict(model_path, heure)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
