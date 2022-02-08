from validate_docbr import CPF
# from cpf import Cpf


def __main__():
    cpf = CPF()

    print(cpf.validate("012.345.678-90"))


if __name__ == "__main__":
    __main__()
