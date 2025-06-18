from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.app import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    errors = restaurant_pizza.validate()
    if errors:
        return jsonify({"errors": errors}), 400

    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify({
        "id": restaurant_pizza.id,
        "price": restaurant_pizza.price,
        "pizza_id": pizza_id,
        "restaurant_id": restaurant_id,
        "pizza": {
            "id": restaurant_pizza.pizza.id,
            "name": restaurant_pizza.pizza.name,
            "ingredients": restaurant_pizza.pizza.ingredients
        },
        "restaurant": {
            "id": restaurant_pizza.restaurant.id,
            "name": restaurant_pizza.restaurant.name,
            "address": restaurant_pizza.restaurant.address
        }
    }), 201
