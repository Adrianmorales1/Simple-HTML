from flask_app import app
from flask import Flask, request, session, render_template, flash, redirect
from flask_app.models.email_send import Email

@app.route('/')
def dashboard():
    return render_template('homePage.html')

@app.route('/test', methods = ['POST'])
def send_email():
    data = {
        'subject' : request.form['subject'],
        'body' : request.form['content'],
        'sender' : request.form['sender']
    }
    email = Email()
    email.send_email(data)
    return redirect('/')