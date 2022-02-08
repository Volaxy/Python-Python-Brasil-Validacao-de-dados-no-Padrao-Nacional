from factory import Factory


def __main__():
    cpf = Factory.create_document("18285399702")

    print(cpf)


if __name__ == "__main__":
    __main__()
