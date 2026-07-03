ALTER TABLE members
RENAME COLUMN name TO full_name;

ALTER TABLE members
ADD COLUMN phone VARCHAR(20);

SELECT * FROM books
ORDER BY title ASC;

SELECT * FROM books
ORDER BY title DESC;