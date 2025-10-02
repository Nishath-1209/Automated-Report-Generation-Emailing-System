from typing import List, Dict
from src.dao.email_log_dao import email_log_dao

class EmailLogService:
    """Service layer for retrieving email logs"""
    def __init__(self):
        self.dao = email_log_dao

    def get_email_logs(self, limit: int = 10) -> List[Dict]:
        """Fetch recent email logs"""
        return self.dao.list_logs(limit)

# Singleton instance
email_log_service = EmailLogService()
