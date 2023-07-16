#!/usr/env/ python3

# a light cli app to practice typing.
import sys
import random
import time


def text_generator(chars, text_length):
    text = ""
    for i in range(text_length):
        if i != 0 and i  % 50 == 0:
            text += "\n"
        text += random.choice(chars)
        if random.randint(0, 1) == 1:
            text += " "

    return text.strip()


def severity(severint):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    char_gen = lambda x: [random.choice(alpha) for _ in range(x)]

    if severint == 0:
        chars = char_gen(2)
        text_length = 100
    elif severint == 1:
        chars = char_gen(5)
        text_length = 200
    elif severint == 2:
        chars = char_gen(10)
        text_length = 300
    elif severint == 3:
        chars = char_gen(15)
        text_length = 400
    elif severint == 4:
        chars = char_gen(26)
        text_length = 500
    else:
        return False

    return chars, text_length


def practice():
    print("\n~ Available levels : ")
    print("~ [0]- Completely Beginner \t [1]- Beginner\n\
~ [2]- A little experienced \t [3]- Experienced\n\
~ [4]- Proffessional")

    try:
        severint = int(input("\n~ Select your level to start the practice. : "))
        chars, text_length = severity(severint)
        text = text_generator(chars, text_length)
    except:
        print("~ Please select one of the available levels.")
        sys.exit()

    print(f"~ Practicing keys {chars} in {text_length} characters.")

    textsp = text.split("\n")
    hlen = len(max(textsp))+14
    print("~ Simple text:\n\n\t", "#"*hlen)

    for line in textsp:
        print(f"\t\t{line}")
    print("\t", "#"*hlen, "\n")

    if input("\n~ Are you ready[Y/n] :").upper() == "Y":
        print("~ Let's start in 3 seconds ....")
        time.sleep(3)
        stime = time.time()
        intext = input("\n~ ")
        etime = int(time.time() - stime)

        if len(intext) == 0:
            sys.exit()
        elif intext.strip() == "".join(textsp):
            print("~ Excellent, completely correct !")

        else:
            print("~ It's not quite correct!, had some mistakes!")

        print(f"~ {text_length} characters in {etime} seconds.\
            \n~ your avarage speed : {round(text_length/etime)} character per second.")


def main():
    print("\n", "\t"*3, "** PYTOUCH **\n")
    description = """~ A light cli app to practice typing in various levels.\
    \n~ From totally beginner to advanced and experienced typers.\n"""
    print(description)
    print("~ Note: PUT THE TERMINAL IN FULLSCREEN MODE.")
    #for ch in description:
    #    print(ch, end="")
    #    time.sleep(0.1)
    practice()

main()
