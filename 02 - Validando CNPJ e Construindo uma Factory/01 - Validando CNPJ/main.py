from validate_docbr import CNPJ
from cnpj import Cnpj


def __main__():
    cnpj_example = "35379838000112"

    cnpj = Cnpj(cnpj_example)

    print(cnpj)


if __name__ == "__main__":
    __main__()
