# src/services/scheduler_service.py
from src.services.report_service import report_service
from src.services.email_service import email_service
from src.services.customer_service import customer_service
from src.services.email_log_service import email_log_service
from src.utils.email_utils import send_email
from src.utils.pdf_utils import generate_pdf  # PDF generator

class SchedulerService:
    """
    Service to automate report generation and emailing (with PDF attachments)
    """
    def __init__(self):
        self.report_service = report_service
        self.email_service = email_service
        self.customer_service = customer_service

    def generate_and_send_report(
        self,
        customer_id: int,
        title: str,
        content: str
    ) -> dict:
        """Generate a report, create PDF, email it, and log the email"""

        # 1️⃣ Get Customer
        customer = self.customer_service.get_customer_by_id(customer_id)
        if not customer:
            return {"error": f"❌ Customer ID {customer_id} not found"}

        # 2️⃣ Create & Save Report
        report = self.report_service.add_report(customer_id, title, content)

        # 3️⃣ Generate PDF
        pdf_file = generate_pdf(title, content)

        # 4️⃣ Prepare Email
        subject = f"Your Report: {title}"
        body = f"Hello {customer['name']},\n\nPlease find your report attached."

        # 5️⃣ Send Email with PDF attachment
        send_email(
            to_email=customer["email"],
            subject=subject,
            body=body,
            attachment_data=pdf_file.read(),
            attachment_name=f"{title}.pdf"
        )

        # 6️⃣ Log Email in Database
        email_log = email_log_service.log_email(
            customer_id=customer_id,
            report_id=report["report_id"],
            status="sent",
            sent_to=customer["email"]
        )

        return {
            "report": report,
            "email_log": email_log,
            "attachment_sent": True
        }

# Singleton instance
scheduler_service = SchedulerService()
