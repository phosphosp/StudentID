from flask import Flask, render_template, request
import re

app = Flask(__name__)

def is_xss(input_str):
    xss_patterns = [
        r"<script.*?>.*?</script.*?>",
        r"on\w+\s*=",
        r"javascript:",
        r"document\.cookie",
        r"<.*?iframe.*?>",
    ]
    for pattern in xss_patterns:
        if re.search(pattern, input_str, re.IGNORECASE):
            return True
    return False

def is_sql_injection(input_str):
    sql_patterns = [
        r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
        r"\b(select|update|delete|insert|drop|alter|create|truncate)\b",
        r"(\bor\b|\band\b).*(=|like)",
        r"union(\s+all)?(\s+select)?",
    ]
    for pattern in sql_patterns:
        if re.search(pattern, input_str, re.IGNORECASE):
            return True
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input', '').strip()

    if is_xss(user_input) or is_sql_injection(user_input):
        return render_template('index.html', error="Invalid input detected. Please try again.")
    
    return render_template('display.html', search_term=user_input)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)