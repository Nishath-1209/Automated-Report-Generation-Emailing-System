# src/services/report_service.py
from typing import Optional, List, Dict
from src.dao.report_dao import report_dao

class ReportService:
    """Service layer for report-related operations"""
    def __init__(self):
        self.dao = report_dao

    def add_report(self, customer_id: int, title: str, content: str) -> Optional[Dict]:
        """Create a new report for a customer"""
        return self.dao.create(customer_id, title, content)

    def edit_report(self, report_id: int, title: str = None, content: str = None) -> Optional[Dict]:
        """Update a report"""
        return self.dao.update(report_id, title, content)

    def remove_report(self, report_id: int) -> Optional[Dict]:
        """Delete a report"""
        return self.dao.delete(report_id)

    def list_reports(self, limit: int = 100) -> List[Dict]:
        """List all reports"""
        return self.dao.read_all(limit)

    def get_report_by_id(self, report_id: int) -> Optional[Dict]:
        """Get report by ID"""
        return self.dao.get_report_by_id(report_id)

# Singleton instance
report_service = ReportService()
