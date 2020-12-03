from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect


db = SQLAlchemy()

class Serializer(object):
    """Class for serializing SQLAlchemy objects into dicts."""

    @staticmethod
    def is_primitive(obj):
        return type(obj) in (int, float, str, bool)

    def serialize(self):
        fields = inspect(self).attrs.keys()
        return {c: getattr(self, c) for c in fields if Serializer.is_primitive(getattr(self, c))}

    @staticmethod
    def serialize_list(list_obj):
        return [m.serialize() for m in list_obj]

class Job(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, nullable=False)
    title = db.Column(db.String)
    normalized_title = db.Column(db.String)
    parent_uuid = db.Column(db.String)
    # jobinfo = db.relationship('Jobinfo', backref='maintable', lazy=True)
    def __repr__(self):
        return f'Jobinfo jobuuid:{self.uuid} job_title:{self.title}'


class Skill(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, unique=True, nullable=False,)
    description = db.Column(db.String)
    name = db.Column(db.String)
    normalized_name = db.Column(db.String)
    onet_element_id = db.Column(db.String)
    type = db.Column(db.String)
    # level =db.Column(db.Float,nullable=False)
    #maintable_jobuuid = db.Column(db.String, db.ForeignKey('maintable.jobuuid'))

    def __repr__(self):
        return f'''Maintable skill_uuid:{self.uuid} skill_title:{self.title} description:{self.description}'''







