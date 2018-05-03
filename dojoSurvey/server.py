# ------------------------------------------------------------------------------/
#   Assignment: Dojo Survey
#       Objectives:
#          Practice creating a server with Flask from scratch
#          Practice adding routes to a Flask app
#          Practice having the client send data to the server with a form
#          Practice having the server render a template using data provided by the client
#          Practice how to redirect a http request to another urlLearn how you can add other business logics/algorithms directly in flask
#
# ------------------------------------------------------------------------------/


from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# the server is listening for a POST request to:
# localhost:5000/result
# we define the route below such that the route matches the action of our form - '/reuslt'
# similarly we need to allow specific methods - 'POST' in this case
@app.route('/result', methods=['POST'])
def result():
    print('Recieved Post info from form')
    print(request.form)
    # to access the data that the user input into the fields we use request.form['name_of_input']
    newData = request.form
    name = request.form['name']
    location = request.form['location']
    fav = request.form['fav']
    comments = request.form['comments']
     # redirects back to the '/' route
    return render_template('result.html', name=name, location=location, fav=fav, comments=comments)




if __name__=="__main__":

    app.run(debug=True)
