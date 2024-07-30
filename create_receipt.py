from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_receipt(file_path, company_info, customer_info, items, total_amount):
    """
    Create a payment receipt PDF.

    Args:
        file_path (str): The file path where the PDF will be saved.
        company_info (dict): A dictionary containing company information.
        customer_info (dict): A dictionary containing customer information.
        items (list): A list of dictionaries containing item details.
        total_amount (float): The total amount to be paid.

    Example:
        company_info = {
            'name': 'ABC Store',
            'address': '123 Main Street',
            'city': 'Anytown',
            'state': 'CA',
            'zip_code': '12345',
            'phone': '555-1234'
        }

        customer_info = {
            'name': 'John Doe',
            'address': '456 Elm Street',
            'city': 'Othertown',
            'state': 'TX',
            'zip_code': '67890',
            'phone': '555-5678'
        }

        items = [
            {'description': 'Item 1', 'quantity': 2, 'price': 10.00},
            {'description': 'Item 2', 'quantity': 1, 'price': 15.00}
        ]

        total_amount = 35.00

        create_receipt('receipt.pdf', company_info, customer_info, items, total_amount)
    """
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Draw company information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 50, company_info['name'])
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 65, company_info['address'])
    c.drawString(50, height - 80, f"{company_info['city']}, {company_info['state']} {company_info['zip_code']}")
    c.drawString(50, height - 95, f"Phone: {company_info['phone']}")

    # Draw customer information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 130, "Bill To:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 145, customer_info['name'])
    c.drawString(50, height - 160, customer_info['address'])
    c.drawString(50, height - 175, f"{customer_info['city']}, {customer_info['state']} {customer_info['zip_code']}")
    c.drawString(50, height - 190, f"Phone: {customer_info['phone']}")

    # Draw table header
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, height - 230, "Description")
    c.drawString(250, height - 230, "Quantity")
    c.drawString(350, height - 230, "Price")
    c.drawString(450, height - 230, "Total")

    # Draw items
    y = height - 250
    for item in items:
        c.setFont("Helvetica", 10)
        c.drawString(50, y, item['description'])
        c.drawString(250, y, str(item['quantity']))
        c.drawString(350, y, f"${item['price']:.2f}")
        c.drawString(450, y, f"${item['quantity'] * item['price']:.2f}")
        y -= 20

    # Draw total amount
    c.setFont("Helvetica-Bold", 10)
    c.drawString(350, y - 20, "Total Amount:")
    c.drawString(450, y - 20, f"${total_amount:.2f}")

    # Save the PDF
    c.showPage()
    c.save()

if __name__ == "__main__":
    company_info = {
        'name': 'ABC Store',
        'address': '123 Main Street',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345',
        'phone': '555-1234'
    }

    customer_info = {
        'name': 'John Doe',
        'address': '456 Elm Street',
        'city': 'Othertown',
        'state': 'TX',
        'zip_code': '67890',
        'phone': '555-5678'
    }

    items = [
        {'description': 'Item 1', 'quantity': 2, 'price': 10.00},
        {'description': 'Item 2', 'quantity': 1, 'price': 15.00}
    ]

    total_amount = 35.00

    create_receipt('receipt.pdf', company_info, customer_info, items, total_amount)
  
