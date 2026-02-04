import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self._role_list = []
        self._lista_artisti = []
        self._lista_connessioni = []

        self._nodes = []
        self._edges = []
        self.id_map = {}

        self.get_authorship()

    def get_nodi(self):
        self._lista_artisti = DAO.get_nodi()

    def get_connessioni(self):
        self._lista_connessioni = DAO.get_connessioni()


    def get_authorship(self):
        self._role_list = DAO.get_authorship()
        print(f"Ruoli: {self._role_list}")

    def build_graph(self, role: str):
        self._nodes = []
        self._edges = []
        self.id_map = {}

        self.get_connessioni()
        self.get_nodi()
        for artist in self._lista_artisti:
            self._nodes.append(artist)
            self.id_map[artist.id] = artist
        self.G.add_nodes_from(self._nodes)

        for id1, id2, peso in self._lista_connessioni:
            if id1 in self.id_map and id2 in self.id_map:
                a1 = self.id_map[id1]
                a2 = self.id_map[id2]
                peso = self.calcola_peso(id1, id2)
                self.G.add_edge(a1, a2)





    def calcola_peso(self, id1, id2):
        pass

    def classifica(self):
        pass
