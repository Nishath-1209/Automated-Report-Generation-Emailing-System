from typing import Optional, List, Dict
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS
from src.dao.email_log_dao import email_log_dao

class EmailService:
    """Service layer for sending emails and logging"""

    def __init__(self):
        self.dao = email_log_dao
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.smtp_user = SMTP_USER
        self.smtp_pass = SMTP_PASS

    def _send_raw_email(self, to_email: str, subject: str, body: str) -> bool:
        """Helper: actually send email (returns success/failure)"""
        try:
            msg = MIMEMultipart()
            msg["From"] = self.smtp_user
            msg["To"] = to_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port, timeout=30) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_pass)
                server.send_message(msg)

            return True
        except Exception as e:
            print(f"SMTP Error: {e}")
            return False

    def send_email(
        self, to_email: str, subject: str, body: str, customer_id: int, report_id: int
    ) -> Dict:
        """Send email with retries and log the result"""

        status = "FAILED"
        success = False

        # Retry mechanism
        for attempt in range(3):
            print(f"Sending email to {to_email} (attempt {attempt+1}/3)...")
            if self._send_raw_email(to_email, subject, body):
                status = "SENT"
                success = True
                break
            else:
                time.sleep(5)  # wait before retry

        # Log the attempt
        log = self.dao.log_email(customer_id, report_id, status, to_email)

        # Small delay to avoid rate limiting when sending bulk
        time.sleep(2)

        return log

    def list_email_logs(self, limit: int = 100) -> List[Dict]:
        """List email logs"""
        return self.dao.list_logs(limit)


# Singleton instance
email_service = EmailService()
