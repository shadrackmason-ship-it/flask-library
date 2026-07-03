from app import app, db
from models import Member, Book


with app.app_context():

    # Optional: clear old data so duplicates don't pile up
    Member.query.delete()
    Book.query.delete()

    # Create members
    member1 = Member(
        full_name="Mason Rakita",
        email="mason@gmail.com",
        phone="0712345678"
    )

    member2 = Member(
        full_name="John Kamau",
        email="john@gmail.com",
        phone="0799999999"
    )

    # Create books
    book1 = Book(
        title=" Python Programming",
        author="Ali Khan",
        year=2025
    )

    book2 = Book(
        title="Flask Development",
        author="Miguel Grinberg",
        year=2024
    )

    # Add to database
    db.session.add(member1)
    db.session.add(member2)

    db.session.add(book1)
    db.session.add(book2)

    db.session.commit()

    print("Database seeded successfully")