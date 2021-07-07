from flask import Flask, render_template, request
from Main import getWeatherData

app=Flask(__name__)

@app.route('/')
def home():
    # return 'hello world'
    return render_template('index.html')
    # create a folder templates and place index.html in it
    # for any js or css files, place them in a folder named static
    # this is the home route

@app.route('/getWeather', methods=['POST'])
def getWeather():
    cityName = request.json['city']
    data = getWeatherData(cityName)
    return data

if __name__ == '__main__':
    app.run()