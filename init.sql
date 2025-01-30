CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (user_name, user_email, user_password) VALUES ('example_user', 'user@example.com', 'password123');

CREATE TABLE IF NOT EXISTS notes (
    note_id INT PRIMARY KEY AUTO_INCREMENT,
    note_name VARCHAR(100),
    note_content TEXT,
    user_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO notes (note_name, note_content, user_id) VALUES ('First Note', 'This is a test note content.', 1);
