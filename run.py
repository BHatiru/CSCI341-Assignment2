from flaskApp import app, db

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        if db is None:
            db.create_all()
    app.run(debug=True)
