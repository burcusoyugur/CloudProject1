from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Frontend'in Backend ile konuşabilmesi için şart

@app.route('/api/data', methods=['GET'])
def get_data():
    # Burası veritabanından veri geliyor gibi simüle eder
    return jsonify({"mesaj": "Bulut Bilişim Projesi Backend Bağlantısı Başarılı!", "durum": "Aktif"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  