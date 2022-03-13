from flask import Flask
from routes import configure_routes
import logging
from config import config

app = Flask(__name__)
configure_routes(app)

logging.basicConfig(filename=config["log_file"], level=config["log_level"])

if __name__ == "__main__":
    app.run(host=config["host"], port=config["port"], debug=True)
