from flask import Flask, render_template, request, jsonify
import os
import smtplib
from email.message import EmailMessage


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('howitworks.html')

@app.route('/pebble')
def pebble():
    return render_template('order.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/compose')
def compose():
    return render_template('create.html')

@app.route('/library')
def library():
    return render_template('recipes.html')
@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/demo', methods=['POST'])
def demo():
    data = request.get_json(force=True)
    # simple stub returning fixed notes regardless of input
    response = {
        'top': ['Citrus', 'Bergamot'],
        'mid': ['Lavender', 'Rosemary'],
        'base': ['Cedarwood', 'Musk']
    }
    return jsonify(response)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json(force=True)
    email = data.get('email')
    if not email:
        return jsonify({'success': False}), 400
    msg = EmailMessage()
    msg['Subject'] = 'Welcome to Narrascent'
    msg['From'] = 'noreply@narrascent.com'
    msg['To'] = email
    msg.set_content('Welcome to Narrascent! We are excited to have you.')

    smtp_server = os.environ.get('SMTP_SERVER', 'localhost')
    smtp_port = int(os.environ.get('SMTP_PORT', '25'))
    smtp_user = os.environ.get('SMTP_USERNAME')
    smtp_pass = os.environ.get('SMTP_PASSWORD')
    use_tls = os.environ.get('SMTP_USE_TLS', 'false').lower() == 'true'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            if use_tls:
                smtp.starttls()
            if smtp_user and smtp_pass:
                smtp.login(smtp_user, smtp_pass)
            smtp.send_message(msg)
    except Exception as e:
        print('Error sending email:', e)
    return jsonify({'success': True})
if __name__ == "__main__":
    # Run the development server when the script is executed directly
    # This allows `python app.py` to start the Flask application as
    # documented in the README.
    app.run(debug=True)

