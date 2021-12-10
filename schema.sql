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
    answer INT,
    CONSTRAINT pk_title
      FOREIGN KEY(title_id)
        REFERENCES subject(id)
        ON DELETE CASCADE
);

CREATE TABLE answer (
    id SERIAL PRIMARY KEY,
    answer TEXT,
    answer_q BOOLEAN,
    question_id INT
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    title_id INT,
    comment TEXT,
    username_id INT,
    CONSTRAINT pk_title
      FOREIGN KEY(title_id)
        REFERENCES subject(id)
        ON DELETE CASCADE,
    CONSTRAINT pk_user
      FOREIGN KEY(username_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE scores (
    id SERIAL PRIMARY KEY,
    username_id INT,
    title_id INT,
    all_results INT,
    score INT
);

INSERT INTO users(username, password, name, role) VALUES ('Admin','pbkdf2:sha256:260000$QN2wi2NG4k7HWAJg$67e3583372c67eb4dff60e1af4891cdc80fa9dc8e48eabea5f34bd651cf13715','Admin','Admin');
INSERT INTO users(username, password, name, role) VALUES ('Käyttäjä','pbkdf2:sha256:260000$aJaVz4OKPI8btVZN$61205b521c82d5bb231d1694aaafe9f7ef9d653913855bc215d4511055aa98f1','Tomi Testaaja','Ohjaaja');
