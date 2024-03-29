"""Definition of the job content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cc.content.interfaces import Ijob
from cc.content.config import PROJECTNAME

jobSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

jobSchema['title'].storage = atapi.AnnotationStorage()
jobSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(jobSchema, moveDiscussion=False)


class job(base.ATCTContent):
    """Description of the Example Type"""
    implements(Ijob)

    meta_type = "job"
    schema = jobSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(job, PROJECTNAME)
