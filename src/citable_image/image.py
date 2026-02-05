from pydantic import BaseModel
from urn_citation import Cite2Urn

class CitableImage(BaseModel):
    """
    A class representing a citable image with its associated metadata.
    """
    urn: Cite2Urn
    caption: str
    rights: str
    

    def delimited(self, delimiter: str = "|") -> str:
        """
        Returns a delimited string representation of the citable image.

        Args:
            delimiter (str): The delimiter to use between fields. Default is "|".

        Returns:
            str: A delimited string of the citable image's attributes.
        """
        return f"{str(self.urn)}{delimiter}{self.caption}{delimiter}{self.rights}"
    
    
    def delimited(self, delimiter: str = "|") -> str:
        """
        Returns a delimited string representation of the citable image.

        Args:
            delimiter (str): The delimiter to use between fields. Default is "|".

        Returns:
            str: A delimited string of the citable image's attributes.
        """
        return f"{str(self.urn)}{delimiter}{self.caption}{delimiter}{self.rights}"

    @classmethod
    def from_delimited(cls, delimited_string: str, delimiter: str = "|") -> "CitableImage":
        """
        Creates a CitableImage instance from a delimited string.

        Args:
            delimited_string (str): A delimited string containing URN, caption, and rights.
            delimiter (str): The delimiter used between fields. Default is "|".

        Returns:
            CitableImage: A new CitableImage instance.
        """
        parts = delimited_string.split(delimiter)
        if len(parts) != 3:
            raise ValueError(f"Expected 3 parts separated by '{delimiter}', got {len(parts)}")
        
        urn = Cite2Urn.from_string(parts[0])
        caption = parts[1]
        rights = parts[2]
        
        return cls(urn=urn, caption=caption, rights=rights)


def pct_string(u: Cite2Urn, places: int = 3) -> str:    
    """Generate a IIIF percentage region string from a URN subreference.
    """

    if u.subreference():
        roi = u.subreference()
        # Split the subreference by commas to get individual float values
        floats = roi.split(",")
        # Multiply each by 100 and round to the specified number of decimal places
        pct_values = [str(round(float(f) * 100, places)) for f in floats]
        # Join them back with commas
        return "pct:" + ",".join(pct_values)
    else:
        return None
