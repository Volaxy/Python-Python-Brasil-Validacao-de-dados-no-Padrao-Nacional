from validate_docbr import CPF


class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)

        if self.cpf_is_valid(cpf):
            self.cpf = cpf
        else:
            raise ValueError("Invalid CPF!")

    def cpf_is_valid(self, cpf):
        if len(cpf) == 11:
            validator = CPF()
            return validator.validate(cpf)

    def __str__(self):
        return self.format_cpf()

    def format_cpf(self):
        mask = CPF()

        return mask.mask(self.cpf)
