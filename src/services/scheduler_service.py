# src/services/scheduler_service.py
from src.services.report_service import report_service
from src.services.email_service import email_service
from src.services.customer_service import customer_service

class SchedulerService:
    """
    Service to automate report generation and emailing
    """
    def __init__(self):
        self.report_service = report_service
        self.email_service = email_service
        self.customer_service = customer_service

    def generate_and_send_report(self, customer_id: int, title: str, content: str) -> dict:
        """Generate a report and email it to customer"""
        customer = self.customer_service.get_customer_by_id(customer_id)
        if not customer:
            return {"error": "Customer not found"}

        # Create report
        report = self.report_service.add_report(customer_id, title, content)

        # Send email
        subject = f"Your Report: {title}"
        body = f"Hello {customer['name']},\n\nPlease find your report below:\n\n{content}"
        email_log = self.email_service.send_email(customer["email"], subject, body, customer_id, report["report_id"])

        return {"report": report, "email_log": email_log}

# Singleton instance
scheduler_service = SchedulerService()
