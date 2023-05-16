from flask import Flask, render_template,  request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@0.0.0.0:5432/first'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




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
@app.before_first_request
def create_tables():
    db.create_all()

l = []
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == "POST":
        now = request.form.get("todo")
        print(now)
        l.append(now)
        now_id = db.session.query().all()
        todo_obj =  Todo(len(now_id)+1,now)
        db.session.add(todo_obj)
        db.session.commit()
        return render_template('index.html', now = now_id, l = now_id)
        
    return render_template('index.html', l = l)

if __name__ == "__main__":
    
    app.run(debug = True, port = 5003)

