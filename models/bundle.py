from models.composite import Composite

class Bundle(Composite):
    def __init__(self, id: int, nom: str, description: str, prix: float, nb_ventes: int, image_url: str, rabais: float = 0.0):
        super().__init__(id, nom, description, prix, nb_ventes, image_url)
        self.rabais = rabais

    def prix_total(self) -> float:
        return super().prix_total() * (1 - self.rabais)