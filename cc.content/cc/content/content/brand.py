"""Definition of the brand content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cc.content.interfaces import Ibrand
from cc.content.config import PROJECTNAME

brandSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
	atapi.StringField(
        name='brandName',
        widget=atapi.StringWidget(
            label='Brand name',
            size=20,
            ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

brandSchema['title'].storage = atapi.AnnotationStorage()
brandSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(brandSchema, moveDiscussion=False)


class brand(base.ATCTContent):
    """Description of the Example Type"""
    implements(Ibrand)

    meta_type = "brand"
    schema = brandSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(brand, PROJECTNAME)
