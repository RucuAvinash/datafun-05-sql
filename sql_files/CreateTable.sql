-- Create the authors table
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,  
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,         
    birth_year INTEGER,         
    nationality TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   
);

-- Create the books table
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,   
    title TEXT NOT NULL,        
    ISBN INTEGER,                
    published_year INTEGER,    
    author_id TEXT,              
    FOREIGN KEY (author_id) REFERENCES authors (author_id) 
);