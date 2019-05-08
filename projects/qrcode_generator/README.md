# Simple QR code generation code
This mini-project aims to create a unique QR code based on receipts,
and generate a html receipt from there.
The generated html is a basic barebones html 
- Important installation: `pip install -r requirements.txt`
- How to use:
    - `python generate.py -h` brings up the help
    - Simple Example call:
    `python generate.py -data "data.json" -qr "example2.png" -out "example2.html" `
    - **NOTE:** This is meant to be used as a simple example only, 
    more edits are necessary for a full working implementation with 
    production code