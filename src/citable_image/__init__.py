from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("citable_image") # 'name' of package from pyproject.toml
except PackageNotFoundError:
    # Package is not installed (e.g., running from a local script)
    __version__ = "unknown"

from .service import IIIFService



__all__ = ["IIIFService"]