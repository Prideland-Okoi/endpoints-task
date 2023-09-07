from flask import Flask, request, jsonify
import datetime
import requests
import pytz

app = Flask(__name__)

@app.route('/get-info', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    tracks = ["vMarketing","design","frontend","mobile", "backend"]
    if track not in tracks:
        return jsonify({"error": "Invalid track selection"}), 400
    current_utc_time = datetime.datetime.now(pytz.utc)
    utc_offset_hours = current_utc_time.utcoffset().total_seconds()/3600
    if abs(utc_offset_hours) > 2:
        return jsonify({"error":"UTC time offset exceeds +/-2 hours"}),400
    file_url = requests.get('https://api.github.com/repos/Prideland-Okoi/python-flask-endpoints/commits/HEAD').json()['url']
    source_code_url = 'https://github.com/prideland-okoi/python-flask-endpoints'
    json_response = {
        'slack_name': slack_name,
        'day_of_week': datetime.datetime.now().strftime("%A"),
        'current_utc_time': current_utc_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        'track': track,
        'file_url': file_url,
        'source_code_url': source_code_url,
        'status_code': 200
    }

    return jsonify(json_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

