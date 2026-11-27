from models.composant import Composant
from abc import ABC 

class Feuille(Composant, ABC):
    
    def prix_total(self) -> float:
            return self.prix

    def est_bundle(self) -> bool:
        return False 

    def nb_items(self) -> int:
            return 1