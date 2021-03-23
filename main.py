import os

from app import create_app
from config import APP_ENV

app = create_app()
port = os.environ.get('PORT', os.environ.get('API_PORT'))

if __name__ == '__main__':
    app.debug = APP_ENV
    app.run(host='0.0.0.0', port=port)
