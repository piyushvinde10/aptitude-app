import os
from dotenv import load_dotenv
load_dotenv()

from app import create_app, db, bcrypt
from app.models import User

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Database tables created!")

        admin_exists = User.query.filter_by(
            email=os.environ.get('ADMIN_EMAIL')).first()
        if not admin_exists:
            hashed = bcrypt.generate_password_hash(
                os.environ.get('ADMIN_PASSWORD')).decode('utf-8')
            admin = User(
                username=os.environ.get('ADMIN_USERNAME'),
                email=os.environ.get('ADMIN_EMAIL'),
                password=hashed,
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin created from .env!")
        else:
            print("ℹ️  Admin already exists.")

    app.run(debug=True)


