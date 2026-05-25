from flask import Flask, render_template, request
import os
import datetime
import platform

app = Flask(__name__)

assignments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add_assignment' in request.form:
            title = request.form.get('assignment_title')
            link = request.form.get('assignment_link')
            if title:
                assignments.append({'title': title, 'link': link})
        else:
            # Simple handler for guestbook submission
            name = request.form.get('name')
            message = request.form.get('message')
            # Could save to db here, but for simulation we just render
    
    # We try to match the timestamp format from the screenshot: 24/5/2026, 8:24:58 pm
    now = datetime.datetime.now()
    timestamp = now.strftime("%d/%m/%Y, %I:%M:%S %p").lower()
    
    # Platform
    plat = platform.system()
    if plat == 'Windows':
        plat = 'Win32'
        
    server_info = {
        'hostname': request.host,
        'platform': plat,
        'timestamp': timestamp,
        'user_agent': request.headers.get('User-Agent')
    }
    
    return render_template('index.html', server_info=server_info, assignments=assignments)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port, debug=True)
