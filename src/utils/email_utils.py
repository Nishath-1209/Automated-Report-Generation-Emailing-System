import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from streamlit import secrets

def send_email(to_email, subject, body, attachment_data=None, attachment_name=None):
    smtp_server = secrets["SMTP"]["SMTP_SERVER"]
    smtp_port = secrets["SMTP"]["SMTP_PORT"]
    smtp_user = secrets["SMTP"]["SMTP_USER"]
    smtp_pass = secrets["SMTP"]["SMTP_PASS"]

    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg["Subject"] = subject

    # Body
    msg.attach(MIMEText(body, "plain"))

    # 📎 Attachment (if provided)
    if attachment_data and attachment_name:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment_data)
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={attachment_name}")
        msg.attach(part)

    # SMTP Send
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
