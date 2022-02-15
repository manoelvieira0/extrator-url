# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

url = " "

#Sanitização da Url
url = url.strip()

#validação da Url
if url == "":
    raise ValueError("A Url está vazia!")

#Separa base e os parêmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:] #Até o final da String
print(url_parametros)

#Busca o valor de um parâmetro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)