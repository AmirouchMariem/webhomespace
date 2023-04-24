from flask import Flask , render_template ,request , send_file

from Authentication import Authentication
from GsFIlesFolders import GsFIlesFolders
from Account import Account

import os

authi : Authentication
gsFiledr = GsFIlesFolders()
account = compte()
pathcurent : str = ""
fixUsername : str = ""

app = Flask(__name__,template_folder="templates",static_folder = 'static')

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route('/logout')
def lougout():
    return render_template("index.html")


@app.route("/")
def accueil():
    return render_template("index.html")

@app.route('/logout')
def lougout():
    return render_template("index.html")

@app.route("/auth",methods =["GET","POST"])
def home():
    global fixUsername
    global pathcurent
    username : str = request.form['username']
    password : str = request.form['password']
    authi = Authentication(username,password)
    if username != "" :
        if authi.authenti() == True:   
            fixUsername = username
            pathcurent = "/home/"+username
            return render_template("index.html",directory = gsFiledr.getPath("/home/"+username) )
    return render_template("index.html",erreur = "username or password incorrect ")

@app.route('/<path:path>/',methods =["GET"])
def routefolders(path):
    try :
        global pathcurent
        pathcurent = "/"+path
        if os.path.isdir(pathcurent):
            return render_template("index.html",directory = gsFiledr.getPath(pathcurent))
        elif os.path.isfile(pathcurent):
            f = open(pathcurent)
            return render_template("index.html",text = f.read())
    except :
        return "erreur"

@app.route('/back',methods =["GET","POST"])
def back():
    global pathcurent
    t = pathcurent.split("/")
    if len(t) != 3 :
        pathcurent = ""
        for i in range(len(t)-1):
            pathcurent += t[i] + "/"
        pathcurent = pathcurent[:len(pathcurent)-1]
  
    if os.path.isdir(pathcurent):
       return render_template("index.html",directory = gsFiledr.getPath(pathcurent))

@app.route("/download")
def download():
    gsFiledr.telechercherHomeDerectory(fixUsername)
    return send_file("/home/"+fixUsername+"/"+fixUsername+".zip", as_attachment=True)

@app.route('/nbrfiles')
def nbrfiles():
    return render_template("index.html",directory = gsFiledr.getPath(pathcurent),fil = str(gsFiledr.getnbrFichier(pathcurent)))

@app.route('/nbrdir')
def nbrdirs():
    return render_template("index.html",directory = gsFiledr.getPath(pathcurent),dir = str(gsFiledr.getnbrDirectory(pathcurent)))

@app.route('/space')
def space():
    return render_template("index.html",directory = gsFiledr.getPath(pathcurent),spa = str(gsFiledr.gettaille(pathcurent)))

@app.route('/findfile',methods =["GET","POST"])
def fileSearch():
    filename : str = request.form['file']
    return render_template("index.html",directory = gsFiledr.rechercheFilesNameFileExtention(pathcurent,filename))

if __name__ == '__main__':
    app.run()

