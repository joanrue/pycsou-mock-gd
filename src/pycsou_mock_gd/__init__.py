try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
from .opt import GradientDescent

__all__ = ("GradientDescent",)
