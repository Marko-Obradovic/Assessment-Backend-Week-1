"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, Response, request, jsonify

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age)

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})


@app.get("/between")
def get_days_between_two_dates():
    args = request.args.to_dict()

    dates = request.json

    dates_first = dates["first"]
    dates_last = dates["last"]

    dates_first_datetime_object = convert_to_datetime(dates_first)
    dates_last_datetime_object = convert_to_datetime(dates_last)

    days_between = get_days_between(first=dates_first_datetime_object,
                     last=dates_last_datetime_object) 
    print(days_between)
    return dates

if __name__ == "__main__":
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.run(port=8080, debug=True)
