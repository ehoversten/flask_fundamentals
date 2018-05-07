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


from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'KeepItSecrectKeepItSafe'

@app.route('/')
def index():
    if 'name' not in session:
        session['name'] = ''
    if 'location' not in session:
        session['location'] = ''
    if 'fav' not in session:
        session['fav'] = ''
    if 'comment' not in session:
        session['comment'] = ''
    return render_template('index.html')

# the server is listening for a POST request to:
# localhost:5000/result
# we define the route below such that the route matches the action of our form - '/reuslt'
# similarly we need to allow specific methods - 'POST' in this case
# @app.route('/result', methods=['POST'])
# def result():
#     print('Recieved Post info from form')
#     print(request.form)
#     # to access the data that the user input into the fields we use request.form['name_of_input']
#     newData = request.form
#     name = request.form['name']
#     location = request.form['location']
#     fav = request.form['fav']
#     comments = request.form['comments']
#      # redirects back to the '/' route
#     return render_template('result.html', name=name, location=location, fav=fav, comments=comments)

@app.route('/process', methods=['POST'])
def process():
    # newData = request.form
    if len(request.form['name']) < 1:
        # display validation errors
        session['comment'] = request.form['comment']
        # session['location'] = request.form['location']
        # session['fav'] = request.form['fav']
        print('Name field cannot be empty')
        flash('Name field cannot be empty')
        # redirect('/')
    if len(request.form['comment']) < 1:
        # display validation errors
        session['name'] = request.form['name']
        # session['location'] = request.form['location']
        # session['fav'] = request.form['fav']
        print('Comment field cannot be empty')
        flash('comment field cannot be empty')
        # redirect('/')
    if len(request.form['comment']) > 120:
        # display validation errors
        session['name'] = request.form['name']
        # session['location'] = request.form['location']
        # session['fav'] = request.form['fav']
        print('Comment field cannot be over 120 characters long')
        flash('Comment field cannot be over 120 characters long')
    else:
        # newData = request.form
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['fav'] = request.form['fav']
        session['comment'] = request.form['comment']
        return render_template('result.html', name=session['name'], location=session['location'], fav=session['fav'], comment=session['comment'])

    return redirect('/')

@app.route('/result', methods=['POST'])
def result():
    print(session)
    flash('Welcome ' + session['name'])
    return render_template('result.html')


if __name__=="__main__":

    app.run(debug=True)
