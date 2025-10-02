# Automated-Report-Generation-Emailing-System

🚀 Automated Report Generation & Emailing System

A Python-based system that automatically generates and sends reports to customers, using Supabase for database management and a layered architecture for clean business logic.

📝 Table of Contents

📝 Project Overview

⚙️ Features

📂 Directory Structure

🛠 Setup

💻 Commands & Usage

🚀 Example Workflows

📧 Email Logs

🏁 Conclusion

✨ Future Enhancements




📝 Project Overview

Manual reporting is time-consuming. This system provides:

✅ Automated report creation

✅ Email delivery to customers

✅ Full tracking of sent reports

✅ Clean separation of concerns: CLI → Services → DAO → Database

Built with Python and Supabase, this project is ideal for businesses needing automated reporting with minimal manual intervention.

⚙️ Features

Add, update, and list customers & reports

Send reports via email

Track email sending status and timestamps

Retry mechanism for failed emails

Business logic implemented via Services layer

📂 Directory Structure
Automated-Report-Generation-Emailing-System/
```
├── src/
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── main.py            # CLI commands
│   │   └── scheduler.py       # Scheduler CLI
│   ├── dao/
│   │   ├── __init__.py
│   │   ├── customer_dao.py    # Customer DB operations
│   │   ├── report_dao.py      # Report DB operations
│   │   └── email_log_dao.py   # Email log DB operations
│   ├── services/
│   │   ├── __init__.py
│   │   ├── customer_service.py
│   │   ├── report_service.py
│   │   ├── email_service.py   # Handles email sending
│   │   └── scheduler_service.py
│   └── utils/
│       ├── __init__.py
│       ├── formatter.py       # Formatting helpers
│       └── config.py          # Config & environment variables
├── .env                        # Email & DB configuration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```
🛠 Setup

Clone the repository:
```
git clone <your-repo-url>

cd Automated-Report-Generation-Emailing-System

```
Create a virtual environment:
```
python -m venv venv

source venv/bin/activate # Linux / macOS

venv\Scripts\activate          # Windows

```
Install dependencies:
```
pip install -r requirements.txt

```
Configure .env with your Supabase and email settings:
```
EMAIL_HOST=smtp.example.com

EMAIL_PORT=587

EMAIL_USER=your-email@example.com

EMAIL_PASSWORD=your-email-password

SUPABASE_URL=https://xyz.supabase.co

SUPABASE_KEY=your-supabase-key
```
💻 Commands & Usage

All commands run via CLI:
```
python -m src.cli.main <command> [options]
```
💻 Customer Commands

All commands run via CLI:

Description: Add a new customer to the system.
```
python -m src.cli.main customer add --name "<Customer Name>" --email "<Customer Email>"
```

Description: List all customers in the database.
```
python -m src.cli.main customer list
```

Description: Update details of an existing customer.
```

python -m src.cli.main customer update --customer_id <ID> --name "<New Name>" --email "<New Email>"
```

Report Commands

```
report add --customer_id <id> --title <title> --content <content>	# Add a new report

report update --report_id <id> --title <title> --content <content>	# Update an existing report

report list	List all reports
```

Email Commands


Command	Description
```
send-report --customer_id <id> --title <title> --content <content> Send a report via email
```
list-email-logs
```
View logs of sent emails
```
Scheduler (Optional)

Command	Description

run-scheduler	                   Run scheduled report emails

🚀 Example Workflows

Add Customer:
```
python -m src.cli.main customer add --name "Nishath Tabassum" --email "23b81a6724@cvr.ac.in"

```
Add Report:
```
python -m src.cli.main report add --customer_id 2 --title "September Performance & Insights" --content "Detailed report content."

```
Send Report via Email:
```
python -m src.cli.main send-report --customer_id 2 --title "September 2025 Report" --content "Dear Nishath, ... report content ..."
```

Update Report:
```
python -m src.cli.main report update --report_id 69 --title "Updated Report Title" --content "New content here"
```

List Email Logs:
```
python -m src.cli.main list-email-logs
```
📧 Email Logs

Each email is tracked with:

email_id

report_id

customer_id

sent_to

status (SENT / FAILED)

sent_at timestamp

Example:
```
{
  "email_id": 59,
  "report_id": 69,
  "customer_id": 2,
  "sent_to": "23b81a6724@cvr.ac.in",
  "status": "SENT",
  "sent_at": "2025-09-29T07:24:32.191571"
}
```
🏁 Conclusion

The Automated Report Generation & Emailing System streamlines creating, sending, and tracking reports with minimal manual effort.

✅ Scalable – easily add more customers, reports, or email logic

✅ Reliable – built-in logging and retry mechanisms ensure delivery

✅ Flexible – can integrate with other databases, APIs, or cloud providers

💡 For small businesses or enterprise setups, this project acts as a strong foundation for automated communication and reporting.

✨ Future Enhancements

Add advanced analytics for reports

Implement multi-channel notifications (SMS, WhatsApp, Slack)

Enable report scheduling and recurring emails

Integrate AI-driven report summarization

Add role-based access control for users
