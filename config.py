
import os


class Config:
        """  
        General configuration parent class
        """
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        UPLOADED_PHOTOS_DEST = 'app/static/photos'
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
        MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
