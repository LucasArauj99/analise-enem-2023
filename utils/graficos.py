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