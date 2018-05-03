# ------------------------------------------------------------------------------/
#   Assignment: HTML Table
#       Objectives:
#          Get comfortable passing information from the route to the template
#          Get very comfortable iterating through a list of dictionaries to generate a html output.  This is very important for all web development as records returned from a database will almost always be in this format.
#
# ------------------------------------------------------------------------------/

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def users():
    users = (
       {'first_name' : 'Michael', 'last_name' : 'Choi'},
       {'first_name' : 'John', 'last_name' : 'Supsupin'},
       {'first_name' : 'Mark', 'last_name' : 'Guillen'},
       {'first_name' : 'KB', 'last_name' : 'Tonel'}
    );
    print(users)
    return render_template('index.html', users=users)

if __name__=="__main__":

    app.run(debug=True)
