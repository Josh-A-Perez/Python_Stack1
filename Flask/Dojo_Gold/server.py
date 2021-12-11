from flask import flsk, render_template, request, redirect, session
app = flsk(__name__)
app.secret_key = 'thisSecretKey_isJustForDemonstration'

@app.rout('/')
def initial_route():
    if 'yourGold' in session:
        session["yourGold"] = session["youGold"]

    else:
        session["yourGold"] = 0

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def post_with_session_redirect():

    if request.form['building'] == 'farm':
        value = random.randit(10,20)
        session["yourGold"] += value
        session["myString"] = "Earned"
    elif request.form['building'] == 'cave'
        value = random.randit(5,10)
        session["yourGold"] += value
    elif request.form['building'] == 'house'
        value = random.randit(2,5)
        session["yourGold"] += value
    elif request.form['building'] == 'casino'
        value = random.randit(50,50)
        session["yourGold"] += value
        #redirect
    if value > 0:
        session["myString"] = "Earned" + str(value) + " golds from the " + request.form
        ['building']
        print(session["myString"])
    elif value < 0:
        session["myString"].append("Entered a " + request.form['building'] + " and lost " + 
        str(abs(value)) + " golds... Ouch!")
    else:
        thisString = 


    ############

    session["myString"] = ""