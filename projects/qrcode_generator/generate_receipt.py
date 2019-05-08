import time
import random
import string
import hashlib
import json


letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
current_nonce = ""
NoSQL_database = {}  # simulate NoSQL database


def generate_nonce(length):
    nonce = ''.join(random.choice(letters) for i in range(length))
    return nonce

def generate_receipt(json_data):
    """
    Fills in receipt fields with nonce and sig
    Appends nonce to create signature
    Nonce will be used as key in database

    :param json_data: data as json, compatible with web services
    :return: json data with updated fields
    """

    # replace with database
    global NoSQL_database

    nonce = generate_nonce(32)
    concat = json_data + str(nonce)

    m = hashlib.sha256()
    m.update(concat.encode())
    receipt_id = m.hexdigest()

    # update database
    json_data = json.loads(json_data)
    json_data["ID"] = receipt_id
    NoSQL_database[receipt_id] = json.dumps(json_data)
    json_data = json.dumps(json_data)

    return json_data


def verify_receipt(receipt):
    """
    This will probably have to be used with some sort of database for nonce
    :param nonce: nonce from database
    :param receipt: full json receipt from generate_receipt
    :return: bool
    """

    # replace with database
    global NoSQL_database

    json_data = json.loads(receipt)
    retrieved = NoSQL_database[json_data["ID"]]

    # simple verify
    if retrieved != receipt:
        return False
    return True


# for testing
data = {
    "ID": "",
    "Person": "User1",
    "Ticket": "Normal",
    "Price": 50,
    "Paid": True,
    "Time_Stamp": time.time(),
    "Signature": "",
}


if __name__=='__main__':
    # generate receipt and save to db
    receipt = generate_receipt(json.dumps(data))

    # get receipt and verify
    print(verify_receipt(receipt=receipt))

