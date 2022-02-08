from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, cnpj):
        cnpj = str(cnpj)

        if self.cnpj_is_valid(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("Invalid CPF!")

    def cnpj_is_valid(self, cnpj):
        validator = CNPJ()

        return validator.validate(cnpj)
