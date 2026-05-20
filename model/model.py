from database.DAO import DAO

class Model:
    def __init__(self):
        pass
    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def buildGraph(self, genere):
        nodes = DAO.getAllNodes(genere)
        self._graph.add_nodes_from(nodes)