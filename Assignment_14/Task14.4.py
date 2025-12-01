"""
Flask app that serves a login form and prints username on successful login.

Install: pip install flask
Run:     python app.py
Then visit http://localhost:5000 in your browser.
"""

from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)


@app.route('/')
def index():
    """Serve the login form."""
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    """Handle login form submission.
    
    Expected POST data:
      - username: string (non-empty)
      - password: string (non-empty)
    
    Returns JSON with success/error messages.
    """
    try:
        data = request.get_json()
        if not data:
            # Try form-encoded instead
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '').strip()
        else:
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()

        # Validation
        errors = {}
        if not username:
            errors['username'] = 'Username cannot be empty'
        if not password:
            errors['password'] = 'Password cannot be empty'

        if errors:
            return jsonify({'success': False, 'errors': errors}), 400

        # Successful login — print username to console/stdout
        print(f'\n✓ Login successful!', file=sys.stderr)
        print(f'  Username: {username}', file=sys.stderr)
        print(f'  Password: {"*" * len(password)}', file=sys.stderr)
        print()

        return jsonify({
            'success': True,
            'message': f'Login successful! Welcome, {username}.',
            'username': username
        }), 200

    except Exception as exc:
        print(f'Error during login: {exc}', file=sys.stderr)
        return jsonify({'success': False, 'error': str(exc)}), 500


@app.route('/health')
def health():
    """Simple health check endpoint."""
    return jsonify({'status': 'ok'}), 200


if __name__ == '__main__':
    print('Starting Flask app on http://localhost:5000')
    print('Press Ctrl+C to stop.\n')
    app.run(debug=True, host='localhost', port=5000)
