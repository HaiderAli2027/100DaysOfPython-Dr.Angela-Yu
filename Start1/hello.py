from flask import Flask

app = Flask(__name__)

def make_Bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper
def Make_Italic(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_UnderLine(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "Hello, World!"

# Diff route using app.route decorator
@app.route("/bye")
@make_Bold
@Make_Italic
@make_UnderLine
def bye():
    return "This is a simple by function and this is done by using a forewarding path decorator "

# Creating a word path then converting the path to a specific data type
@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # run the app in the debug mode to auto reload
    app.run(debug = True)