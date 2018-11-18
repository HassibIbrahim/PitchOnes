from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import PostForm, CommentForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db, photos
from ..models import User, Post, Comment


@main.route('/')
def index():
    title = 'Home - Welcome to Pitch Ones'

    return render_template('index.html', title=title)


@main.route('/category/<ct_name>')
def category(ct_name):
    category = ct_name
    title = f'{category}'
    posts = Post.get_posts(category)
    return render_template('category.html', title=title, category=category, posts=posts)


@main.route('/category/comments/<int:id>')
def comments(id):
    title = 'Comments'
    comments = Comment.get_comments(id)
    return render_template('comments.html', title=title, comments=comments)
