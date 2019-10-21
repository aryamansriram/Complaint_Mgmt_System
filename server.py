from flask import *
app = Flask(__name__)
@app.route('/')

#Landing Page
def home():
    return render_template("login.html")

#Home page
@app.route('/home')

def renderHome():
    return render_template("Project_Homepage.html")

#Login Page
@app.route("/login",methods=['POST'])

def requestCheck():
    uname = request.form["username"]
    password = request.form["password"]
    return redirect(url_for("renderHome"))


#Signup Page
@app.route("/Signup")
def renderSignUp():
    return render_template("Signup.html")


@app.route("/signup_validate",methods=['POST'])
def signupCheck():
    Name = request.form["Name"]
    mail = request.form["mail"]
    age = request.form["age"]
    add = request.form["add"]
    uname = request.form["uname"]
    pwd = request.form["pwd"]
    cpwd = request.form["cpwd"]
   
    return redirect(url_for("renderHome"))
    
@app.route("/answers",methods=['POST'])

def checkanswer():
    answer = request.form["answer"]
   
    return answer

@app.route("/data")
def renderDataPage():
    return render_template("data.html")

@app.route("/testing")
def renderTest():
    return render_template("Phmpg2.html")

@app.route("/twit")
def renderTwit():
    return render_template("twitter.html")
    

@app.route("/ratings")
def renderRatings():
    return render_template("ratings.html")

@app.route("/data")
def renderData():
    return render_template("data.html")

@app.route("/ratings_validate",methods=["POST"])
def val():
    green = request.form["green"]
    poll = request.form["pollution"]
    clean = request.form["clean"]
    if("traffic_yes" in request.form.keys()):
        traff_yes = request.form["traffic_yes"]
    else:
        traff_no = request.form["traffic_no"]
    if("safe_yes" in request.form.keys()):
        safe_yes = request.form["safe_yes"]
    else:
        safe_no = request.form["safe_no"]

    return request.form


if __name__=='__main__':
    app.run("localhost",8000,debug=True)