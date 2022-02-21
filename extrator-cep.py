endereco = "Praça Floriano Peixoto, 303, Centro, Plar, AL, 57150-000"

import re #RegEx

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)