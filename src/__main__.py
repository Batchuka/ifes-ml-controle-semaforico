import time
from semaforo_class import Semaforos
from kmeans_class import KMeansModel

# Cria instâncias das classes Semaforos e KMeansModel
semaforos = Semaforos()
modelo_kmeans = KMeansModel(num_clusters=3)

while True:

    # Varia os dados de quantidade de pedestres e veículos antes de criar o modelo
    for semaforo in semaforos.lista_semaforos:
        semaforo.variar_dados_tempo()

    # Gera dados fictícios e os envia para a classe Semaforos
    dados = semaforos.gerar_dados()

    # Atualiza o modelo KMeans com os dados
    modelo_kmeans.construir_modelo(dados)

    # Varia os dados de quantidade de pedestres e veículos antes para classificação
    for semaforo in semaforos.lista_semaforos:
        semaforo.variar_dados_tempo()

    # Gera dados fictícios e os envia para a classe Semaforos
    dados = semaforos.gerar_dados()

    # Obtém os novos tempos de verde para cada semáforo com base no modelo treinado
    novos_tempos_de_verde = modelo_kmeans.obter_tempo_de_verde(dados)

    # Atualiza os tempos de verde dos semáforos com os novos tempos
    semaforos.atualizar_tempos_de_verde(novos_tempos_de_verde)

    # Imprime os resultados ou realiza outras ações necessárias
    print("Modelo Atualizado")
    print("Novos Tempos de Verde:", novos_tempos_de_verde)

    # Aguarda algum tempo antes de gerar e enviar novos dados (simula a passagem do tempo)
    time.sleep(5)  # Aguarda 5 segundos

    modelo_kmeans.plotar_resultado_kmeans()