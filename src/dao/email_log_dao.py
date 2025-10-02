from typing import Optional, List, Dict
from datetime import datetime
from src.config import get_supabase

sb = get_supabase()

class EmailLogDAO:
    """Data Access Object for Email Logs"""
    def __init__(self):
        self.sb = sb

    def log_email(self, customer_id: int, report_id: int, status: str, sent_to: str) -> Optional[Dict]:
        payload = {
            "customer_id": customer_id,
            "report_id": report_id,
            "sent_to": sent_to,
            "status": status,
            "sent_at": datetime.utcnow().isoformat()
        }
        self.sb.table("email_log").insert(payload).execute()
        resp = self.sb.table("email_log").select("*").eq("customer_id", customer_id).eq("report_id", report_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def list_logs(self, limit: int = 100) -> List[Dict]:
        resp = self.sb.table("email_log").select("*").limit(limit).execute()
        return resp.data or []

    def get_log_by_id(self, log_id: int) -> Optional[Dict]:
        resp = self.sb.table("email_log").select("*").eq("email_id", log_id).limit(1).execute()
        return resp.data[0] if resp.data else None

# Singleton instance
email_log_dao = EmailLogDAO()
