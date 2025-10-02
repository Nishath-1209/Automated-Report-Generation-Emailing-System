# src/utils/formatter.py

def format_report(title: str, content: str, customer_name: str = "") -> str:
    """Format report content for email or display"""
    header = f"Report Title: {title}\n"
    if customer_name:
        header = f"Hello {customer_name},\n\n" + header
    body = f"{content}\n\n-- End of Report --"
    return header + body
