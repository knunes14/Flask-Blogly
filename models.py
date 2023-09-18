from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

"""Models for Blogly."""

class User(db.Model):
    """Site user"""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    
    first_name = db.Column(db.Text(50),
                     nullable=False,
                     unique=True)
    
    last_name = db.Column(db.Text(50),
                     nullable=False,
                     unique=True)
    
    image_url = db.Column(db.Text(255), nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    



