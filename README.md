# 📊 CSV Filter & Splitter

Projeto desenvolvido em **Python** para facilitar a leitura, filtragem e divisão de arquivos CSV.

A aplicação permite que o usuário navegue pelas pastas do diretório, selecione um arquivo CSV, escolha uma coluna para filtragem e selecione um ou mais valores dessa coluna. A partir dessas escolhas, o programa gera automaticamente novos arquivos CSV separados em uma pasta definida pelo usuário.

O projeto foi desenvolvido como forma de colocar em prática conceitos de **Python, Pandas, manipulação de arquivos, tratamento de entradas e organização de código em módulos**.

---

## 🚀 Funcionalidades

- 📁 Listagem das pastas disponíveis no diretório do projeto
- 📄 Seleção de arquivos `.csv`
- 📊 Leitura de dados utilizando **Pandas**
- 🧹 Remoção de espaços desnecessários nos nomes das colunas
- 🔎 Seleção da coluna utilizada como filtro
- 📋 Listagem dos valores únicos e não nulos da coluna selecionada
- ☑️ Seleção de um ou vários valores para filtragem
- 🔄 Remoção de valores duplicados selecionados
- 📂 Criação automática do diretório de saída
- 💾 Geração de novos arquivos CSV de acordo com os filtros escolhidos

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Pandas**
- **OS / os.path**

### Conceitos praticados

- Funções e modularização
- Estruturas condicionais
- Estruturas de repetição
- Tratamento de exceções
- List comprehensions
- Manipulação de strings
- Manipulação de listas
- Manipulação de arquivos e diretórios
- Leitura e escrita de arquivos CSV
- Filtragem de DataFrames
- Tratamento de valores nulos
- Valores únicos com `unique()`
- Criação de diretórios com `os.makedirs()`

---

## 📂 Estrutura do projeto

```text
CSV-Filter-Splitter/
│
├── main.py
├── caminhos.py
├── opcaoColunas.py
├── opcaoItens.py
│
├── entrada/
│   └── Arquivos CSV
│
├── resultados/
│   └── Arquivos CSV processados
│
└── README.md
