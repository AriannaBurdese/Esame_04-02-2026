from dataclasses import dataclass
@dataclass

class Authorship:
    object_id : int
    role:str
    artist_id:int

    def __str__(self):
        return f"{self.object_id} {self.role} {self.artist_id}"

    def __repr__(self):
        return f"{self.object_id} {self.role} {self.artist_id}"

    def __hash__(self):

        return hash(self.object_id)