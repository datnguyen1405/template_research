from flask import Flask, request, render_template, send_file, url_for
import os
from dotenv import load_dotenv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Route to render the form
@app.route('/')
def form():
    return render_template('form.html')


# Endpoint to process form data and generate the report
@app.route('/generate-report', methods=['POST'])
def generate_report():
    main_symbol = request.form['main_symbol']
    comp_symbol1 = request.form['comp_symbol1']
    comp_symbol2 = request.form['comp_symbol2']
    comp_symbol3 = request.form['comp_symbol3']

    # Call the function to generate the report
    report_path = generate_pdf_report(main_symbol, [comp_symbol1, comp_symbol2, comp_symbol3])

    # Render download page with the path to the generated report
    return render_template('download.html', file_path=report_path)


# Endpoint to download the generated report
@app.route('/download/<path:file_path>')
def download_report(file_path):
    # Serve the file for download
    return send_file(file_path, as_attachment=True)


# Function to generate the PDF report (replace with actual logic)
def generate_pdf_report(main_symbol, comparison_symbols):
    # Example code to generate a PDF (replace with actual logic)
    pdf_path = 'generated_report.pdf'

    # Use a PDF generation library like reportlab or fpdf here
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    # Create a PDF canvas
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.drawString(100, 750, f"Report for: {main_symbol}")
    c.drawString(100, 730, "Comparison Symbols:")

    # Write each comparison symbol to the PDF
    y_position = 710
    for symbol in comparison_symbols:
        c.drawString(100, y_position, f"- {symbol}")
        y_position -= 20  # Move down for the next symbol

    # Save the PDF
    c.save()

    return pdf_path


if __name__ == '__main__':
    # Set environment variables for 'SA_INFO' and 'API_KEY' for secure access
    os.environ['SA_INFO'] = 'your_sa_info_here'
    os.environ['API_KEY'] = 'your_api_key_here'

    # Run the Flask app
    app.run(debug=True)
