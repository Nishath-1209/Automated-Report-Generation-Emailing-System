import streamlit as st
from src.services.customer_service import customer_service
from src.services.report_service import report_service
from src.services.scheduler_service import scheduler_service
from src.services import email_log_service

# Supabase config
supabase_url = st.secrets["SUPABASE"]["SUPABASE_URL"]
supabase_key = st.secrets["SUPABASE"]["SUPABASE_KEY"]

# SMTP config
smtp_server = st.secrets["SMTP"]["SMTP_SERVER"]
smtp_port = st.secrets["SMTP"]["SMTP_PORT"]
smtp_user = st.secrets["SMTP"]["SMTP_USER"]
smtp_pass = st.secrets["SMTP"]["SMTP_PASS"]

# Main title
st.markdown(
    """
    <h1 style='color:#4CAF50; font-family: Verdana;'>🚀 Automated Report Generation & Emailing System</h1>
    <p style='font-size:18px; color:gray;'>Manage customers, reports, scheduling, and email logs efficiently.</p>
    <hr>
    """,
    unsafe_allow_html=True,
)

# Horizontal top menu
menu = ["Customer", "Report", "Send Report", "Scheduler", "Email Logs"]
choice = st.radio("Menu", menu, horizontal=True)

# ----------------- Customer -----------------
if choice == "Customer":
    st.subheader("Customer Management")
    action = st.radio("Select Action", ["Add", "List", "Update"], horizontal=True)

    if action == "Add":
        with st.form("add_customer_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")

            submitted = st.form_submit_button("Add Customer")
            if submitted:
                if not name or not email:
                    st.error("Name and Email are required!")
                else:
                    result = customer_service.add_customer(name, email, phone)
                    st.success(f"Customer Added: {result}")

    elif action == "List":
        customers = customer_service.list_customers()
        if customers:
            st.table(customers)
        else:
            st.info("No customers found.")

    elif action == "Update":
        with st.form("update_customer_form"):
            cust_id = st.number_input("Customer ID", min_value=1)

            name = st.text_input("New Name")
            email = st.text_input("New Email")
            phone = st.text_input("New Phone")
            submitted = st.form_submit_button("Update Customer")

            if submitted:
                fields = {k: v for k, v in {"name": name, "email": email, "phone": phone}.items() if v}
                if not fields:
                    st.warning("Please provide at least one field to update.")
                else:
                    result = customer_service.update_customer(cust_id, fields)
                    st.success(f"Customer Updated: {result}")

# ----------------- Report -----------------
elif choice == "Report":
    st.subheader("Report Management")
    action = st.radio("Select Action", ["Add", "List", "Update", "Delete"], horizontal=True)

    if action == "Add":
        with st.form("add_report_form"):
            customer_id = st.number_input("Customer ID", min_value=1)
            title = st.text_input("Title")
            content = st.text_area("Content")
            submitted = st.form_submit_button("Add Report")

            if submitted:
                if not title or not content:
                    st.error("Title and Content are required!")
                else:
                    result = report_service.add_report(customer_id, title, content)
                    st.success(f"Report Added: {result}")

    elif action == "List":
        reports = report_service.list_reports()
        if reports:
            st.table(reports)
        else:
            st.info("No reports found.")

    elif action == "Update":
        with st.form("update_report_form"):
            report_id = st.number_input("Report ID", min_value=1)
            title = st.text_input("New Title")
            content = st.text_area("New Content")
            submitted = st.form_submit_button("Update Report")

            if submitted:
                if not title and not content:
                    st.warning("Provide at least one field to update.")
                else:
                    result = report_service.edit_report(report_id, title, content)
                    st.success(f"Report Updated: {result}")

    elif action == "Delete":
        with st.form("delete_report_form"):
            report_id = st.number_input("Report ID", min_value=1)
            submitted = st.form_submit_button("Delete Report")

            if submitted:
                result = report_service.remove_report(report_id)
                st.success(f"Report Deleted: {result}")

# ----------------- Send Report -----------------
elif choice == "Send Report":
    st.subheader("Send Report via Email")
    with st.form("send_report_form"):
        customer_id = st.number_input("Customer ID", min_value=1)
        title = st.text_input("Report Title")
        content = st.text_area("Report Content")
        submitted = st.form_submit_button("Send Email")

        if submitted:
            if not title or not content:
                st.error("Title and Content are required!")
            else:
                result = scheduler_service.generate_and_send_report(customer_id, title, content)
                st.success(f"Report Sent: {result}")

# ----------------- Scheduler -----------------
elif choice == "Scheduler":
    st.subheader("Run Scheduler")
    if st.button("Run Scheduler Now"):
        from src.cli.scheduler import run_scheduler
        run_scheduler()
        st.success("Scheduler Run Completed")

# ----------------- Email Logs -----------------
elif choice == "Email Logs":
    st.subheader("Recent Email Logs")
    limit = st.number_input("Number of logs to show", min_value=1, value=10)
    if st.button("Show Logs"):
        logs = email_log_service.get_email_logs(limit=limit)
        if logs:
            st.table(logs)
        else:
            st.info("No email logs found.")
