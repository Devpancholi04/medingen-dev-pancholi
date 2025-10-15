from flask import Blueprint, jsonify, request
from models import db, User, Product, Description, Review, Salt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message" : "Missing required fields"}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400
    
    password_hash = generate_password_hash(password)

    new_user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username = username).first()

    if user:
        check_password = check_password_hash(user.password_hash, password)

        if check_password:
            token = create_access_token(identity=username)
            return jsonify({'status' : 'Success','message': 'Login Success', 'access Token': token}), 200
        
    return jsonify({'status' : 'Failed', 'message' : 'Invalid Cerdentials'}), 400


@api.route('/products/', methods=['GET'])
@api.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()
def get_all_products(product_id=None):
    current_user = get_jwt_identity()

    if product_id is None:
        product = Product.query.all()
        data = [{
            "id" : p.id,
            "name" : p.name,
            "manufacturer_name" : p.manufacturer_name,
            "price" : p.price,
            'stock' : p.stock,
            'image_url' : p.image_url
        } for p in product ] 

    else:
        product = Product.query.filter_by(id=product_id).first()
        if not product:
            return jsonify({
                'Status' : 'Failed',
                'Message' : 'Product Not Found!'
            }), 404
        
        data ={
            "id" : product.id,
            "name" : product.name,
            "manufacturer_name" : product.manufacturer_name,
            "price" : product.price,
            'stock' : product.stock,
            'image_url' : product.image_url
        } 

    return jsonify({
        'Status' : 'Success',
        'Message' : "Fetch Success",
        'Data' : data
    }), 200
    

@api.route('/description/<int:product_id>', methods=['GET'])
@jwt_required()
def get_description(product_id):
    current_user = get_jwt_identity()
    desc = Description.query.filter_by(product_id = product_id).first()
    if not desc:
        return jsonify({
            'Status' : 'Failed',
            'Message' : 'Product Not Found!'
        }), 404
    
    return jsonify({
        'Status' : 'Success',
        'Message' : "Fetch Success",
        'Data' : {
            'id' : desc.id,
            'product_id' : desc.product_id,
            'text' : desc.text
        }
    }), 200

@api.route('/review/<int:product_id>', methods=['GET'])
@jwt_required()
def get_reviews(product_id):
    current_user = get_jwt_identity()
    review = Review.query.filter_by(product_id = product_id).first()
    if not review:
        return jsonify({
            'Status' : 'Failed',
            'Message' : 'Product Not Found!'
        }), 404
    
    return jsonify({
        'Status' : 'Success',
        'Message' : "Fetch Success",
        'Data' : {
            'id' : review.id,
            'product_id' : review.product_id,
            'user_id' : review.user_id,
            'rating' : review.rating, 
            'comment' : review.comment
        }
    }), 200

@api.route('/salt/<int:product_id>', methods=['GET'])
@jwt_required()
def get_salt(product_id):
    current_user = get_jwt_identity()
    salt = Salt.query.filter_by(product_id = product_id).first()
    if not salt:
        return jsonify({
            'Status' : 'Failed',
            'Message' : 'Product Not Found!'
        }), 404
    
    return jsonify({
        'Status' : 'Success',
        'Message' : "Fetch Success",
        'Data' : {
            'id' : salt.id,
            'product_id' : salt.product_id,
            'salt_name' : salt.salt_name
        }
    }), 200


    
    