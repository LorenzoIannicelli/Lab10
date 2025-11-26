from dataclasses import dataclass


@dataclass
class Arco:
    origine : int
    destinazione : int
    avg_valore_merce : float

    def __str__(self):
        return f"Arco: {self.origine} {self.destinazione} {self.avg_valore_merce}"

    def __hash__(self):
        return hash(self.origine)