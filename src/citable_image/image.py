from pydantic import BaseModel
from urn_citation import Cite2Urn

class CitableImage(BaseModel):
    """
    A class representing a citable image with its associated metadata.
    """
    urn: Cite2Urn
    caption: str
    rights: str
    

    