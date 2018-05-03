# ------------------------------------------------------------------------------/
#   Assignment: Checkerboard
#       Objectives:
#          Continue to learn how to pass information from the url to the route
#          Get comfortable passing information from the route to the template
#          Understand how to use for loop properly in the template
#          Recognize the value of creating a html/css first and then adding logic/code
# ------------------------------------------------------------------------------/

from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/<count>')
# def index(count):
#     print(count)
#     return render_template('index.html', num=int(count))

@app.route('/<x>/<y>')
def index(x, y):
    print(x)
    print(y)
    return render_template('index.html', rowNum=int(x), colNum=int(y))

if __name__=="__main__":

    app.run(debug=True)