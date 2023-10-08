USE news_db;
CREATE TABLE IF NOT EXISTS news_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(512),
    headlines VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS news_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(512),
    url_hash CHAR(36) UNIQUE,
    is_crawled TINYINT(1),
    INDEX idx_url_hash (url_hash)
)