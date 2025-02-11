from flask_mail import Message
from flask import current_app
from . import mail
from datetime import datetime
import threading

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, recipients, body):
    app = current_app._get_current_object()
    msg = Message(subject,
                 sender=app.config['MAIL_USERNAME'],
                 recipients=recipients)
    msg.body = body
    
    # Send email asynchronously
    threading.Thread(target=send_async_email,
                    args=(app, msg)).start()

def send_reminder_email(reminder):
    subject = f"Reminder: {reminder.topic}"
    body = f"""
    This is a reminder for: {reminder.topic}
    Time: {reminder.time}
    Frequency: {reminder.frequency}
    """
    # For now, we'll send to a default email. In production, use the user's email
    recipients = [current_app.config['MAIL_USERNAME']]
    send_email(subject, recipients, body) 