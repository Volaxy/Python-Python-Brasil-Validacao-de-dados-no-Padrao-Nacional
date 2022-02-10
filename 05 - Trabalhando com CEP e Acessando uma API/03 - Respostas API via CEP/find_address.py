import requests


class FindAddress:
    def __init__(self, cep):
        cep = str(cep)

        if self.cep_is_valid(cep):
            self.cep = cep
        else:
            raise ValueError("Incorrect cep!")

    def cep_is_valid(self, cep):
        return True if len(cep) == 8 else False

    def __str__(self):
        return self.formated_cep()

    def formated_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def access_address(self):
        return requests.get("https://viacep.com.br/ws/01001000/json/")
