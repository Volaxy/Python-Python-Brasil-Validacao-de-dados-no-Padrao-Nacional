from cpf import Cpf
from cnpj import Cnpj


# This class will return the class according the length of string passed byt parameter
class Factory:
    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return Cpf(document)
        elif len(document) == 14:
            return Cnpj(document)
