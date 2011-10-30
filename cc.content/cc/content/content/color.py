"""Definition of the color content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cc.content.interfaces import Icolor
from cc.content.config import PROJECTNAME

colorSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

colorSchema['title'].storage = atapi.AnnotationStorage()
colorSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(colorSchema, moveDiscussion=False)


class color(base.ATCTContent):
    """Description of the Example Type"""
    implements(Icolor)

    meta_type = "color"
    schema = colorSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(color, PROJECTNAME)
