import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Porcentagem:
    """
    A class vai receber 3 parâmetros, ax, total(quantidade dos dados),
    e a fontsize, que vai ser o tamanho da fonte. E terá duas funções:
    centro -> que vai centralizar a porcentagem no meio das barras
    cima -> que vai centralizar a porcentagem a cima das barras
    """
    def __init__(self, ax, total, fontsize):
        self.ax = ax 
        self.total = total
        self.fontsize = fontsize
    def centro(self):
        for p in self.ax.patches:
            height = p.get_height()
            percent = f'{100 * height / self.total:.1f}%'
            self.ax.annotate(percent,
                (p.get_x() + p.get_width() / 2., height / 2),  # y = meio da barra
                ha='center', va='center', color='white', fontsize=self.fontsize, fontweight='bold')
            
    def cima(self):
        for p in self.ax.patches:
            height = p.get_height()
            percent = f'{100 * height / self.total:.1f}%'
            self.ax.annotate(percent, (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom', fontsize=self.fontsize)
            
class Media:

    def __init__(self, ax, fontsize):
        self.ax = ax 
        self.fontsize = fontsize

    def media(self):
        for p in self.ax.patches:
            self.ax.annotate(f'{p.get_height():.1f}', (p.get_x() + p.get_width() / 2., p.get_height() / 2),
                ha='center', va='center', color='white', fontsize=self.fontsize, fontweight='bold')

class max_min_media:
    def __init__(self, dados, coluna):
        self.coluna = coluna
        self.max = dados[coluna].max()
        self.min = dados[coluna].min()
        self.media = dados[coluna].mean()
    def exibir(self):
        if self.coluna == 'nota_lc':
            text = 'em Linguagens e Códigos'
        elif self.coluna == 'nota_ch':
            text = 'em Ciências Humanas'
        elif self.coluna == 'nota_cn':
            text = 'em Ciências da Natureza'
        elif self.coluna == 'nota_mt':
            text = 'em Matemática e suas tecnologias'
        elif self.coluna == 'nota_redacao':
            text = 'de Redação'
        print(f'Maior nota {text}: {self.max:.2f}\nMenor nota {text}: {self.min:.2f}\nMédia geral {text}: {self.media:.2f}')

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

