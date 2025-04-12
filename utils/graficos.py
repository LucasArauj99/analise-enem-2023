import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class graficos_notas:

    def __init__(self, dados, materia, titulo):
        self.dados = dados 
        self.materia = materia
        self.titulo = titulo

    def plot(self):
        plt.figure(figsize=(10, 6))
        sns.set(style="whitegrid")

        sns.histplot(
        data=self.dados,
        x=self.materia,
        kde=True,
        bins=30,
        color="#4C72B0",        # azul suave
        edgecolor='white'
        )

        plt.title(self.titulo, fontsize=16, weight='bold')
        plt.xlabel('Nota', fontsize=12)
        plt.ylabel('Quantidade de Participantes', fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.show()

       
class GraficoNotasCategoria:
    def __init__(self, dados, faixa_etaria, disciplina, titulo):
        self.dados = dados
        self.faixa_etaria = faixa_etaria
        self.disciplina = disciplina
        self.titulo = titulo

    def gerar_graficos(self):
        categorias = [
            ('sexo', 'Sexo'),
            ('cor_raca_label', 'Cor e Raça'),
            ('tp_escola', 'Escola'),
            ('in_treineiro', 'Treineiro'),
            ('faixa_idade', 'Idade'),
            ('uf_prova', 'Estado')
        ]

        # Gráficos lado a lado (primeiras 4 categorias)
        plt.figure(figsize=(18, 8))
        for i, (coluna, nome_coluna) in enumerate(categorias[:4]):
            plt.subplot(2, 2, i+1)
            agrupado = self.dados.groupby(coluna, observed=True)[self.disciplina].mean().reset_index()
            sns.barplot(data=agrupado, x=coluna, y=self.disciplina, hue=coluna, palette='cividis', edgecolor='black', legend=False)
            plt.title(f'Nota de {self.titulo} por {nome_coluna}')
            plt.xlabel('')
            plt.ylabel(f'Nota de {self.titulo}')
        plt.tight_layout()
        plt.show()

        # Reorganiza faixa etária
        self.dados['faixa_idade'] = pd.Categorical(self.dados['faixa_idade'], categories=self.faixa_etaria.values(), ordered=True)

        # Gráficos individuais para Idade e Estado
        for coluna, nome_coluna in categorias[4:]:
            plt.figure(figsize=(14, 6))
            agrupado = self.dados.groupby(coluna, observed=True)[self.disciplina].mean().reset_index()
            if coluna == 'faixa_idade':
                agrupado = agrupado.sort_values(by='faixa_idade')
            sns.barplot(data=agrupado, x=coluna, y=self.disciplina, hue=coluna, palette='cividis', edgecolor='black')
            plt.title(f'Nota de {self.titulo} por {nome_coluna}')
            plt.xlabel('')
            plt.ylabel(f'Nota de {self.titulo}')
            plt.xticks(rotation=45 if coluna in ['faixa_idade', 'uf_prova'] else 0)
            plt.tight_layout()
            plt.show()

