from pydantic import BaseModel
from urn_citation import Cite2Urn


# Test with these values:
# baseurl = "http://www.homermultitext.org/iipsrv"
#root = "/project/homer/pyramidal/deepzoom"




class IIIFService(BaseModel):
    """A IIIF image service mirroring URN citation in its file layout.
    
    Attributes:
        baseurl (str): base URL of the IIIF image service.
        pathroot (str): root path for the image files.
    """
    baseurl: str
    pathroot: str
