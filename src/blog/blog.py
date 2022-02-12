from src import db
from datetime import datetime
class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    content=db.Column(db.Text,nullable=False)
    author=db.Column(db.String(50),nullable=False)
    tag=db.Column(db.String(20),nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    reaction=db.Column(db.String(50),nullable=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'tag':self.tag,
            'created_at': self.created_at,
            'reaction': self.reaction
        }
