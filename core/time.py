# Importa biblioteca para trabalhar com tempo
import time

# Classe responsável pelo cronômetro
class Timer:

    # Método construtor
    def __init__(self):

        # Indica se o cronômetro está rodando
        self.rodando = False

        # Guarda o tempo inicial
        self.tempo_inicial = 0

        # Guarda o tempo acumulado
        self.tempo_decorrido = 0

    # Método iniciar
    def iniciar(self):

        # Verifica se já não está rodando
        if not self.rodando:

            # Ativa cronômetro
            self.rodando = True

            # Salva horário atual
            self.tempo_inicial = time.time()

    # Método pausar
    def pausar(self):

        # Só pausa se estiver rodando
        if self.rodando:

            # Desativa
            self.rodando = False

            # Soma tempo atual ao acumulado
            self.tempo_decorrido += time.time() - self.tempo_inicial

    # Método resetar
    def resetar(self):

        # Reseta variáveis
        self.rodando = False
        self.tempo_inicial = 0
        self.tempo_decorrido = 0

    # Método para retornar tempo formatado
    def obter_tempo(self):

        # Se estiver rodando
        if self.rodando:

            # Calcula tempo atual
            tempo = (
                time.time()
                - self.tempo_inicial
                + self.tempo_decorrido
            )

        else:

            # Usa apenas acumulado
            tempo = self.tempo_decorrido

        # Converte para minutos
        minutos = int(tempo // 60)

        # Converte para segundos
        segundos = int(tempo % 60)

        # Converte para milissegundos
        milesimos = int((tempo * 100) % 100)

        # Retorna formatado
        return f"{minutos:02}:{segundos:02}:{milesimos:02}"