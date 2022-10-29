from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
import smtplib
from flask_mail import Mail, Message
import os

mail_username = os.environ.get("M_USERNAME")
mail_password = os.environ.get("M_PASSWORD")


app = Flask(__name__)
app.config['MAIL_SERVER'] ="smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password




mail = Mail(app)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)