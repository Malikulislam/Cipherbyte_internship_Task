from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


# Set up the PDF document
doc = canvas.Canvas("receipt.pdf", pagesize=A4)

# Set up the font and font size
doc.setFont("Helvetica", 12)

# Set up the margins
margin_left = 2.2 * inch
margin_top = 10 * inch

# Set up the receipt data
receipt_data = {
    "date": "2023-02-20",
    "transaction_id": "TRX123456",
    "customer_name": "Malikul Islam",
    "items": [
        {"item_name": "Item 1", "quantity": 2, "price": 10.99},
        {"item_name": "Item 2", "quantity": 1, "price": 5.99},
        {"item_name": "Item 3", "quantity": 3, "price": 7.99}
    ],
    "subtotal": 34.97,
    "tax": 2.99,
    "total": 37.96
}

# Draw the receipt header
doc.drawString(margin_left, margin_top + 1 * inch, "Payment Receipt")
doc.drawString(margin_left, margin_top + 0.5 * inch, "Date: " + receipt_data["date"])
doc.drawString(margin_left, margin_top + 0.2 * inch, "Transaction ID: " + receipt_data["transaction_id"])

# Draw the customer information
doc.drawString(margin_left, margin_top - 0.2 * inch, "Customer Name: " + receipt_data["customer_name"])

# Draw the items table
doc.drawString(margin_left, margin_top - 1 * inch, "Items:")
doc.drawString(margin_left+1.8*inch, margin_top - 1 * inch, "Quantity")
doc.drawString(margin_left+3*inch, margin_top - 1 * inch, "Amount")
doc.line(margin_left, margin_top - 1.1 * inch, margin_left + 4 * inch, margin_top - 1.1 * inch)
for i, item in enumerate(receipt_data["items"]):
    doc.drawString(margin_left, margin_top - 1.5 * inch - i * 0.2 * inch, item["item_name"])
    doc.drawString(margin_left + 2 * inch, margin_top - 1.5 * inch - i * 0.2 * inch, str(item["quantity"]))
    doc.drawString(margin_left + 3 * inch, margin_top - 1.5 * inch - i * 0.2 * inch, "${:.2f}".format(item["price"]))

# Draw the subtotal, tax, and total
doc.drawString(margin_left, margin_top - 3 * inch, "Subtotal:")
doc.drawString(margin_left+2*inch,margin_top-3*inch,f"${receipt_data['subtotal']:.2f}")
doc.drawString(margin_left, margin_top - 3.2 * inch, "Tax:")
doc.drawString(margin_left+2*inch,margin_top-3.2*inch,f"${receipt_data['tax']:.2f}")
doc.drawString(margin_left, margin_top - 3.4 * inch, "Total:")
doc.drawString(margin_left+2*inch,margin_top-3.4*inch,f"${receipt_data['total']:.2f}")
# Save the PDF document
doc.save()
