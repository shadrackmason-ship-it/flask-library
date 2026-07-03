CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100)
);

CREATE TABLE borrowed_books(
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES members(id),
    book_id INTEGER REFERENCES books(id),
    borrow_date DATE
);