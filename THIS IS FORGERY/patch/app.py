from flask import Flask
from flask import request
import requests
from urllib.parse import urlparse


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
        return "Welcome Admin! You've succesfully exploited a server side request forgery vulnerability!"
    else:
        return "Access Denied"
@app.route('/ssrf', methods=['GET'])
def ssrf():
    url = request.args.get('url')
    safe_host = ['worldtimeapi.org']
    safe_content_type = ['application/json']
    url_object = urlparse(url)
    if url_object.hostname not in safe_host:
        return "You've entered a bad URL!"
    try:
        r = requests.get(url)
        body = r.text
        return 'Here\'s the Time:<br>' + body
    except Exception as e:
        return str(e)

app.run(host='0.0.0.0', port=8181)