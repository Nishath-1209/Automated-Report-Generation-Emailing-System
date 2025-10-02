import time
from src.services.scheduler_service import scheduler_service
from src.dao.report_dao import report_dao

def run_scheduler(interval_seconds: int = 60):
    """
    Run continuous scheduler to process pending reports.
    """
    print("Scheduler started...")
    while True:
        pending_reports = report_dao.read_all()  # Can filter for unsent reports if needed
        for report in pending_reports:
            try:
                scheduler_service.generate_and_send_report(
                    report["customer_id"], 
                    report["title"], 
                    report["content"]
                )
                print(f"Processed Report ID: {report['report_id']}")
            except Exception as e:
                print(f"Error processing Report ID {report['report_id']}: {e}")
        time.sleep(interval_seconds)
