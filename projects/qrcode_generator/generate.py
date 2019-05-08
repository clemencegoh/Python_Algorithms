# For CLI
from jinja2 import Template
from generate_receipt import generate_receipt, verify_receipt
from generate_html import create_html_receipt
import time
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates a html file with desired QR code")
    parser.add_argument('-data', help="input json data file to be encoded")
    parser.add_argument('-qr', help='filepath for QR code')
    parser.add_argument('-out', help='filepath for html outfile')

    args = parser.parse_args()

    if not args.data or not args.qr or not args.out:
        parser.print_help()
        exit(0)

    # filter through args
    if ".png" not in args.qr:
        print('qr needs to have a .png extension')
        exit(0)
    if ".html" not in args.out:
        print('out needs to be a .html extension')
        exit(0)

    with open(args.data, "r") as json_file:
        receipt = generate_receipt(json_file.read())

    create_html_receipt(receipt, args.qr, args.out)