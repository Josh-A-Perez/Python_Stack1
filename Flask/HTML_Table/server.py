from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def users():
    users = [
        {'first_name' : 'Josh', 'last_name' : 'Perez'},
        {'first_name' : 'Rick', 'last_name' : 'James'},
        {'first_name' : 'Stephen', 'last_name' : 'Curry'},
        {'first_name' : 'Rico', 'last_name' : 'Swave'}
    ]

    return render_template("index.html",users=users)




if __name__=="__main__":
    app.run(debug=True)

