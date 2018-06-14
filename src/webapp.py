from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
