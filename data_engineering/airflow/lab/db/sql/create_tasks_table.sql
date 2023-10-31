--  Creates a new tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    priority integer,
    status_id integer NOT NULL,
    project_id integer NOT NULL,
    begin_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);