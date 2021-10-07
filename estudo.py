from tkinter import *
janela = Tk()
janela.title("Programa 1")
texto = Label(janela, text='Primeira Interface Gráfica')
texto.grid(column=0, row=0, padx=30, pady=30)

botao = Button(janela, text='Olá Mundo')
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text='')
texto_resposta.grid(column=0, row=2, padx=10, pady=10)




janela.mainloop()