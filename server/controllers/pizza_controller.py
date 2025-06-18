from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    } for pizza in pizzas])
