"""
SunPy's custom representation classes.
Part of the proposed Coordinates API.
@author: Pritish C. (VaticanCameos)
"""

# Astropy
from astropy.utils.compat.odict import OrderedDict
from astropy import units as u
from astropy.coordinates.representation import SphericalRepresentation
from astropy.coordinates import Longitude, Latitude

__all__ = ['Longitude180', 'SphericalWrap180Representation']

class Longitude180(Longitude):
    def __new__(cls, angle, unit=None, wrap_angle=180*u.deg, **kwargs):
        self = super(Longitude180, cls).__new__(cls, angle, unit=unit,
                                                wrap_angle=wrap_angle, **kwargs)
        return self

class SphericalWrap180Representation(SphericalRepresentation):
    """
    Representation of points in 3D Spherical coordinates.
    This representation allows for a negative Longitude.
    It does so by setting wrap_angle=180 degrees.

    Parameters
    ----------
    lon, lat: `~astropy.units.Quantity`
        The longitude and latitude of the point(s) in angular units. The
        latitude should be between -90 and +90 degrees, and the longitude
        is allowed to have any value between -180 to 180 degrees. These
        can also be instances of `~astropy.units.Angle`,
        `~astropy.coordinates.Longitude`, or `~astropy.coordinates.Latitude`.

    distance: `~astropy.units.Quantity`
        The distance to the point(s). If the distance is a length, it is
        passed to the :class:`~astropy.coordinates.Distance` class, else
        it is passed to the :class:`~astropy.units.Quantity` class.

    copy: bool, optional
        If True, arrays will be copied rather than referenced.
    """

    attr_classes = OrderedDict([('lon', Longitude180),
                                ('lat', Latitude),
                                ('distance', u.Quantity)])
    recommended_units = {'lon': u.deg, 'lat': u.deg}
