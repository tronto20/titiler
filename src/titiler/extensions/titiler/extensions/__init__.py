"""titiler.extensions"""

__version__ = "0.14.0"

from .cogeo import cogValidateExtension  # noqa
from .stac import stacExtension  # noqa
from .viewer import cogViewerExtension, stacViewerExtension  # noqa
from .wms import wmsExtension  # noqa
from .cloud import cloudCredentialsExtension
from .wmts import wmtsTitleExtension
