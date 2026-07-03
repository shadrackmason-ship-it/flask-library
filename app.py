from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# PostgreSQL connection
# username = postgres
# password = 1234  (set this in postgres first)
# database = library_db

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost/library_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize database
db = SQLAlchemy(app)

# initialize migrations
migrate = Migrate(app, db)

# import models after db creation
from models import Member, Book, BorrowedBook


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Show all members
@app.route("/members")
def members():

    all_members = Member.query.all()

    return render_template(
        "members.html",
        members=all_members
    )


# Show all books
@app.route("/books")
def books():

    all_books = Book.query.all()

    return render_template(
        "books.html",
        books=all_books
    )


# Run application
if __name__ == "__main__":
    app.run(debug=True)
