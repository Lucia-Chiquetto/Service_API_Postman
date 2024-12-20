# Consulta de CEPs - API FastAPI
Este projeto foi desenvolvido para oferecer um serviço completo de consulta, gerenciamento e exportação de CEPs, utilizando Python, FastAPI e MongoDB.

## Objetivo
Desenvolver um sistema que:

- **Consulta CEPs**: Permita buscar CEPs usando a API ViaCEP.
- **Armazenamento**: Salve os resultados das consultas em um banco de dados MongoDB.
- **Exportação**: Ofereça a opção de exportar os dados em formato JSON ou CSV.
- **Operações CRUD**: Implemente as operações CRUD (Create, Read, Update e Delete) para gerenciar os dados armazenados.

## Funcionalidades

1. **Consulta de CEPs**
   - Permite buscar CEPs informando o Estado e o CEP específico.
   - Faz uso da API ViaCEP para obter os dados.
   - Inclui validação para garantir integridade e lidar com erros.

2. **Armazenamento no MongoDB**
   - Dados de consultas são salvos no MongoDB.
   - Evita duplicação ao verificar registros antes do salvamento.

3. **Exportação de Dados**
   - Dados armazenados podem ser exportados em:
     - **JSON**: Estruturado para uso em integrações ou APIs.
     - **CSV**: Para análise de dados ou manipulação em planilhas.

4. **Operações CRUD**
   - **Create**: Permite criar um registro de CEP manualmente.
   - **Read**: Lista todos os CEPs armazenados.
   - **Update**: Atualiza dados de um CEP específico.
   - **Delete**: Remove registros indesejados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para construção de APIs.
- **MongoDB**: Banco de dados NoSQL para armazenamento.
- **ViaCEP API**: Serviço para consulta de CEPs.
- **Postman**: Tecnologia para validação e testes dos endpoints. 

### Bibliotecas Adicionais

- **pymongo**: Conexão com MongoDB.
- **csv, json**: Manipulação e exportação de dados.
- **requests**: Consumo de APIs externas.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/consulta-cep.git
cd consulta-cep
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o MongoDB:

Certifique-se de que o MongoDB está instalado e rodando na porta padrão.

Inicie o serviço:

```bash
python consulta_cep.py
```

## Uso

### Endpoints da API

- **POST /create/**: Cria um novo registro de CEP.
- **GET /read/**: Lista todos os registros de CEP.
- **PUT /update/{cep}/**: Atualiza os dados de um CEP específico.
- **DELETE /delete/{cep}/**: Remove um registro de CEP.

### Scripts Disponíveis

- **Exportar JSON**:
  ```bash
  python consulta_cep.py --export json
  ```

- **Exportar CSV**:
  ```bash
  python consulta_cep.py --export csv
  ```

## Arquivos no Repositório

- `consulta_cep.py`: Script principal com implementação do serviço.
- `consultas.json`: Exemplo de exportação em formato JSON.
- `consultas.csv`: Exemplo de exportação em formato CSV.

