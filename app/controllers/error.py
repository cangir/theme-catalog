#!/usr/bin/python3
from flask import render_template, redirect, url_for, session
from flask_login import login_user, logout_user, current_user


@app.route("/404")
def error_404():
    # Check if current user is authenticated
    # If authenticated redirect homepage
    # Else render login page
    return render_template("error/404.html")
