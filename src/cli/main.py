import argparse
from src.services.customer_service import customer_service
from src.services.report_service import report_service
from src.services.scheduler_service import scheduler_service
from src.services import email_log_service   # ✅ add this

def main():
    parser = argparse.ArgumentParser(description="Automated Report Generation & Emailing System")
    subparsers = parser.add_subparsers(dest="command")

    # ---------------- Customer Commands ----------------
    cust_parser = subparsers.add_parser("customer", help="Customer operations")
    cust_sub = cust_parser.add_subparsers(dest="action")

    add_cust = cust_sub.add_parser("add", help="Add a new customer")
    add_cust.add_argument("--name", required=True)
    add_cust.add_argument("--email", required=True)
    add_cust.add_argument("--phone", required=True)

    cust_sub.add_parser("list", help="List all customers")

    update_cust = cust_sub.add_parser("update", help="Update a customer")
    update_cust.add_argument("--cust_id", type=int, required=True)
    update_cust.add_argument("--name", required=False)
    update_cust.add_argument("--email", required=False)
    update_cust.add_argument("--phone", required=False)

    delete_cust = cust_sub.add_parser("delete", help="Delete a customer")
    delete_cust.add_argument("--cust_id", type=int, required=True)

    # ---------------- Report Commands ----------------
    report_parser = subparsers.add_parser("report", help="Report operations")
    report_sub = report_parser.add_subparsers(dest="action")

    add_report = report_sub.add_parser("add", help="Add a report")
    add_report.add_argument("--customer_id", type=int, required=True)
    add_report.add_argument("--title", required=True)
    add_report.add_argument("--content", required=True)

    report_sub.add_parser("list", help="List all reports")

    edit_report = report_sub.add_parser("update", help="Update a report")
    edit_report.add_argument("--report_id", type=int, required=True)
    edit_report.add_argument("--title", required=False)
    edit_report.add_argument("--content", required=False)

    delete_report = report_sub.add_parser("delete", help="Delete a report")
    delete_report.add_argument("--report_id", type=int, required=True)

    # ---------------- Send Report Command ----------------
    send_report = subparsers.add_parser("send-report", help="Generate and send a report")
    send_report.add_argument("--customer_id", type=int, required=True)
    send_report.add_argument("--title", required=True)
    send_report.add_argument("--content", required=True)

    # ---------------- Scheduler Command ----------------
    subparsers.add_parser("run-scheduler", help="Run the report scheduler")

    # ---------------- Email Log Command ---------------- ✅ NEW
    log_parser = subparsers.add_parser("list-email-logs", help="List recent email logs")
    log_parser.add_argument("--limit", type=int, default=10, help="Number of logs to display")

    args = parser.parse_args()

    # ---------------- Execute Commands ----------------
    if args.command == "customer":
        if args.action == "add":
            print("Customer Added:", customer_service.add_customer(args.name, args.email, args.phone))
        elif args.action == "list":
            print("Customers:", customer_service.list_customers())
        elif args.action == "update":
            fields = {k: v for k, v in vars(args).items() if k in ["name", "email", "phone"] and v}
            print("Customer Updated:", customer_service.update_customer(args.cust_id, fields))
        elif args.action == "delete":
            print("Customer Deleted:", customer_service.delete_customer(args.cust_id))

    elif args.command == "report":
        if args.action == "add":
            print("Report Added:", report_service.add_report(args.customer_id, args.title, args.content))
        elif args.action == "list":
            print("Reports:", report_service.list_reports())
        elif args.action == "update":
            print("Report Updated:", report_service.edit_report(args.report_id, args.title, args.content))
        elif args.action == "delete":
            print("Report Deleted:", report_service.remove_report(args.report_id))

    elif args.command == "send-report":
        print("Report & Email Result:", scheduler_service.generate_and_send_report(args.customer_id, args.title, args.content))

    elif args.command == "run-scheduler":
        from src.cli.scheduler import run_scheduler
        run_scheduler()

    elif args.command == "list-email-logs":   # ✅ NEW
        logs = email_log_service.get_email_logs(limit=args.limit)
        for log in logs:
            print(log)

if __name__ == "__main__":
    main()
