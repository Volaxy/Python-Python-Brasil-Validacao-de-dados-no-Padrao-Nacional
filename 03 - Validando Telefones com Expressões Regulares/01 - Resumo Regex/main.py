import re


def __main__():
    # pattern = "[0-9][a-z][0-9]" - This pattern finds "1f6", "3h9c", ...
    # The {x} indicates how many times the condition before will be repeat
    # pattern = "[0-9][a-z]{2}[0-9]" - This pattern finds "3gf7", "8gf9", ...
    # text = "123 1ag2 1cc aa1"

    # The "\w" indicates that it must contain a digit or a letter
    pattern = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
    text = "horse rodrigo123@gmail.com.br apple"

    # The "re.search()" receive the pattern and the text, and return the position and the string where it found the
    # expression or returns "None"
    response = re.search(pattern, text)

    # print(response)
    # The ".group()" returns the string match with the pattern
    print(response.group())


if __name__ == "__main__":
    __main__()
