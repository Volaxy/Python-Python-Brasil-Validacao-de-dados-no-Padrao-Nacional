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

    def __str__(self):
        return self.format_cnpj(self.cnpj)

    def format_cnpj(self, cnpj):
        mask = CNPJ()

        # This method ".mask()" generate a formataded CNPJ, Ex.: "35.379.838/0001-12"
        return mask.mask(cnpj)
