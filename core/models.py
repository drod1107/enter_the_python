from core import db

class Projects(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    date = db.Column(db.Date())
    category=db.Column(db.String, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Projects {}>'.format(self.title)