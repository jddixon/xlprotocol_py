# xlprotocol/__init__.py

""" Protocol library for python XLattice packages. """

__version__ = '0.0.3'
__version_date__ = '2017-02-24'

__all__ = ['__version__', '__version_date__', 'XLProtocolError', ]


class XLProtocolError(RuntimeError):
    """ General purpose exception for the package. """
