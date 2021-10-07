create database web;
use web;
CREATE TABLE students (
    id int NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(100),
    email VARCHAR(100),
    batch_title varchar(100),
    date_created  DATETIME DEFAULT   CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);
CREATE TABLE notifications (
    id int NOT NULL AUTO_INCREMENT,
    title VARCHAR(100),
    reference_num VARCHAR(100),
    content varchar(100),
PRIMARY KEY (id)
);
CREATE TABLE timetable (
    id int NOT NULL AUTO_INCREMENT,
    session VARCHAR(100),
    monday VARCHAR(100),
    tuesday VARCHAR(100),
    wednesday VARCHAR(100),
    thursday VARCHAR(100),
    friday VARCHAR(100),
    PRIMARY KEY (id)
    );



insert into students(full_name, email, batch_title) values ('M Raza Khan', 'raza@gmail.com', 'BSCS');
insert into students(full_name, email, batch_title) values ('Azhar Khan', 'azhar@gmail.com', 'BSIT');
insert into students(full_name, email, batch_title) values ('Wateen Khan', 'wateen@gmail.com', 'BSCS');
insert into students(full_name, email, batch_title) values ('Zaheer Khan', 'zaheer@gmail.com', 'BSCS');

