from flask import Flask
from flask import request, jsonify
from datetime import datetime


app = Flask(__name__)
@app.route('/api')
def get_info():
    # Get the value of the 'slack_name' parameter from the request URL
    slack_name = request.args.get('Damien_Ayine')
    
    # Get the value of the 'track' parameter from the request URL
    track = request.args.get('backend')
    
    # Get the current day using the datetime module and format it as a string
    current_day = datetime.now().strftime('%A')
    
    # Get the current UTC time using the datetime module and format it as a string
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Create a dictionary containing the information to be returned as JSON
    info = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': 'https://github.com/Damiennsoh/Backend-Internships/blob/main/endpoint_task/endpoint.py',
        'github_repo_url': 'https://github.com/Damiennsoh/Backend-Internships',
        'status_code': 'success'
    }

    # Return the information as JSON response
    return jsonify(info)
if __name__ == '__main__':
    app.run()


