from app import create_app
from app.constants import TEST_PORT
app = create_app()

if __name__ == '__main__':
 app.run(port=TEST_PORT, threaded=True)