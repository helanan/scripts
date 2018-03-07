def isPhoneNumber(input):
# step one: is the string 12 numbers?
    if len(input) != 12:
        return False
#step 2: first 3 characters in text consists of numeric characters?
    for i in range(0,3):
        if not input[i].isdecimal():
            return False
    if input[3] != '-':
        return False
    for i in range(4,7):
        if not input[i].isdecimal():
            return False
    if input[7] != '-':
        return False
    for i in range(8, 12):
        if not input[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
