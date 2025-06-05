from scipy.spatial.distance import cosine

class LogicMap:
    def __init__(self):
        self.vector_to_symbol = {}
        self.symbol_to_vector = {}

    def add_mapping(self, vector, symbol):
        self.vector_to_symbol[tuple(vector)] = symbol
        self.symbol_to_vector[symbol] = vector

    def get_symbol(self, vector, threshold=0.9):
        for ref_vector, symbol in self.vector_to_symbol.items():
            similarity = 1 - cosine(vector, ref_vector)
            if similarity > threshold:
                return symbol
        return None
