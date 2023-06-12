-- Author: Group 3
-- Date: 2023-06-09
-- Description: SQL dump for Group 3

-- create database for sql dump
DROP DATABASE IF EXISTS 'group3';
CREATE DATABASE IF NOT EXISTS 'group3';
USE 'group3';

-- create tables
-- user
CREATE TABLE IF NOT EXISTS user(
  user_id INT(3) NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(25) NOT NULL,
  middle_initial VARCHAR(2), 
  last_name VARCHAR(25) NOT NULL,
  email_address VARCHAR(50) NOT NULL,
  CONSTRAINT user_id_pk PRIMARY KEY(user_id)
);
-- group
CREATE TABLE groups(
  group_id INT(3) NOT NULL AUTO_INCREMENT,
  group_name VARCHAR(30) NOT NULL,
  no_of_group_members INT(3) NOT NULL,
  CONSTRAINT group_id_pk PRIMARY KEY(group_id)	
  );
-- group members
CREATE TABLE group_members (
    group_member_id INT(10) NOT NULL AUTO_INCREMENT,
	group_id INT(3) NOT NULL,
	user_id INT(3) NOT NULL,
	group_name VARCHAR(30) NOT NULL,
    CONSTRAINT group_member_id_pk PRIMARY KEY(group_member_id)	
  );
-- expenses
CREATE TABLE expense(
	expense_id INT(10) NOT NULL AUTO_INCREMENT,
	group_id INT(3) NOT NULL,
	date_incurred DATE NOT NULL,
    expense_payor_first_name VARCHAR(30) NOT NULL,
    expense_payor_id INT(3) NOT NULL,
	total_amount DECIMAL(10, 2) NOT NULL, 
	is_settled VARCHAR(15) NOT NULL,
	CONSTRAINT expense_id_pk PRIMARY KEY(expense_id)
  );
-- payments
CREATE TABLE payment(
	payment_id INT(10) NOT NULL AUTO_INCREMENT,
	expense_id INT(10) NOT NULL,
	user_id INT(3) NOT NULL,
    expense_payor_first_name VARCHAR(30) NOT NULL,
    expense_payor VARCHAR(30),
    expense_payor_id INT(10) NOT NULL,
	amount_to_be_paid DECIMAL(10,2) NOT NULL, 
	is_settled VARCHAR(15) NOT NULL,
	CONSTRAINT payment_id_pk PRIMARY KEY(payment_id),
    CONSTRAINT payment_user_id_fk FOREIGN KEY(user_id) REFERENCES user(user_id)
  );

-- dummy data
-- user
INSERT INTO user (user_id, first_name, middle_initial, last_name, email_address)
VALUES
(1, 'Chad', 'A', 'Enriquez', 'chad.enriquez@gmail.com'),
(2, 'Ryan', 'G', 'Villacorte', 'ryan.villacorte@gmail.com'),
(3, 'Genevieve', 'D', 'Penes', 'genevieve.penes@gmail.com');

--groups
INSERT INTO groups (group_id, group_name, no_of_group_members)
VALUES
(100, 'Group1', 3),
(101, 'Group2', 2),
(102, 'Group3', 4);

--group members
INSERT INTO group_members (group_member_id, group_id, user_id, group_name)
VALUES	
(300, 100, 2, 'Group 2'),
(301, 100, 3, 'Group 2'),
(302, 100, 1, 'Group 2'),
(303, 101, 2, 'Group 1'),
(304, 101, 3, 'Group 1'),
(305, 101, 1, 'Group 1'),
(306, 102, 2, 'Group 3'),
(307, 102, 3, 'Group 3'),
(308, 102, 1, 'Group 3');

--expense 
INSERT INTO expense (expense_id, group_id, date_incurred, expense_payor_first_name,  expense_payor_id, total_amount, is_settled)
VALUES
(1000, 100, '2023-05-01', 'Chad', 1, 500.00, 'No'),
(1001, 102, '2023-04-30', 'Ryan', 2, 1000.00, 'Yes'),
(1002, 101, '2023-05-10', 'Genevieve', 3, 750.00, 'No');

--payment
INSERT INTO payment(payment_id, expense_id, user_id, expense_payor_first_name, expense_payor_id, amount_to_be_paid, is_settled)
VALUES
(5000, 1002, 2, 'John', 4, 500, 'No'),
(5001, 1001, 3, 'Janna', 5, 800, 'Yes'),
(5002, 1000, 1, 'Jane', 6, 600, 'Yes');