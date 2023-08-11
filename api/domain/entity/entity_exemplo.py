import mongoengine
from mongoengine import Document, EmbeddedDocument


class AnotherEntity(EmbeddedDocument):
    name = mongoengine.StringField(requerid=True)


class Entity(Document):
    name = mongoengine.StringField(required=True)
    another_entities = mongoengine.EmbeddedDocumentListField(AnotherEntity, required=False)
