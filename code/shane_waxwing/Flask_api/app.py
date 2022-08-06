from flask import Flask, render_template, request
import key
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather/', methods=['POST'])
def weather():

    long = ''
    lat = ''
    city = request.form['city']
    if city == "cary":
        long = '-78.781143'
        lat = '35.791470'
    
    elif city == "pocono":
        long = '-75.391752'
        lat = '41.131944'

    else:
        long = '-74.978881'
        lat = '40.757975'






    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={key.key}&units=imperial")
    data = response.json() 
    print(data)
    return render_template('weather.html', data=data)










app.run(debug=True)





# https://api.openweathermap.org/data/2.5/weather?lat=41.131944&lon=-75.391752&appid=0e9058793eaded984375570b053e1006&units=imperial