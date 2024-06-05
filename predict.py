import sys
import joblib
import json

def predict(model_path, heure):
    model = joblib.load(model_path)
    prediction = model.predict([[int(heure)]])
    return prediction[0]

if __name__ == '__main__':
    model_path = sys.argv[1]
    heure = sys.argv[2]
    prediction = predict(model_path, heure)
    print(json.dumps({'prediction': prediction}))
