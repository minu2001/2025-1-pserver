import requests

new_measurement = {
    "sepal_length": 5.0,
    "sepal_width" : 3.4,
    "petal_length": 1.4,
    "petal_width" : 0.2
}

response = requests.post("http://127.0.0.1:8000/predict", json=new_measurement)
print(response.content)

getresponse = requests.get("http://127.0.0.1:8000/predict")
print(getresponse.content)