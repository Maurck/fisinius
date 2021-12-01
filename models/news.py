'''
news.py: Modulo para definir el modelo Historia Clinica
'''
from mongoengine import Document, StringField, DateTimeField, IntField, ListField

class News(Document):

    title = StringField(required=True, default='')
    body = StringField(required=True, default='')
    abstract = StringField(required=True, default='')
    uri = StringField(required=True, default='')
    source = StringField(required=True, default='')
    authors_names = ListField(StringField())
    date = DateTimeField(required=True, default=None)
    image_url = StringField(required=True, default='')
    category = StringField(required=True, default='')

    def to_json(self):
        news_dict = {
            "news_id": str(self.pk),
            "title": self.title,
            "body": self.body,
            "abstract": self.abstract,
            "uri": self.uri,
            "source": self.source,
            "authors_names": self.authors_names,
            "date": self.date,
            "image_url": self.image_url,
            "category": self.category
        }
        return news_dict