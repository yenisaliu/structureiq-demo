# StructureIQ Demo
# This is a demo Flask app that simulates a backend system for structural monitoring. It connects to a local SQLite DB, processes sensor data differently depending on the asset type (bridge or building), and displays filtered data in a simple, Bootstrap-styled web dashboard. It allows users to switch between asset types and user roles (engineer, inspector, analyst). It logs database query times to simulate performance monitoring. It was built using modular backend code with unit tests for asset-specific logic
.
# Tech used: Python3, Flask, SQLite, Jinja2, Bootstrap 5, unittest.
# Run: Install Flask with pip install flask. Run init_db.py to generate the database and sample data. Start the app by running app.py. Open your browser and visit http://127.0.0.1:5000/dashboard






