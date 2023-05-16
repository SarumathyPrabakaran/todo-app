from flask import Flask, render_template,  request

app = Flask(__name__)

l = []
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == "POST":
        now = request.form.get("todo")
        print(now)
        l.append(now)
        return render_template('index.html', now = now, l = l)
        
    return render_template('index.html', l = l)

if __name__ == "__main__":
    app.run(debug = True, port = 5003)