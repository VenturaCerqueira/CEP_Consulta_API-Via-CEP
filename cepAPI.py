import requests as Re

# Cosultar CEP

cep = str(input("Digite CEP p/Consulta: "))

if len(cep) != 8:
    print("Quantidade de digitos inválida")
    exit()

# request
request = Re.get("https://viacep.com.br/ws/{}/json/".format(cep))

address_data = request.json()

if 'erro' not in address_data:
    print("CEP encontrada ==>")
    print('CEP: {}'.format(address_data['cep']))
    print('Logradouro: {}'.format(address_data['logradouro']))
    print('Complemento: {}'.format(address_data['complemento']))
    print('Bairro: {}'.format(address_data['bairro']))
    print('Estado: {}'. format(address_data['localidade']))

else:
    print("CEP inválido!")
