from find_address import FindAddress
import requests


def __main__():
    cep = FindAddress(84574857)

    content = cep.access_address()

    print(type(content.text))
    # Extract data from dictionary is easier than string
    print(type(content.json()))

    print(content.json()["cep"])
    print(content.json()["complemento"])
    print(content.json()["bairro"])


if __name__ == "__main__":
    __main__()
