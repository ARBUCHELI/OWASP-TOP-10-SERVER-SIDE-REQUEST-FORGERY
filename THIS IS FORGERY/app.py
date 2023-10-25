from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
	CHECK THE TIME BASED ON THIS SYSTEM'S IP!
	<form action="/ssrf" id="time">
	<label>Please Enter Your URL</label>
	<input type="hidden" id="url" name="url" value="https://worldtimeapi.org/api/ip">
	</form>
	<button type="submit" form="time">Check the time!</button>

	'''

@app.route('/admin', methods=['GET'])
def admin():
    ip_addr = request.remote_addr
    if ip_addr == '127.0.0.1':
        return "Welcome, Admin! You've successfully exploited a server-side request forgery vulnerability!"
    else:
        return "Access Denied"
        
@app.route('/ssrf', methods=['GET'])
def ssrf():
    url = request.args.get('https://127.0.0.1:8181/admin')
    try:
        r = requests.get(url)
        body = r.text
        return 'Here\'s the Time:<br>' + body
    except Exception as e:
        return str(e)

app.run(host='0.0.0.0', port=8181)