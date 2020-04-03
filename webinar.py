import subprocess
#import re
#import socket
import logging

from flask import Flask, jsonify, request, render_template, flash
from flask.logging import create_logger
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


class ReusableForm(Form):
    message = TextField('Please enter a message:', validators=[validators.DataRequired()])


# Instantiate our Node
app = Flask(__name__)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# Enable logging
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/", methods=['GET', 'POST'])
def handle_input():
    # Get node name and pod IP address, then pass it to the template
    node_name = subprocess.run(["hostname"])

    # Send node name to the template for rendering
    flash(node_name)
    
    # Proceed to the form
    form = ReusableForm(request.form)
    print(form.errors)
    
    if (request.method == 'POST'):
        message = request.form['message']
 
        if (form.validate()):
            # Handle the message: create a file with a name of the message text without spaces
            try:
                open("".join(message.split()), "w+", encoding='utf-8').close()
            except:
                LOG.info("Error creating a file from the message {}".format(message))
                flash('Epic fail. Something went wrong...')
            else:
                LOG.info("Message {} received and written to a file".format(message))
                flash('Thank you. Your message was written to a file!')
        else:
            flash('Please enter some text. The input field must not be empty.')
 
    return render_template('handle_input.html', form=form)

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)
