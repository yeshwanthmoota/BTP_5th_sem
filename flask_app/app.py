from flask import Flask, request, render_template, redirect
import os
import webbrowser

from flask.helpers import url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/hill_racing", methods=["GET"])
def hill_racing():
    if request.method == "GET":
        webbrowser.open("https://www.topgames.com/play/Hill-Climb-Racing")
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Hill_racing")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 hill_racing.py")

        
    return redirect(url_for('home'))

@app.route("/crazy_roll", methods=["GET"])
def crazy_roll():
    if request.method == "GET":
        webbrowser.open("https://www.crazygames.com/game/crazy-roll-3d")
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Crazy_roll")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 crazy_roll.py")

    return redirect(url_for('home'))

@app.route("/snake_game", methods=["GET"])
def snake_game():
    if request.method == "GET":
        path_list = (os.path.dirname(__file__)).split("/")
        print(path_list)
        if path_list[-1] == "flask_app":
            path_list.pop(-1)
            print(path_list)    
        final_path = "/".join(path_list)
        print(final_path)
        os.chdir(final_path+"/Snake_game")
        print(os.getcwd())
        print("################ Directory Changed ################")
        os.system("python3 main.py")
        

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)