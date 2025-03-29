# Import Flask
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return "Hello_Rakesh"

# Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
