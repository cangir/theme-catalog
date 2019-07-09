#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
description: Authentication controller
copyright: (c) 2019 by Ahmet Cangir
license: https://github.com/cangir/theme-catalog/blob/master/LICENSE
"""
from app.models.user import User
from flask import render_template, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user

from app import app, db, login_manager
from app.libraries.oauth import OAuthSignIn


@app.route("/login")
def login():
    # Check if current user is authenticated
    # If authenticated redirect homepage
    # Else render login page
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # Clear logged in user's session
    session.clear()
    logout_user()
    # Redirect home
    return redirect(url_for("home"))


@login_manager.user_loader
def load_user(user_id):
    # Load the logged in user
    return db.session.query(User).get(int(user_id))


@app.route("/authorize/<string:provider>")
def oauth_authorize(provider):
    # Perform outh authorization with selected provider
    if not current_user.is_anonymous:
        return redirect(url_for('categories'))

    # Get the item provider and authorize access
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route("/callback/<string:provider>")
def oauth_callback(provider):
    # Get the profile information of authorized user
    if not current_user.is_anonymous:
        return redirect(url_for("home"))

    oauth = OAuthSignIn.get_provider(provider)
    username, email, picture = oauth.callback()

    if email is None:
        flash("Error: Authentication.")
        return redirect(url_for("home"))

    # Add user if not exists
    user = db.session.query(User).filter_by(email=email).first()
    if not user:
        user = User(name=username, email=email, avatar=picture)
        db.session.add(user)
        db.session.commit()

    # Log the user in and redirect to main page.
    login_user(user, True)
    return redirect(url_for("home"))
