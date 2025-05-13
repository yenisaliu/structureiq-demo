# StructureIQ Demo
# This is a demo Flask app that simulates a backend system for structural monitoring. It connects to a local SQLite DB, processes sensor data differently depending on the asset type (bridge or building), and renders a basic dashboard.
# Tech used: Python, Flask, SQLite, Jinja2, unittest.
# Run: python app.py then visit http://localhost:5000/dashboard?asset=bridge

StructureIQ Demo Dashboard
This is a self-hosted backend dashboard system inspired by my interview with StructureIQ. It simulates how sensor data from civil infrastructure (such as bridges and buildings) can be processed and displayed using modular Python logic, a relational database, and the Flask web framework.

What It Does
Connects to a local SQLite database (sensor.db)

Processes and filters sensor data differently depending on the selected asset type (bridge or building)

Displays filtered data in a simple, Bootstrap-styled web dashboard

Allows users to switch between asset types and user roles (engineer, inspector, analyst)

Logs database query times to simulate performance monitoring

Built using modular backend code with unit tests for asset-specific logic

Tech Stack
Python 3

Flask

SQLite

Jinja2 (for templating)

Bootstrap 5 (for styling)

unittest (for backend testing)


How to Run
Clone the repository and navigate to the project folder.

(Optional) Create and activate a virtual environment.

Install Flask with pip install flask.

Run init_db.py to generate the database and sample data.

Start the app by running app.py.

Open your browser and go to:
http://127.0.0.1:5000/dashboard
Use the dropdown to select asset type and user role.

Available Parameters
asset: bridge or building
user: engineer, inspector, or analyst

Running Tests
To run the unit test, run test_app.py.

Author
Created by Yeni Femi-Saliu as a backend development and system design demo project.