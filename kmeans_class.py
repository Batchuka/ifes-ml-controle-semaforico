import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder


class KMeansModel:
    def __init__(self, num_clusters):
        self.num_clusters = num_clusters
        self.kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
        self.tempos_de_verde_fixos = [15, 30, 60]
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

    def obter_tempo_de_verde_por_id(self, semaforo_id):
        # Obtém o rótulo do cluster associado ao semáforo
        idx = self.ids_semaforos[self.ids_semaforos == semaforo_id].index[0]
        cluster = self.kmeans_model.predict(self.X[idx].reshape(1, -1))[0]

        # Retorna o tempo de verde fixo associado ao cluster
        return self.tempos_de_verde_fixos[cluster]
    
    def plotar_resultado_kmeans(self):

        if self.X is None:
            print("Nenhum dado para plotar. Treine o modelo e atualize os dados antes de chamar este método.")
            return

        # Adiciona as colunas do cluster aos dados originais
        labels = self.kmeans_model.predict(self.X)
        dados_com_cluster = pd.DataFrame(self.X, columns=["qtd_pedestres", "qtd_veiculos"])
        dados_com_cluster["cluster"] = labels

        # Plota os dados e os centróides
        plt.scatter(dados_com_cluster["qtd_pedestres"], dados_com_cluster["qtd_veiculos"], c=dados_com_cluster["cluster"], cmap='viridis', alpha=0.5)
        plt.scatter(self.kmeans_model.cluster_centers_[:, 0], self.kmeans_model.cluster_centers_[:, 1], c='red', marker='x', s=200)
        plt.xlabel("Quantidade de Pedestres")
        plt.ylabel("Quantidade de Veículos")
        plt.title("Resultado do KMeans")
        plt.show()
