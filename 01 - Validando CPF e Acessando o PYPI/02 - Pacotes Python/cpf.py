class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)

        if self.cpf_is_valid(cpf):
            self.cpf = cpf
        else:
            # The "raise" throw an Exception
            raise ValueError("Invalid CPF!")

    def cpf_is_valid(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False

    def __str__(self):
        return self.format_cpf()

    def format_cpf(self):
        slice_1 = self.cpf[:3]
        slice_2 = self.cpf[3:6]
        slice_3 = self.cpf[6:9]
        slice_4 = self.cpf[9:]

        print(slice_1)
        print(slice_2)
        print(slice_3)
        print(slice_4)

        cpf_formatted = "{}.{}.{}-{}".format(
            slice_1,
            slice_2,
            slice_3,
            slice_4
        )

        return cpf_formatted
