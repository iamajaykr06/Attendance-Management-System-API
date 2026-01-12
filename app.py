from flask import Flask
from routes.subject_routes import attendance_bp
app = Flask(__name__)
app.register_blueprint(attendance_bp)
if __name__ == '__main__':
    app.run(debug=True)