import tkinter as tk
from tkinter import filedialog 
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

def criar_grafico():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        # Ler os dados do arquivo e armazená-los em listas
        with open(arquivo, 'r') as file: #abri
            linhas = file.readlines()
            #info do grafico
            
    labels = ['FIFA 23','POKÉMON LEGENDS: ARCEUS','NINTENDO SWITCH SPORTS','MARIO KART 8 DELUXE','GOD OF WAR RAGNAROK','GTA 5','MINECRAFT','JUSTDANCE23']
    valores = [46,31,24,19,14,12,10,7]
    bar_colors = ['blue', 'red', 'orange','green','yellow','purple','black','pink']

    for linha in linhas:
            partes = linha.strip().split(',') #searador de texto splt, strip tira espaco
            if len(partes) == 3:
                label, valor, cor = partes
                labels.append(label)
                valores.append(float(valor))
                bar_colors.append(cor)
                
      # Criar o garfico.
    plt.figure(figsize=(8, 6))
    plt.bar(labels, valores, color=bar_colors)
    plt.xlabel('MEDIA FEITA SEGUNDO AS LOJAS FNAC PORTUGAL')
    plt.ylabel('QUANTIDADE VENDIDA ATE O MÊS ATUAL')
    plt.title('JOGOS MAS VENDIDO EM 2023')
    plt.xticks(rotation=50)

        # Mostrar o gráfico
    plt.tight_layout()
    plt.show()  
    

root = tk.Tk()
root.title('JOGOS MAS VENDIDO EM PORTUGAL')

imagem = Image.open('EXEAVALIACAO/fotojogo.png')
imagem = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(root, image=imagem)
label_imagem.pack()

botao = tk.Button(root, text='Criar Gráfico', command=criar_grafico)
botao.pack(pady=50)

root.mainloop()              