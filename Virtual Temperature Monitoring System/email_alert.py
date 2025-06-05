import smtplib
from email.message import EmailMessage
 
SENDER_EMAIL = "****"
RECEIVER_EMAIL = "****" 
APP_PASSWORD = "qhrn seca ydiq qtcc"  # Use Gmail App Password
 
def send_email_alert(temp):
    msg = EmailMessage()
    msg['Subject'] = "🚨 CRITICAL TEMPERATURE ALERT"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(f"Temperature reached CRITICAL level!\n\nCurrent Temperature: {temp}°C")
 
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        print("🚨 Email alert sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
