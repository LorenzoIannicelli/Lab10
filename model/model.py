from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._dizionario_hub = {}
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self._nodes = DAO.read_all_hub()

        for hub in self._nodes:
            self._dizionario_hub[hub.id] = hub

        self.G.add_nodes_from(self._nodes)
        print('nodi aggiunti')

        self.get_all_edges(threshold)

        for edge in self._edges:
            self.G.add_edge(self._dizionario_hub[edge.origine],
                            self._dizionario_hub[edge.destinazione],
                            weight=edge.avg_valore_merce)
        print('archi aggiunti')

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return len(self._edges)

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return len(self._nodes)

    def get_all_edges(self, threshold):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        self._edges = DAO.read_all_spedizioni(threshold)

