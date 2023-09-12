# Importing necessary dependencies/libraries
from flask import Flask, jsonify, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Retrieve the values of 'slack_name' and 'track' from the query parameters
    slack_name = request.args.get('slack_name', default='Damien_Ayine')
    track = request.args.get('track', default='backend')

    # Get the current UTC time
    current_time_utc = datetime.utcnow()

    # Add a timedelta of -2 seconds to the current UTC time
    lower_bound = current_time_utc - timedelta(seconds=2)

    # Add a timedelta of +2 seconds to the current UTC time
    upper_bound = current_time_utc + timedelta(seconds=2)

    # Format the current UTC time and bounds as strings
    current_time_str = current_time_utc.strftime('%Y-%m-%d %H:%M:%S')
    lower_bound_str = lower_bound.strftime('%Y-%m-%d %H:%M:%S')
    upper_bound_str = upper_bound.strftime('%Y-%m-%d %H:%M:%S')

    # Define the URLs for the GitHub file and repository
    github_file_url = 'https://github.com/Damiennsoh/Backend-Internships/blob/main/endpoint_task/endpoint.py'
    github_repo_url = 'https://github.com/Damiennsoh/Backend-Internships'

    # Create a response dictionary with the retrieved values and URLs
    response = {
        'slack_name': slack_name,
        'current_time_utc': current_time_str,
        'lower_bound_utc': lower_bound_str,
        'upper_bound_utc': upper_bound_str,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    # Return the response as JSON with a status code of 200
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
