from flask import Flask, request,render_template
import requests

api_key="7e956342f3845b05ae3c7bf48d142ee7"  # API_Key
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")


@app.route('/temperature')
def temperature():
    city = request.args.get('City', '')
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(URL,verify=False) #SSL verification False 
    if response.status_code == 200: 
        data = response.json() 
        temperature = data["main"]['temp']
        country = data['sys']['country']
        name = data['name']

        return f"<br>{name}, {country} temperature is {temperature}°C <br><br><a href='/'>Return to Homepage"
    else:
        return f"Something went wrong!<br>Error Code: {response.status_code} <br><a href='/'>Return to Homepage</a> "
    

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
