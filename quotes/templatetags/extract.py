from bson.objectid import ObjectId
from django import template

from ..utils import get_mongo_db
register = template.Library()

def get_authors(id_):
    db = get_mongo_db()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']

register.filter('author', get_authors)