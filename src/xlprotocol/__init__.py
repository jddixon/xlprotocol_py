# xlprotocol/__init__.py

""" Protocol library for python XLattice packages. """

__version__ = '0.0.10'
__version_date__ = '2018-03-06'

__all__ = ['__version__', '__version_date__', 'XLProtocolError', ]


class XLProtocolError(RuntimeError):
    """ General purpose exception for the package. """
    pass
