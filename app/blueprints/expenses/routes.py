from flask import Blueprint, render_template

expenses = Blueprint('expenses', __name__)

@expenses.route('/')
def index():
    return "Welcome to the Expense Tracker"
