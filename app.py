
from flask import Flask
import os
import subprocess
import datetime

app = Flask(__name__)

def get_top_output():
    """Run 'top' command and return the output."""
    try:
        return subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    full_name = "Your Full Name"  # Replace with your actual full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = get_top_output()

    return f"""
    <html>
    <head><title>HTop Output</title></head>
    <body>
        <h1>Name: {full_name}</h1>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
