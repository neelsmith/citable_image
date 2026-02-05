from ntpath import join
from pydantic import BaseModel
from urn_citation import Cite2Urn
from citable_image.image import pct_string
from io import BytesIO
import requests
from PIL import Image


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


def iiif_url(urn: Cite2Urn, service: IIIFService, w: int=2000, extension: str = "tif"):
    """Generate IIIF image request URL and file path from URN citation.
    
    Args:
        urn (Cite2Urn): URN citation of the image.
        service (IIIFService): IIIF image service configuration.
    Returns:
        a URL
    """
   
    subdir = urn.namespace + "/" + urn.collection + "/" + urn.version


    if urn.subreference() is not None:
        pct = pct_string(urn)
        return service.baseurl + "?IIIF=" + service.pathroot + "/" + subdir + "/" + urn.drop_subreference().object_id +  f".{extension}/{pct}/{w},/0/default.jpg" 
    
    else:
        return service.baseurl + "?IIIF=" + service.pathroot + "/" + subdir + "/" + urn.drop_subreference().object_id +  f".{extension}/full/{w},/0/default.jpg" 
        
    #
    # service.baseurl * "?IIIF=" * service.directoryroot * "/" * subdirectory(img) * "/" * objectcomponent(dropsubref(img)) * ".$(extension)/$(pct)/$(w),/0/default.jpg"   
    # or
    #    service.baseurl * "?IIIF=" * service.directoryroot * "/" * subdirectory(img) * "/" * objectcomponent(dropsubref(img)) * ".$(extension)/full/$(w),/0/default.jpg" 



def iiif_image(urn: Cite2Urn, service: IIIFService, w: int=2000, extension: str = "tif"):
    url = iiif_url(urn, service, w, extension)
    img = Image.open(BytesIO(requests.get(url).content))
    return img

