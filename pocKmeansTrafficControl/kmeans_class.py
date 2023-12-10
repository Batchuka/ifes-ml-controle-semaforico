import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


class KMeansModel:
    def __init__(self, num_clusters):
        self.num_clusters = num_clusters
        self.kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
        self.ids_semaforos = None


    def preparar_dados_para_kmeans(self, dados):

        # Converte os dados do formato JSON para um DataFrame do pandas
        df = pd.DataFrame(list(dados.values()))

        # Mapeia as categorias de qualidade_via para pesos
        mapa_qld_via = {"residencial": 0.5, "comercial": 1, "industrial": 2}
        df["qld_via"] = df["qld_via"].map(mapa_qld_via)

        # Mapeia as categorias de qualidade_veiculos para pesos
        mapa_qld_porte = {"pequeno": 0.5, "medio": 1, "grande": 2}
        df["qld_porte"] = df["qld_porte"].map(mapa_qld_porte)

        # Aplica pesos às variáveis "qtd_pedestres" e "qtd_veiculos"
        df["qtd_pedestres"] *= df["qld_via"]
        df["qtd_veiculos"] *= df["qld_porte"]

        # Extrai os identificadores dos semáforos
        self.ids_semaforos = df["id_semaforo"]

        # Retorna a matriz numpy dos dados
        return df[["qtd_pedestres", "qtd_veiculos"]].values

    def construir_modelo(self, dados):
        # Prepara os dados para o modelo KMeans
        self.X = self.preparar_dados_para_kmeans(dados)

        # Aplica o KMeans aos dados
        self.kmeans_model.fit(self.X)

    def obter_tempo_de_verde(self, dados_semaforo):
        # Prepara os dados do semáforo para o modelo KMeans
        dados_semaforo = self.preparar_dados_para_kmeans(dados_semaforo)

        # Obtém o rótulo do cluster associado aos dados do semáforo
        cluster = self.kmeans_model.predict(dados_semaforo)

        # Mapeia os rótulos do cluster para os tempos de verde
        mapeamento = {0: 15, 1: 30, 2: 60}

        # Aplica o mapeamento para obter os tempos de verde correspondentes
        tempos_de_verde = [mapeamento[label] for label in cluster]

        # Retorna o tempo de verde fixo associado ao cluster
        return tempos_de_verde
    
    def plotar_resultado_kmeans(self):
        if self.X is None:
            print("Nenhum dado para plotar. Treine o modelo e atualize os dados antes de chamar este método.")
            return

        # Adiciona as colunas do cluster aos dados originais
        labels = self.kmeans_model.predict(self.X)
        dados_com_cluster = pd.DataFrame(self.X, columns=["qtd_pedestres", "qtd_veiculos"])
        dados_com_cluster["cluster"] = labels

        # Define cores específicas para cada cluster
        cores_clusters = {0: 'blue', 1: 'green', 2: 'red'}

        # Plota os dados e os centróides
        scatter = plt.scatter(dados_com_cluster["qtd_pedestres"], dados_com_cluster["qtd_veiculos"], c=dados_com_cluster["cluster"].map(cores_clusters), alpha=0.5)
        plt.scatter(self.kmeans_model.cluster_centers_[:, 0], self.kmeans_model.cluster_centers_[:, 1], c=list(cores_clusters.values()), marker='x', s=200)

        # Adiciona a legenda manualmente
        legend_labels = {0: 30, 1: 15, 2: 60}
        handles = [plt.Line2D([0], [0], marker='o', color='w', label=f"{legend_labels[value]} segundos", markerfacecolor=color, markersize=10) for value, color in cores_clusters.items()]

        # Adiciona a legenda
        plt.legend(handles=handles)

        plt.xlabel("Quantidade de Pedestres")
        plt.ylabel("Quantidade de Veículos")
        plt.title("Resultado do KMeans")
        plt.show()




