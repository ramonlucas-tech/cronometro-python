# Biblioteca gráfica
import tkinter as tk

# Importa Timer
from core.time import Timer

# Classe da janela
class Janela:

    # Método construtor
    def __init__(self):

        # Cria cronômetro
        self.timer = Timer()

        # Cria janela principal
        self.janela = tk.Tk()

        # Título da janela
        self.janela.title("Cronômetro Python")

        # Tamanho
        self.janela.geometry("350x220")

        # Impede redimensionamento
        self.janela.resizable(False, False)

        # Mantém janela acima
        self.janela.attributes("-topmost", True)

        # Texto do cronômetro
        self.label = tk.Label(
            self.janela,
            text="00:00:00",
            font=("Arial", 40)
        )

        # Espaçamento
        self.label.pack(pady=30)

        # Frame dos botões
        frame = tk.Frame(self.janela)
        frame.pack()

        # Botão iniciar
        self.btn_iniciar = tk.Button(
            frame,
            text="Iniciar",
            width=10,
            command=self.iniciar
        )

        self.btn_iniciar.grid(row=0, column=0, padx=5)

        # Botão pausar
        self.btn_pausar = tk.Button(
            frame,
            text="Pausar",
            width=10,
            command=self.pausar
        )

        self.btn_pausar.grid(row=0, column=1, padx=5)

        # Botão resetar
        self.btn_resetar = tk.Button(
            frame,
            text="Resetar",
            width=10,
            command=self.resetar
        )

        self.btn_resetar.grid(row=0, column=2, padx=5)

        # Atualiza interface
        self.atualizar()

    # Atualiza cronômetro na tela
    def atualizar(self):

        # Atualiza texto
        self.label.config(
            text=self.timer.obter_tempo()
        )

        # Atualiza a cada 10ms
        self.janela.after(10, self.atualizar)

    # Iniciar cronômetro
    def iniciar(self):
        self.timer.iniciar()

    # Pausar cronômetro
    def pausar(self):
        self.timer.pausar()

    # Resetar cronômetro
    def resetar(self):
        self.timer.resetar()

    # Executar aplicação
    def executar(self):
        self.janela.mainloop()