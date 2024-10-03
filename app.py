from flask import Flask, render_template, url_for

import os
EMBLEM_FOLDER= os.path.join('static', 'images')
app =Flask(__name__)



app.config['UPLAOD_FOLDER'] = EMBLEM_FOLDER 

@app.route("/")
<!--@app.route("/index")-->
def home():
    
    return render_template('index.html')
    
    
@app.route("/coroverview")
def coroverview():
    return render_template('coroverview.html')
    
@app.route("/sched")
def sched ():
    return render_template('sched.html')
    
@app.route("/gallery")
def gallery():
    return render_template('gallery.html')
    
@app.route("/officers")
def officers ():
    return render_template('officers.html')
    
@app.route("/const")
def const():
    return render_template('const.html')
    

@app.route("/jan")
def jan():
    return render_template('jan.html')

@app.route("/feb")
def feb():
    return render_template('feb.html')

@app.route("/mar")
def mar():
    return render_template('mar.html')

@app.route("/apr")
def apr():
    return render_template('apr.html')

@app.route("/may")
def may():
    return render_template('may.html')

@app.route("/jun")
def jun():
    return render_template('jun.html')

@app.route("/jul")
def jul():
    return render_template('jul.html')

@app.route("/aug")
def aug():
    return render_template('aug.html')


@app.route("/sept")
def sept():
    return render_template('sept.html')
    
@app.route("/oct")
def oct():
    return render_template('oct.html')

@app.route("/nov")
def nov():
    return render_template('nov.html')

@app.route("/dec")
def dec():
    return render_template('dec.html')    
    
@app.route("/gjan")
def gjan():
    return render_template('gjan.html')
    
@app.route("/gapr")
def gapr():
    return render_template('gapr.html')
    
@app.route("/gmay")
def gmay():
    return render_template('gmay.html')
    
@app.route("/gjun")
def gjun():
    return render_template('gjun.html')

@app.route("/gaug")
def gaug():
    return render_template('gaug.html')
    
@app.route("/gsep")
def gsep():
    return render_template('gsep.html')
   
        
if __name__ == "__main__":
    app.run()