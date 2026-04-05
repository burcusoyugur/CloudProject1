from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests
from datetime import datetime, timedelta # Zaman düzeltmesi için 
application = Flask(__name__)
CORS(application)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/api/status', methods=['GET'])
def get_status():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=39.93&longitude=32.85&current=temperature_2m,relative_humidity_2m,apparent_temperature"
        response = requests.get(url, timeout=5)
        res_data = response.json()
        current = res_data['current']
        
        
        turkiye_saati = datetime.utcnow() + timedelta(hours=3)
        su_an = turkiye_saati.strftime("%H:%M:%S")
        
        data = {
            "istasyon": "Ankara Merkez İstasyonu",
            "sicaklik": current['temperature_2m'],
            "durum": "AWS Frankfurt - Aktif",
            "mesaj": f"Hissedilen Sıcaklık: {current['apparent_temperature']}°C",
            "zaman": su_an
        }
    except Exception as e:
        data = {"istasyon": "Hata", "sicaklik": 0, "durum": "API Hatası", "mesaj": "Bağlantı Kesildi", "zaman": "--"}
        
    return jsonify(data)

if __name__ == '__main__':
    application.run(port=5000)
