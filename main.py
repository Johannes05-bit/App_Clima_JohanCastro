from flask import Flask, render_template, request
import requests

main = Flask(__name__)

# Ruta principal
@main.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = "788a3328cacfbbb7053717184f4a2564"  
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'latitude': data['coord']['lat'],
                'longitude': data['coord']['lon']
            }
        else:
            weather_data = {'error': 'error'}
    return render_template('index.html', weather_data=weather_data)

# Ruta del CV
@main.route('/cv.html')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    main.run(debug=True)
