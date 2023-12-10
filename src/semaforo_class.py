import random

class Semaforo:

    def __init__(self, semaforo_id):
        self.semaforo_id = semaforo_id
        self.dados = {
            "id_semaforo": f"{semaforo_id}",
            "qld_via": random.choice(["residencial", "comercial", "industrial"]),
            "qld_porte": random.choice(["pequeno", "medio", "grande"]),
            "qtd_pedestres": random.randint(0, 20),
            "qtd_veiculos": random.randint(0, 30),
            "tempo_verde": 30,
        }

    def obter_json(self):
        return {self.semaforo_id: self.dados}

    def variar_dados_tempo(self):
        # Adiciona uma pequena variação aos dados de quantidade de pedestres e veículos
        self.dados["qtq_pedestres"] = max(0, self.dados["qtd_pedestres"] + random.randint(-2, 2))
        self.dados["qtd_veiculos"] = max(0, self.dados["qtd_veiculos"] + random.randint(-5, 5))

class Semaforos:

    def __init__(self):
        self.lista_semaforos = [Semaforo(i) for i in range(1, 51)]

    def gerar_dados(self):
        dados = {}
        for semaforo in self.lista_semaforos:
            dados.update(semaforo.obter_json())
        return dados

    def atualizar_tempos_de_verde(self, novos_tempos_verde):

        # Certifique-se de que o comprimento da lista de novos tempos de verde seja igual ao número de semáforos
        if len(novos_tempos_verde) != len(self.lista_semaforos):
            raise ValueError("O número de novos tempos de verde não corresponde ao número de semáforos")

        # Atualiza os tempos de verde para cada semáforo
        for semaforo, novo_tempo_verde in zip(self.lista_semaforos, novos_tempos_verde):
            semaforo.dados["tempo_verde"] = novo_tempo_verde
