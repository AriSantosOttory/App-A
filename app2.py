import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import os

def criar_grafico():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        # Ler os dados do arquivo e armazená-los em listas
        with open(arquivo, 'r') as file:
            linhas = file.readlines()

        labels = ['FIFA 23','POKÉMON LEGENDS:ARCEUS','NINTENDO SWITCH SPORTS','MARIO KART 8 DELUXE','GOD OF WAR RAGNAROK','GTA 5','MINECRAFT','JUSTDANCE23']
        valores = [46,31,24,19,14,12,10,7]
        bar_colors = ['blue', 'red', 'orange','green','yellow','purple','black','pink']

        for linha in linhas:
            partes = linha.strip().split(',')
            if len(partes) == 2:
                label, valor, cor = partes
                labels.append(label)
                valores.append(float(valor))
                bar_colors.append(cor)

        
        plt.figure(figsize=(8, 6))
        plt.bar(labels, valores, color=bar_colors)
        plt.xlabel('MEDIA FEITA SEGUNDO AS LOJAS FNAC PORTUGAL')
        plt.ylabel('QUANTIDADE VENDIDA ATE O MÊS ATUAL')
        plt.title('JOGOS MAIS VENDIDOS EM 2023')
        plt.xticks(rotation=50)
        
    # for i, v in enumerate(valores):
    #   plt.text(i, v, str(v), ha='center', va='bottom')

        # Salvar o gráfico como imagem na pasta de execução função matplotlib
    nomearquivo = 'graficojogo.png'
    caminhoarquivo = os.path.join(os.getcwd(), nomearquivo)
    plt.savefig(caminhoarquivo)

    plt.tight_layout()
    plt.show()
        

def main():
    root = tk.Tk()
    root.title('JOGOS MAIS VENDIDOS EM PORTUGAL')

    imagem = Image.open('EXEAVALIACAO/fotojogo.png')
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = tk.Label(root, image=imagem)
    label_imagem.pack()

    botao = tk.Button(root, text='Criar Gráfico', command=criar_grafico)
    botao.pack(pady=50)

    root.mainloop()

if __name__ == "__main__": #dois scripts, um e executado dentro do principal
    main()
#determinar se um script está sendo executado como um programa principal 
# (ou seja, diretamente por mim o  usuário) ou se está sendo importado como um módulo em outro script.