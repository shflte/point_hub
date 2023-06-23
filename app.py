from flask import Flask, render_template, request, jsonify
from flask_oauthlib.client import OAuth
from dotenv import load_dotenv

app = Flask(__name__)

# Set up your database and other configurations

@app.route('/')
def root():
    return render_template('point-hub.html')

@app.route('/point-hub')
def point_hub():
    return render_template('point-hub.html')

@app.route('/updatePoints', methods=['POST'])
def update_points():
    points_per_click = request.form.get('pointsPerClick')

    # Perform the necessary logic to update the points in your database
    # You can access the value of 'points_per_click' and update the corresponding user's points
    update_successful = True

    # If the update is successful
    if update_successful:
        response = {
            'status': 'success',
            'message': 'Points updated successfully.'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 'error',
            'message': 'Failed to update points.'
        }
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
