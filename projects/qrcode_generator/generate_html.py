from jinja2 import Template
from generate_receipt import generate_receipt, verify_receipt
from simple_qr import encoding, decoding
import time
import json
import argparse

saved_QR = {}

def create_html_receipt(receipt, filepath):
    simple_counter = 0
    path = encoding(receipt, "temp"+str(simple_counter)+".png")
    simple_counter += 1

    with open('receipt_template.html', "r") as f:
        contents = f.read()
        Template(contents).stream(qr_image=path).dump(filepath)


if __name__=='__main__':
    # sample data for receipt
    data = {
        "ID": "",
        "Person": "User1",
        "Ticket": "Normal",
        "Price": 50,
        "Paid": True,
        "Time_Stamp": time.time(),
        "Signature": "",
    }

    receipt = generate_receipt(json.dumps(data))
    print(verify_receipt(receipt))

    create_html_receipt(receipt, "example.html")