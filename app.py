from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from oauth import init_oauth, google
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = load_dotenv("GOOGLE_CLIENT_SECRET")
init_oauth(app)

@app.route('/')
def home():
    if 'google_token' in session:
        user_info = google.get('userinfo').data
        return f"Hello, {user_info['name']}! You are logged in with Google."
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return 'Logged out.'

@app.route('/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason={0} error={1}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    return redirect(url_for('home'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')
# 

@app.route('/')
def root():
    return render_template('point-hub.html')

@app.route('/point-hub')
def point_hub():
    return render_template('point-hub.html')

@app.route('/getUserInfo')
def get_user_info():
    try:
        current_points = 100
        points_per_click = 5

        user_info = {
            'currentPoints': current_points,
            'pointsPerClick': points_per_click
        }

        return jsonify({
            'status': 'success',
            'userInfo': user_info
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/incrementPoints', methods=['POST'])
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
