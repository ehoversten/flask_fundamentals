# ------------------------------------------------------------------------------/
#   Assignment: Understanding Routing
#       Objectives:
#           Practice building a server with Flask from scratch
#           Get comfortable with routes and passing information to the routes
#
# ------------------------------------------------------------------------------/


from flask import Flask

app = Flask(__name__)

print(__name__)
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<count>/<given_input>')
def repeat_hello(count, given_input):
    print(count)
    print(given_input)
    print(f"{given_input} \n" * int(count))
    return given_input * int(count)


if __name__=="__main__":

    app.run(debug=True)

