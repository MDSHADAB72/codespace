from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the current server time in IST
    ist_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")

    # Get the top command output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    # Full name and system username
    full_name = "Md Shadab   "  # Replace with your actual name
    username = os.getenv('USER') or os.getenv('USERNAME')

    # Create HTML response
    return f"""
    <html>
    <body>
        <h1>System Info</h1>
        <p><strong>Full Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre><strong>Top Output:</strong>
{top_output}
        </pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
