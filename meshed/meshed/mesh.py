class Mesh(object):
    def __init__(self):
        self.nodes = {}
        self.values = {}
        self.elements = {}

    def get_nodes(self):
        return self.nodes

    def get_values(self):
        return self.values

    def get_elements(self):
        return self.elements
