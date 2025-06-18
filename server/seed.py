from server.app import create_app
from server.config import db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Pepperoni, Cheese")

    # Create restaurants
    r1 = Restaurant(name="Kiki's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's", address="456 Side St")

    # Create join records
    rp1 = RestaurantPizza(price=10, pizza=p1, restaurant=r1)
    rp2 = RestaurantPizza(price=15, pizza=p2, restaurant=r1)

    db.session.add_all([p1, p2, r1, r2, rp1, rp2])
    db.session.commit()
