# 📊 Análise dos Microdados do ENEM 2023

Este projeto tem como objetivo realizar o **tratamento** e a **análise exploratória dos dados do ENEM 2023**, com foco em entender o perfil dos participantes e seus desempenhos nas provas. Os dados foram tratados para considerar apenas os candidatos presentes em todas as áreas, garantindo análises mais precisas.

---

## 🗂 Estrutura do Projeto

```plaintext
📁 dados/
│   ├── dados_enem_2023.zip           # Arquivo compactado com o CSV tratado
│   └── MICRODADOS_ENEM_2023.csv      # Arquivo original (ignorado pelo Git).

📁 utils/
│   ├── grafico.py                    # Funções utilitárias para visualização
│   └── utilitarios.py                # Outras funções úteis para reaproveitamento.

📄 analise_enem_2023.ipynb            # Análise dos participantes (sexo, idade, região, etc.).
📄 analise_notas.ipynb                # Análise de desempenho por área da prova.
📄 tratamento_enem.ipynb              # Script de tratamento dos dados.
📄 .gitignore                         # Arquivos/pastas ignoradas pelo Git.
📄 README.md                          # Este arquivo.


---

## 🎯 Objetivo

O foco principal do projeto é analisar quem **realmente compareceu** à prova do ENEM 2023, deixando de lado os alunos ausentes. A partir disso, são feitas:

- Limpeza e tratamento de dados ausentes.
- Criação de gráficos e análises descritivas sobre o perfil dos participantes.
- Análise do desempenho nas áreas de conhecimento e redação.

---

## 🔍 Análises Realizadas

### 📋 `tratamento_enem.ipynb`
- Leitura dos microdados originais.
- Filtragem dos participantes ausentes.
- Seleção de colunas relevantes.
- Exportação dos dados tratados para arquivo `.csv`.

### 📊 `analise_enem_2023.ipynb`
Análises sobre o perfil dos participantes:
- Sexo
- Idade
- Estado e cidade de prova
- Cor/raça
- Nacionalidade
- Tipo de escola
- Treineiros
- Médias por grupo

### 📈 `analise_notas.ipynb`
Análises focadas no desempenho:
- Notas por área (CN, CH, LC, MT, Redação)
- Comparações entre grupos
- Distribuição geral das notas

### 🛠️ `utils/`
Módulos com classes e funções utilizadas em mais de um notebook:
- `grafico.py`: funções de visualização com Matplotlib e Seaborn.
- `utilitarios.py`: funções auxiliares diversas.

---

## 📥 Fonte dos Dados

Os microdados completos do ENEM podem ser baixados no site oficial do INEP:

🔗 [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

> ⚠️ O arquivo `MICRODADOS_ENEM_2023.csv` **não está neste repositório** devido ao seu tamanho. Para reproduzir o projeto completo, baixe diretamente do link acima.

---

## 🚀 Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/LucasArauj99/analise-enem-2023.git

2. Instale as dependências necessárias:

- pip install pandas matplotlib seaborn jupyter

3. Execute os notebooks na ordem:

- tratamento_enem.ipynb

- analise_enem_2023.ipynb

- analise_notas.ipynb

📌 Observações
O projeto é voltado para fins educacionais e exploratórios.

Sugestões de melhorias e contribuições são bem-vindas!

🧑‍💻 Autor
Lucas Araujo
📬 GitHub: LucasArauj99