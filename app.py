from flask import Flask, render_template, request
from db import get_sensor_data
from modules import get_asset_module

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to StructureIQ Demo"

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        asset_type = request.form.get('asset', 'bridge')
        user = request.form.get('user', 'engineer')
    else:
        asset_type = request.args.get('asset', 'bridge')
        user = request.args.get('user', 'engineer')

    module = get_asset_module(asset_type)
    data = get_sensor_data(asset_type)
    processed = module.process(data)

    return render_template('dashboard.html', data=processed, asset=asset_type, user=user)

if __name__ == '__main__':
    app.run(debug=True)