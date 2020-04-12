"""
Compress to show string and number behind
"""

def compressedString(message):
    # catch empty or single
    if len(message) <= 1:
        return message

    # use a stack and counter
    last_alpha = ""
    count = 1

    return_string = ""

    for msg in message:
        if last_alpha != msg:
            # append to return string
            return_string += last_alpha
            if count > 1:
                return_string += str(count)
            last_alpha = msg
            count = 1
        else:
            count += 1
    # last append
    return_string += last_alpha
    if count > 1:
        return_string += str(count)

    return return_string
        

# driver
print(compressedString("abbbbccccc"))