# src/utils/pdf_utils.py
from fpdf import FPDF
from io import BytesIO

def generate_pdf(title: str, content: str) -> BytesIO:
    """Generate PDF report and return as in-memory BytesIO file"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, content)
    
    # Use output(dest='S') to get PDF as a byte string
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    
    pdf_buffer = BytesIO(pdf_bytes)
    pdf_buffer.seek(0)
    return pdf_buffer
