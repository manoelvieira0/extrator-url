endereco = "Praça Floriano Peixoto, 303, Centro, Plar, AL, 57150-000"

import re #RegEx

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)