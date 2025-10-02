# src/dao/report_dao.py
from typing import Optional, List, Dict
from src.config import get_supabase

sb = get_supabase()

class ReportDAO:
    """Data Access Object for Report-related DB operations"""
    def __init__(self):
        self.sb = sb

    def create(self, customer_id: int, title: str, content: str) -> Optional[Dict]:
        payload = {"customer_id": customer_id, "title": title, "content": content}
        self.sb.table("reports").insert(payload).execute()
        resp = self.sb.table("reports").select("*").eq("customer_id", customer_id).eq("title", title).limit(1).execute()
        return resp.data[0] if resp.data else None

    def read_all(self, limit: int = 100) -> List[Dict]:
        resp = self.sb.table("reports").select("*").limit(limit).execute()
        return resp.data or []

    def update(self, report_id: int, title: str = None, content: str = None) -> Optional[Dict]:
        fields = {}
        if title: fields["title"] = title
        if content: fields["content"] = content
        self.sb.table("reports").update(fields).eq("report_id", report_id).execute()
        resp = self.sb.table("reports").select("*").eq("report_id", report_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def delete(self, report_id: int) -> Optional[Dict]:
        resp_before = self.sb.table("reports").select("*").eq("report_id", report_id).limit(1).execute()
        row = resp_before.data[0] if resp_before.data else None
        self.sb.table("reports").delete().eq("report_id", report_id).execute()
        return row

    def get_report_by_id(self, report_id: int) -> Optional[Dict]:
        resp = self.sb.table("reports").select("*").eq("report_id", report_id).limit(1).execute()
        return resp.data[0] if resp.data else None

# Singleton instance
report_dao = ReportDAO()
