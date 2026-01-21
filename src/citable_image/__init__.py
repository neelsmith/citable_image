from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("citable_image") # 'name' of package from pyproject.toml
except PackageNotFoundError:
    # Package is not installed (e.g., running from a local script)
    __version__ = "unknown"

from .service import IIIFService
from .image import CitableImage



__all__ = ["IIIFService", "CitableImage"]