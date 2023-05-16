from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    #done = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}>'
    def __init__(self, id, title):
        self.id = id
        self.title = title
        #self.done = done