# Import necessary modules
from flask import Flask, render_template,  request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv() 

database   = os.getenv('DB_NAME')
user       =os.getenv('DB_USER')
password   =os.getenv('DB_PASS')
host       =os.getenv('DB_HOST')
port       = (os.getenv('DB_PORT'))

app = Flask(__name__)

# Configure the PostgreSQL database connection

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create a class representing the database schema for the todo table
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
   

    def __repr__(self):
        return f'<Todo {self.id}>'
    def __init__(self, id, title):
        self.id = id
        self.title = title
   
   

# Set up a route for rendering the HTML template and processing POST requests
@app.route('/',methods = ['GET','POST'])
def index():
    
    # Fetch all todo items from the database
    objs = db.session.query(Todo).all() 
    
    # Handle form submission
    if request.method == "POST":
        now = request.form.get("todo")
        
        # Create a new Todo object with the submitted title
        now_id = db.session.query(Todo.id).all()
        todo_obj =  Todo(len(now_id)+1,now)
        
        # Add the new todo to the database session and commit the changes
        db.session.add(todo_obj)
        db.session.commit()
        
        # Refresh the list of todos from the database
        objs = db.session.query(Todo).all() 
        
      # Render the index.html template and pass the list of todos to it
    return render_template('index.html', l = objs)

if __name__ == "__main__":
    
    app.run(debug = True, port = 5003)

