from flask import Flask, render_template,  request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@0.0.0.0:5432/saru'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
   

    def __repr__(self):
        return f'<Todo {self.id}>'
    def __init__(self, id, title):
        self.id = id
        self.title = title
    
objs = []
@app.route('/',methods = ['GET','POST'])
def index():
    global objs
    objs = db.session.query(Todo).all() 
    if request.method == "POST":
        now = request.form.get("todo")
        
        
        now_id = db.session.query(Todo).all()
        
        todo_obj =  Todo(len(now_id)+1,now)
        db.session.add(todo_obj)
        db.session.commit()
        objs = db.session.query(Todo).all() 
        return render_template('index.html', l = objs)
 
    return render_template('index.html', l = objs)

if __name__ == "__main__":
    
    app.run(debug = True, port = 5003)

