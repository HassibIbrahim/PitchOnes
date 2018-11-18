from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import PostForm, CommentForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db, photos
from ..models import User, Post, Comment



@main.route('/')
def index():
    title = 'Home - Welcome to Pitch Me This'
    
    return render_template('index.html', title=title)
