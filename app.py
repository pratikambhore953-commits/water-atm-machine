from routes.admin import admin_bp
from flask import Flask, render_template
from dotenv import load_dotenv
import os

from database import db
from routes.create_order import create_order_bp
from routes.webhook import webhook_bp
from routes.machine import machine_bp

load_dotenv()

app = Flask(__name__)

# ✅ DATABASE CONFIGURATION
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///water_atm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# ✅ REGISTER BLUEPRINTS
app.register_blueprint(create_order_bp)
app.register_blueprint(webhook_bp)
app.register_blueprint(machine_bp)
app.register_blueprint(admin_bp)

# ✅ HOME ROUTE
@app.route("/")
def home():
    return "Smart Water QR Backend Running"

# ✅ PAYMENT PAGE ROUTE (ADD THIS)
@app.route("/pay")
def pay():
    return render_template("index.html")

# ✅ RUN APP
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)