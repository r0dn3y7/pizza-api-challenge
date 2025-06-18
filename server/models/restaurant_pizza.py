from server.app import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    # Custom validator: price must be between 1 and 30
    def validate(self):
        errors = []
        if not (1 <= self.price <= 30):
            errors.append("Price must be between 1 and 30")
        return errors

    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'
