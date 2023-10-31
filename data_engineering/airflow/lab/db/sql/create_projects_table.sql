-- Creates a new projects table
CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    begin_date text,
    end_date text
);