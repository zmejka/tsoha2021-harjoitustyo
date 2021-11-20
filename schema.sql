CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    name TEXT,
    role TEXT
);

CREATE TABLE subject (
    id SERIAL PRIMARY KEY,
    title TEXT UNIQUE,
    description TEXT,
    username_id INT,
    CONSTRAINT pk_user
      FOREIGN KEY(username_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE question (
    id SERIAL PRIMARY KEY,
    question TEXT UNIQUE,
    question_type INT,
    title_id INT,
    answer INT
);

CREATE TABLE answer (
    id SERIAL PRIMARY KEY,
    answer TEXT,
    answer_q BOOLEAN,
    question_id INT
);

INSERT INTO users(username, password, name, role) VALUES ('Testaaja','','Testaaja Nimi','');
