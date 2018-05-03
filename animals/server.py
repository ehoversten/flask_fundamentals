# ------------------------------------------------------------------------------/
#   Assignment: Cute Animals
#       Objectives:
#          Practice adding static files to the template files
#          Practice passing information from route to template
#          Learn how you can add other business logics/algorithms directly in flask
#
# ------------------------------------------------------------------------------/


from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<num>')
def number(num):
    print(num)
    return render_template('index.html', num=int(num))

@app.route('/danger')
def danger():
    print("User has accessed the DANGER ZONE!!")
    return redirect('/')

if __name__=="__main__":

    app.run(debug=True)
