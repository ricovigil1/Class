# Author: Enrique Vigil
# Date: 10.24.26
# Assignment: Prog Assign_7 - Strings

# translates the letters in a telephone number to their equivalents
def translate_phone_number(phone_number):
    translated_number = ""

    # converts the letters to uppercase so the lowercase letters also work
    for character in phone_number.upper():
        if character in "ABC":
            translated_number += "2"
        elif character in "DEF":
            translated_number += "3"
        elif character in "GHI":
            translated_number += "4"
        elif character in "JKL":
            translated_number += "5"
        elif character in "MNO":
            translated_number += "6"
        elif character in "PQRS":
            translated_number += "7"
        elif character in "TUV":
            translated_number += "8"
        elif character in "WXYZ":
            translated_number += "9"
        else:
            # keep numbers and hyphens unchanged
            translated_number += character

    return translated_number


def main():
    phone_number = input(
        "Please enter a telephone number in the format XXX-XXX-XXXX: "
    )

    translated_number = translate_phone_number(phone_number)
    print("Translated telephone number:", translated_number)


# run the program
main()
