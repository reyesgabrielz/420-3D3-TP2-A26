from models.composant import Composant
from abc import ABC, abstractmethod

class Composite(Composant, ABC):
     def __init__(self, id: int, nom: str, description: str, prix: float, nb_ventes: int, image_url: str):
          super().__init__(id, nom, description, prix, nb_ventes, image_url)
          self.enfants: list[Composant] = []

     def prix_total(self) -> float:
        return sum(enfant.prix_total() for enfant in self.enfants)

     def nb_items(self) -> int:
         return sum(enfant.nb_items() for enfant in self.enfants)

     def est_bundle(self) -> bool:
         return True

     def ajouter(self, enfant: Composant) -> None:
         self.enfants.append(enfant)

 
