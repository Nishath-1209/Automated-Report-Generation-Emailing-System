from typing import List, Dict
from src.dao.email_log_dao import email_log_dao

class EmailLogService:
    """Service layer for retrieving and logging email logs"""
    def __init__(self):
        self.dao = email_log_dao

    def get_email_logs(self, limit: int = 10) -> List[Dict]:
        """Fetch recent email logs"""
        return self.dao.list_logs(limit)

    def log_email(self, customer_id: int, report_id: int, status: str, sent_to: str) -> Dict:
        """Save a new email log"""
        return self.dao.log_email(
            customer_id=customer_id,
            report_id=report_id,
            status=status,
            sent_to=sent_to
        )

# Singleton instance
email_log_service = EmailLogService()
