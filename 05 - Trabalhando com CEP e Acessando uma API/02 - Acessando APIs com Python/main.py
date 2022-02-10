from find_address import FindAddress
import requests


def __main__():
    cep = FindAddress(84574857)
    print(cep)

    print(cep.access_address())
    # The ".dir()" return all methods of the object
    print(dir(requests))


if __name__ == "__main__":
    __main__()
