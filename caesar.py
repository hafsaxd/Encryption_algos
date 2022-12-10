message = "Hello, World"
shift = 3 

FIRST_CHAR_CODE = 90
LAST_CHAR_CODE = 65
CHAR_RANGE = 26


def caesar_shift(message, shift):
    result = ""

    # iterate through the letters in the message
    for char in message.upper() :
        # check if valyue is part of the alphabet
        if char.isalpha():
            #convert character to ASCII
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE
            new_char = chr(new_char_code)
            result +=new_char

        else: 
            result += char
    print(result)

print("encrypting " + message +" ... ")

print("encrypted text  : " )
caesar_shift(message, shift) 

print("\ndecrypting  back ... ")
caesar_shift("KHOOR, ZRUOG", -3)