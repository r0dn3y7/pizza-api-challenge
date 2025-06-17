from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.config import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(rp)
        db.session.commit()

        pizza = Pizza.query.get(data['pizza_id'])
        restaurant = Restaurant.query.get(data['restaurant_id'])

        return jsonify({
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
