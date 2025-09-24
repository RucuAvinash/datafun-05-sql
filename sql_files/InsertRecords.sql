-- Insert records into the authors table

INSERT INTO authors (author_id, first_name, last_name, birth_year, nationality)
VALUES
    ('AUTH_01', 'Isaac', 'Asimov', 1920, 'American'),
    ('AUTH_02', 'Agatha', 'Christie', 1890, 'British'),
    ('AUTH_03', 'George', 'Orwell', 1903, 'British'),
    ('AUTH_04', 'Toni', 'Morrison', 1931, 'American'),
    ('AUTH_05', 'Gabriel', 'García Márquez', 1927, 'Colombian'),
    ('AUTH_06', 'Jane', 'Austen', 1775, 'British');

-- Insert records into the books table
INSERT INTO books (book_id, title, ISBN, published_year, author_id)
VALUES
    ('B_01', 'Foundation', 9780553805374, 1951, 'AUTH_01'),
    ('B_02', 'I, Robot', 9780553803714, 1950, 'AUTH_01'),
    ('B_03', 'Murder on the Orient Express', 9780007119318, 1934, 'AUTH_02'),
    ('B_04', '1984', 9780451524935, 1949, 'AUTH_03'),
    ('B_05', 'Beloved', 9781400033420, 1987, 'AUTH_04'),
    ('B_06', 'One Hundred Years of Solitude', 9780060883287, 1967, 'AUTH_05'),
    ('B_07', 'Pride and Prejudice', 9780141439518, 1813, 'AUTH_06');