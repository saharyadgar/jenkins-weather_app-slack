import json

from flask import Flask, render_template, request
import requests
from pandas import Timestamp

app = Flask(__name__)
@app.route('/')
def home():

    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    api_key = "GLDY4VV8V7VJ8GJJYC3U3ABDT"
    location = request.form['city']
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    query_data = "next7days?unitGroup=metric&elements=datetime%2Cname%2Caddress%2Ctempmax%2Ctempmin%2Ctemp%2Chumidity%2Cicon&include=days&key="

    full_url = f"{base_url}{location}/{query_data}{api_key}&contentType=json"

    try:
        response = requests.get(full_url).json()
        days_list_by_name = get_days_by_date(response)
        return render_template('weather.html', data=response, days=days_list_by_name)

    except:
        return render_template('error.html')


def get_days_by_date(response):
    days = response['days']

    days_list_by_date = []
    days_list_by_name = []

    for i in range(len(days)):
        days_list_by_date.append(days[i]['datetime'])

    for i in days_list_by_date:
        days_list_by_name.append((Timestamp(i).day_name()))

    return days_list_by_name

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
