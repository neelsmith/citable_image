from pydantic import BaseModel


class IIIFService(BaseModel):
    baseurl: str
    pathroot: str
