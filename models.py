from database import db
from datetime import datetime


# 🏢 MERCHANT TABLE
class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    razorpay_key_id = db.Column(db.String(200), nullable=False)
    razorpay_key_secret = db.Column(db.String(200), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    machines = db.relationship("Machine", backref="merchant", lazy=True)

    def __repr__(self):
        return f"<Merchant {self.name}>"


# 🏧 MACHINE TABLE
class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    machine_id = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(200))

    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant.id'), nullable=False)

    # 🔐 SECURITY TOKEN (VERY IMPORTANT)
    machine_token = db.Column(db.String(200), unique=True, nullable=False)

    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    payments = db.relationship("Payment", backref="machine", lazy=True)

    def __repr__(self):
        return f"<Machine {self.machine_id}>"


# 💳 PAYMENT TABLE
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.String(200), unique=True, nullable=False)
    payment_id = db.Column(db.String(200))

    machine_id = db.Column(db.Integer, db.ForeignKey('machine.id'), nullable=False)

    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default="created")  # created / success / failed

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Payment {self.order_id}>"