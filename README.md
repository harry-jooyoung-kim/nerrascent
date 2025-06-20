# Narrascent Pebble Flask App

This minimal Flask application serves the static HTML pages for the Narrascent Pebble website.

## Setup
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000/` in your browser.

Available routes:
- `/` – Home page.
- `/how-it-works` – How it works.
- `/pebble` – Product detail.
- `/shop` – Palette shop.
- `/compose` – Compose web app.
- `/library` – Library page.
- `/support` – Support & FAQ.
- `/demo` – POST endpoint used by the home page interactive demo.
- `/subscribe` – POST endpoint to send a welcome email when subscribing.

### Email configuration
To actually send emails, set the following environment variables before running the app:

- `SMTP_SERVER` – address of your SMTP server (default `localhost`)
- `SMTP_PORT` – port to connect to (default `25`)
- `SMTP_USERNAME` – username for SMTP authentication, if required
- `SMTP_PASSWORD` – password for SMTP authentication, if required
- `SMTP_USE_TLS` – set to `true` to enable TLS


