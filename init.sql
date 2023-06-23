CREATE SCHEMA IF NOT EXISTS pointhub;

CREATE TABLE IF NOT EXISTS pointhub.player (
    id SERIAL PRIMARY KEY,
    oauth_id VARCHAR(255),
    points INT DEFAULT 0,
    points_per_click INT DEFAULT 1,
    items JSON
);
