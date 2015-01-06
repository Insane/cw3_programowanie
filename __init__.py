# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Pogoda
                                 A QGIS plugin
 Zadanie na programowanie w GIS
                             -------------------
        begin                : 2015-01-02
        copyright            : (C) 2015 by PB
        email                : insane.m@wp.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Pogoda class from file Pogoda.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Pogoda_PB import Pogoda
    return Pogoda(iface)
