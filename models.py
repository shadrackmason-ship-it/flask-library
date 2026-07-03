from app import db


class Member(db.Model):

    __tablename__ = "members"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(100)
    )

    phone = db.Column(
        db.String(20)
    )

    borrowed = db.relationship(
        "BorrowedBook",
        backref="member"
    )


class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100)
    )

    author = db.Column(
        db.String(100)
    )

    # Added to force second migration
    year = db.Column(
        db.Integer
    )

    borrowed = db.relationship(
        "BorrowedBook",
        backref="book"
    )


class BorrowedBook(db.Model):

    __tablename__ = "borrowed_books"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    member_id = db.Column(
        db.Integer,
        db.ForeignKey("members.id")
    )

    book_id = db.Column(
        db.Integer,
        db.ForeignKey("books.id")
    )

    borrow_date = db.Column(
        db.Date
    )