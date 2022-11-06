from flask import *
from registerauthor_dbm import *
from user_registration_form_dbm import *
from addpost_dbm import *
from viewpost_dbm import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/registerauthor")
def regauthor():
    return render_template("registerauthor.html")
    
@app.route("/Userregistrationform")
def reguser():
    return render_template("Userregistrationform.html")

@app.route("/authorinterface")
def loginauthor():
    return render_template("authorinterface.html")


@app.route("/addpost")
def addpost():
    return render_template("addpost.html")

@app.route("/yourpost")
def yourpost():
    active_author=getactiveauthor()
    if len(active_author)>0:
        email = active_author[0]
    posts=showspecificdata(email)
    return render_template("yourpost.html",posts=posts)


@app.route("/allpost")
def allpost():
    posts=showdata()
    return render_template("allpost.html",posts=posts)

@app.route("/Loginasauthor")
def loginasauthor():
    return render_template("Loginasauthor.html")

@app.route("/Loginasuser")
def loginasuser():
    return render_template("Loginasuser.html")


@app.route("/insertdata",methods=["post"])
def insertdata():
    Username=request.form["Username"]
    Password=request.form["password"]
    Email_id=request.form["Emailid"]
    City=request.form["City"]
    t=(Username,Password,City,Email_id)
    insert(t)
    return redirect("/")

@app.route("/userinsertdata",methods=["post"])
def userinsertdata():
    Username=request.form["Username"]
    Password=request.form["password"]
    Email_id=request.form["Emailid"]
    City=request.form["City"]
    u=(Email_id,Username,Password,City)
    userinsert(u)
    return redirect("/")

@app.route("/postinsertdata",methods=["post"])
def postdata():
    username=request.form["author"]
    title=request.form["title"]
    blog=request.form["blog"]
    active_author=getactiveauthor()
    if len(active_author)>0:
        created_by = active_author[0]
    p=(username,title,blog,created_by)
    postinsert(p)
    return redirect("/yourpost")

@app.route("/verify_author_email",methods=["post"])
def verifyauthor():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=checkauthor(email)
    if t in t1:
         activeauthor(email)
         return render_template("authorinterface.html")
    else:
  
        return render_template("Home.html")

@app.route("/verify_user_email",methods=["post"])
def verifyuser():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=checkuser(email)
    if t in t1:
         posts=showdata()
         return render_template("allpost.html", posts=posts)
    else:
  
        return render_template("Home.html")

if __name__=='__main__':
    app.run(debug=True)

#change