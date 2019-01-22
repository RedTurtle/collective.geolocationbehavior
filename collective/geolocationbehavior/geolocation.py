# -*- coding: utf-8 -*-
from collective.geolocationbehavior import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.formwidget.geolocation.field import GeolocationField
from plone.supermodel import model
from zope.interface import provider


@provider(IFormFieldProvider)
class IGeolocatable(model.Schema):
    """Form field for geolocation behavior"""

    geolocation = GeolocationField(
        title=_('label_geolocation', default=u'Coordinate'),
        description=_('help_geolocation',
                      default=u'Click sulla mappa per scegliere una posizione; oppure usare il box di ricerca'),
        required=False)

    model.fieldset(
         'coord',
         label=_(u"Coordinate"),
         fields=['geolocation']
    )
