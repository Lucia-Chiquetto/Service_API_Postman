import requests
from time import sleep
from pymongo import MongoClient
import json
import csv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Configuração do MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['cep_service']
collection = db['consultas']

# Inicializar FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Consulta de CEPs!"}

# Modelo de Dados para Validação
class CEPModel(BaseModel):
    cep: str
    logradouro: str
    complemento: str
    bairro: str
    localidade: str
    uf: str

@app.post("/create/", status_code=201)
def create_cep(data: CEPModel):
    """Cria um novo registro de CEP no MongoDB."""
    if collection.find_one({"cep": data.cep}):
        raise HTTPException(status_code=400, detail="CEP já existe no banco de dados.")
    collection.insert_one(data.dict())
    return {"message": "CEP criado com sucesso!", "data": data}

@app.get("/read/", response_model=List[CEPModel])
def read_ceps():
    """Retorna todos os registros de CEP armazenados."""
    registros = list(collection.find({}, {"_id": 0}))
    if not registros:
        raise HTTPException(status_code=404, detail="Nenhum registro encontrado.")
    return registros

@app.put("/update/{cep}/", status_code=200)
def update_cep(cep: str, data: CEPModel):
    """Atualiza os dados de um CEP específico."""
    if not collection.find_one({"cep": cep}):
        raise HTTPException(status_code=404, detail="CEP não encontrado.")
    collection.update_one({"cep": cep}, {"$set": data.dict()})
    return {"message": "CEP atualizado com sucesso!"}

@app.delete("/delete/{cep}/", status_code=200)
def delete_cep(cep: str):
    """Deleta um registro de CEP específico."""
    result = collection.delete_one({"cep": cep})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="CEP não encontrado.")
    return {"message": "CEP deletado com sucesso!"}

def salvar_no_mongo(cep_data):
    """Salva os dados no MongoDB."""
    if collection.find_one({"cep": cep_data["cep"]}):
        print("\033[33mO CEP já existe no banco de dados.\033[m")
    else:
        collection.insert_one(cep_data)
        print("\033[32mDados salvos no MongoDB com sucesso!\033[m")

def exportar_json():
    """Exporta os dados do MongoDB para um arquivo JSON."""
    dados = list(collection.find({}, {"_id": 0}))
    with open("consultas.json", "w") as f:
        json.dump(dados, f, indent=4)
    print("\033[32mDados exportados para consultas.json\033[m")

def exportar_csv():
    """Exporta os dados do MongoDB para um arquivo CSV."""
    dados = list(collection.find({}, {"_id": 0}))
    if dados:
        with open("consultas.csv", "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=dados[0].keys())
            writer.writeheader()
            writer.writerows(dados)
        print("\033[32mDados exportados para consultas.csv\033[m")
    else:
        print("\033[31mNenhum dado disponível para exportação.\033[m")

def main():
    print('=' * 42)
    print(f'          \033[46mConsulta CEP - ViaCEP\033[m')
    print('=' * 42)

    sigla_estado = ''
    while not sigla_estado.isalpha() or len(sigla_estado) != 2:
        sigla_estado = input("\033[36mInforme a sigla do estado (ex: SP): \033[m").upper()
        if not sigla_estado.isalpha() or len(sigla_estado) != 2:
            print("\033[31mSigla do estado inválida.\033[m")

    cep_option = ''
    while not cep_option.isdecimal() or not len(cep_option) == 8:
        cep_option = input('\033[36mInforme o CEP a ser consultado (8 dígitos): \033[m ')
        if not cep_option.isdecimal() or len(cep_option) != 8:
            print(f'\033[31mO CEP informado ({cep_option}) é inválido!\033[m')

    consumo_api = requests.get(f'https://viacep.com.br/ws/{cep_option}/json/')
    if consumo_api.status_code == 200:
        try:
            cep_data = consumo_api.json()
            print('=' * 42)
            if 'erro' not in cep_data.keys():
                print(f'\033[46mCEP consultado:\033[m \033[36m{cep_data["cep"]}\033[m')
                print(f'\033[43mEndereço:\033[m \033[33m{cep_data["logradouro"]} {cep_data["complemento"]}\033[m')
                print(f'\033[42mLocalidade/UF:\033[m \033[32m{cep_data["localidade"]}-{cep_data["uf"]}\033[m')
                salvar_no_mongo(cep_data)
            else:
                print(f'\033[31mCEP {cep_option} inválido!\033[m')
        except json.JSONDecodeError:
            print("\033[31mErro ao decodificar a resposta da API.\033[m")
    else:
        print(f"\033[31mErro na consulta à API: {consumo_api.status_code}.\033[m")

    print("\033[36mOpções disponíveis:\033[m")
    print("1. Consultar outro CEP")
    print("2. Exportar dados para JSON")
    print("3. Exportar dados para CSV")
    print("4. Sair")
    user_option = input("Escolha uma opção: ")

    if user_option == '1':
        main()
    elif user_option == '2':
        exportar_json()
        main()
    elif user_option == '3':
        exportar_csv()
        main()
    elif user_option == '4':
        print('\033[31mEncerrando o programa\033[m', end='')
        for c in range(3):
            sleep(0.5)
            print('\033[31m.\033[m', end='')
        print()
    else:
        print("\033[31mOpção inválida. Encerrando o programa.\033[m")

if __name__ == '__main__':
    main()
