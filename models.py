from flask_sqlalchemy import SQLAlchemy
import passlib

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer_name = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Product id : {self.id} name : {self.name}>'

class Description(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)

    product = db.relationship('Product', backref=db.backref('descriptions', lazy=True))

    def __repr__(self):
        return f'<Description id : {self.id} product_id : {self.product_id}>'

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    product = db.relationship('Product', backref=db.backref('reviews', lazy=True))
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))

    def __repr__(self):
        return f'<Review id : {self.id} product_id : {self.product_id} user_id : {self.user_id}>'
    
class Salt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    salt_name = db.Column(db.String(64), nullable=False)

    product = db.relationship('Product', backref=db.backref('salt', uselist=False))

    def __repr__(self):
        return f'<Salt id : {self.id} product_id : {self.product_id}>'