import requests

def recuperar_info_marcas(id_marcas):
    url_completa = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marcas}/modelos'
    headers = {'user-agent':'mystudyApp'}
    resposta = requests.get(url_completa, headers=headers)

    if resposta.status_code != 200:
        print('Error')
        return []

    resposta_info = resposta.json()
    return resposta_info['modelos']


class Lista_fipe():
    def __init__(self, id_marcas):
        self.id_marcas = id_marcas
        self.id_modelos = id_modelos
        self.modelos = []
        self.indice = 0


    def __iter__(self):
        self.modelos = recuperar_info_marcas(self.id_marcas)
        return self

    def __next__(self):
        if self.indice >= len(self.modelos):
            raise StopIteration
        
        else:
            modelo = self.modelos[self.indice]
            self.indice += 1
            return modelo


id_marcas = 21
id_modelos = 5940
lista_fipe = Lista_fipe(id_marcas)

for veiculo in lista_fipe:
    #if veiculo['nome'] == 'Windstar GL':
        print(f"nome: {veiculo['nome']}")
        print(f"id: {veiculo['codigo']}")
