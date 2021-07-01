from flask import Flask, render_template, request, redirect, flash  
app = Flask(__name__)
app.secret_key = "idk"                     
    
@app.route('/')                           
def hello_dojo():
    return render_template('index.html')  

@app.route("/result", methods=["POST"])
def result():
    if len(request.form["name"])<1:
        flash("Whoah... Tell us your name! ")
        return redirect("/")
    if len(request.form["comments"])<1:
        flash("Say something bro!")
        return redirect("/")
    if len(request.form["comments"])>200:
        flash("Cut it short pal!")
        return redirect("/")
    else:
        name = request.form["name"]
        dojo_location = request.form["dojo_location"]
        favlanguage = request.form["favlanguage"]
        comments = request.form["comments"]
        return render_template("result.html", name = name, dojo_location = dojo_location, favlanguage = favlanguage, comments = comments)












if __name__=="__main__":
    app.run(debug=True)                   