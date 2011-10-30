"""Definition of the service content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from Products.Archetypes.SQLStorage import MySQLSQLStorage
# -*- Message Factory Imported Here -*-

from cc.content.interfaces import Iservice
from cc.content.config import PROJECTNAME

serviceSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        name='serviceType',
        vocabulary = ['oil', 'oilGear', 'oilRearGear', 'oilBrake', 'oilFilter', 'coating', 'surface'],
        widget=atapi.SelectionWidget(
            label='Service type',
            ),
        storage=MySQLSQLStorage()
    ),
	atapi.StringField(
        name='serviceNumber',
        widget=atapi.StringWidget(
            label='Service number',
            size=20,
            ),
        storage=MySQLSQLStorage()
    ),
	atapi.StringField(
        name='servicePrice',
        widget=atapi.StringWidget(
            label='Service price',
            size=20,
            ),
        storage=MySQLSQLStorage()
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

serviceSchema['title'].storage = atapi.AnnotationStorage()
serviceSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(serviceSchema, moveDiscussion=False)


class service(base.ATCTContent):
    """Description of the Example Type"""
    implements(Iservice)

    meta_type = "service"
    schema = serviceSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(service, PROJECTNAME)
