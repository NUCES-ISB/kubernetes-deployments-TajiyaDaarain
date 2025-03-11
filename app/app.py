from flask import Flask
import psycopg2

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="flaskdb",
            user="flaskuser",
            password="flaskpass",
            host="postgres-service",
            port="5432"
        )
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

@app.route('/')
def home():
    return connect_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
