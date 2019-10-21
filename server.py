from flask import *
from pymongo import MongoClient
from bson import json_util
import base64

client = MongoClient()
db = client.ProjectDB
user_info = db.UserInfo



app = Flask(__name__)
app.secret_key = "abc"
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
    session["login"] = uname
    myquery = {"uname":uname}
    data_unlog = "Sign up first!"
    data_unpass = "Incorrect Password!"
    result = user_info.find_one(myquery)
    if result:
        if(result["pwd"]!=base64.b64encode(password)):
            return render_template("login.html",data=data_unpass)
        else:
            return redirect(url_for("renderTwit"))
    else:
        return render_template("login.html",data = data_unlog)
    #return redirect(url_for("renderHome"))
    

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
    pwd_enc = base64.b64encode(pwd)
    cpwd = request.form["cpwd"]
    pwd_dec = base64.b64encode(pwd)
    if(pwd!=cpwd){
        return render_template("Signup.html",data="Passwords do not match")
    }
    else{
        send_dict = {
        "Name": Name,
        "Mail": mail,
        "age": age,
        "address": add,
        "uname": uname,
        "pwd": pwd_enc,
        "cpwd": cpwd_end
        }
    user_info.insert_one(send_dict)
    return redirect(url_for("renderHome"))
    }
    
    
@app.route("/answers",methods=['POST'])

def checkanswer():
    if(request.is_json):

        data = request.get_json["data"]
        newvalues = { "$set": { "data": data } }
        my_query = {"uname":session["login"]}
        result = user_info.update_one(my_query,newvalues)
        return render_html("blank_page.html",result=data)
    else:
        return "LOL"

@app.route("/data")
def renderDataPage():
    return render_template("data.html")



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
    ret_dict = {}
    ret_dict["green"] = request.form["green"]
    ret_dict["poll"] = request.form["pollution"]
    ret_dict["clean"] = request.form["clean"]
    if("traffic_yes" in request.form.keys()):
        ret_dict["traffic"] = "yes"
    else:
        ret_dict["traffic"] = "no"
    if("safe_yes" in request.form.keys()):
        ret_dict["safe"] = "yes"
    else:
        ret_dict["safe"] = "no"

    my_query = {"uname":session["login"]}
    newvalues = { "$set": { "ratings": ret_dict } }
    user_info.update_one(my_query,newvalues)
    result = user_info.find_one(my_query)
    req_dict = json.dumps(result,default=json_util.default)

    return render_template("boiler_template.html",result=result)

@app.route("/signout")
def signout():
    session.clear()
    return render_template("Project_Homepage.html")


if __name__=='__main__':
    app.run("localhost",8000,debug=True)