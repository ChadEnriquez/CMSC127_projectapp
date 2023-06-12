-- Author: Group 3
-- Date: 2023-06-09
-- Description: SQL dump for Group 3

-- create database for sql dump
DROP DATABASE IF EXISTS group3;
CREATE DATABASE IF NOT EXISTS group3;
USE 'group3';

-- create tables
-- user
DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user(
  user_id INT(3) NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(25) NOT NULL,
  middle_initial VARCHAR(2), 
  last_name VARCHAR(25) NOT NULL,
  email_address VARCHAR(50) NOT NULL,
  CONSTRAINT user_id_pk PRIMARY KEY(user_id)
);
-- group
DROP TABLE IF EXISTS group;
CREATE TABLE IF NOT EXISTS groups(
  group_id INT(3) NOT NULL AUTO_INCREMENT,
  group_name VARCHAR(30) NOT NULL,
  no_of_group_members INT(3) NOT NULL,
  CONSTRAINT group_id_pk PRIMARY KEY(group_id)	
);
-- group members
DROP TABLE IF EXISTS group_members;
CREATE TABLE IF NOT EXISTS group_members (
  group_member_id INT(10) NOT NULL AUTO_INCREMENT,
	user_id INT(3) NOT NULL,
	first_name VARCHAR(25) NOT NULL,
	group_name VARCHAR(30) NOT NULL,
	group_id INT(3) NOT NULL,
  CONSTRAINT group_member_id_pk PRIMARY KEY(group_member_id)
);
-- expenses
DROP TABLE IF EXISTS expense;
CREATE TABLE IF NOT EXISTS expense(
	expense_id INT(10) NOT NULL AUTO_INCREMENT,
	date_incurred DATE NOT NULL,
  expense_payor_first_name VARCHAR(30) NOT NULL,
  user_id INT(3) NOT NULL,
	total_amount DECIMAL(10, 2) NOT NULL, 
	is_settled VARCHAR(15) NOT NULL,
	group_id INT(3) NOT NULL,
	CONSTRAINT expense_id_pk PRIMARY KEY(expense_id)
);
-- payments
DROP TABLE IF EXISTS payment;
CREATE TABLE IF NOT EXISTS payment(
	payment_id INT(10) NOT NULL AUTO_INCREMENT,
	expense_id INT(10) NOT NULL,
  expense_payor_first_name VARCHAR(30) NOT NULL,
	amount_to_be_paid DECIMAL(10,2) NOT NULL, 
	is_settled VARCHAR(15) NOT NULL,
	CONSTRAINT payment_id_pk PRIMARY KEY(payment_id)
);

--DUMMY DATA
/*
User: Ariel (1)

Friends:
–group1: comsci
Chad (2)
Ryan (3)
Genevieve (4)
Ariel

–group2: divergent
Tris (5)
Four (6)
Ariel

–group3: avengers
Ariel
Tony (7)
Steve (8)
Natasha (9)
Clint (10)

–group4: pink
Barbie (11)
Ken (12)
Ariel

–group5: potter
Ariel
Hermione (13)
Ron (14)
Harry (15)


–friend1: tangled
Ariel
Rapunzel (16)

–friend2: aladdin
Ariel
Jasmine (17)

–friend3: brave
Ariel
Merida (18)

–friend4: beauty
Ariel
Belle (19)

–friend5: frozen
Ariel 
Elsa (20)

*/

--users
INSERT INTO user(user_id, first_name, middle_initial, last_name, email_address) VALUES
	(1, 'Ariel', 'A.', 'Alvarez', 'aaalvarez@gmail.com'),
	(2, 'Chad', 'A.', 'Enriquez', 'caenriquez@gmail.com'),
	(3, 'Ryan', 'G.', 'Villacorte', 'rgvillacorte@gmail.com'),
	(4, 'Genevieve', 'D.', 'Penes', 'gdpenes@gmail.com'),
	(5, 'Tris', 'T.', 'Torres', 'tttorres@gmail.com'),
	(6, 'Four', 'F.', 'Ferrer', 'ffferrer@gmail.com'),
	(7, 'Tony', 'T.', 'Tambunting', 'tttambunting@yahoo.com'),
	(8, 'Steve', 'S.', 'Suarez', 'sssuarez@gmail.com'),
	(9, 'Natasha', 'N.', 'Nacua', 'nnnacua@gmail.com'),
	(10, 'Clint', 'C.', 'Concepcion', 'ccconcepcion@gmail.com'),
	(11, 'Barbie', 'B.', 'Buenaventura', 'bbbuenaventura@gmail.com'),
	(12, 'Ken', 'K.', 'Kabigting', 'kkkabigting@hotmail.com'),
	(13, 'Hermione', 'H.', 'Hernandez', 'hhhernandez@gmail.com'),
	(14, 'Ron', 'R.', 'Rodriguez', 'rrrodriguez@gmail.com'),
	(15, 'Harry', 'H.', 'Herrera', 'hhherrera@gmail.com'),
	(16, 'Rapunzel', 'R.', 'Reyes', 'rrreyes@gmail.com'),
	(17, 'Jasmine', 'J.', 'Jacinto', 'jjjacinto@gmail.com'),
	(18, 'Merida', 'M.', 'Magdangal', 'mmmagdangal@icloud.com'),
	(19, 'Belle', 'B.', 'Buenaflor', 'bbbuenaflor@gmail.com'),
	(20, 'Elsa', 'E.', 'Evangelista', 'eeevangelista@gmail.com');


--groups
INSERT INTO groups (group_id, group_name, no_of_group_members) VALUES
	(111, 'comsci', 4),
	(112, 'divergent', 3),
	(113, 'avengers', 5),
	(114, 'pink', 3),
	(115, 'potter', 4),
	(116, 'tangled', 2),
	(117, 'aladdin', 2),
	(118, 'brave', 2),
	(119, 'beauty', 2),
	(120, 'frozen', 2);


--group members
INSERT INTO group_members (group_member_id, user_id, first_name, group_name, group_id) VALUES
	(2111, 1, 'Ariel',  'comsci', 111),
	(2112, 2, 'Chad',  'comsci', 111),
	(2113, 3, 'Ryan',  'comsci', 111),
	(2114, 4, 'Genevieve',  'comsci', 111),
	(2221, 1, 'Ariel',  'divergent', 112),
	(2222, 5, 'Tris',  'divergent', 112),
	(2223, 6, 'Four',  'divergent', 112),
	(2331, 1, 'Ariel',  'avengers', 113),
	(2332, 7, 'Tony',  'avengers', 113),
	(2333, 8, 'Steve',  'avengers', 113),
	(2334, 9, 'Natasha',  'avengers', 113),
	(2335, 10, 'Clint',  'avengers', 113),
	(2441, 1, 'Ariel',  'pink', 114),
	(2442, 11, 'Barbie',  'pink', 114),
	(2443, 12, 'Ken',  'pink', 114),
	(2551, 1, 'Ariel',  'potter', 115),
	(2552, 13, 'Hermione',  'potter', 115),
	(2553, 14, 'Ron',  'potter', 115),
	(2554, 15, 'Harry',  'potter', 115),
	(2661, 1, 'Ariel',  'tangled', 116),
	(2662, 16, 'Rapunzel',  'tangled', 116),
	(2771, 1, 'Ariel',  'aladdin', 117),
	(2772, 17, 'Jasmine',  'aladdin', 117),
	(2881, 1, 'Ariel',  'brave', 118),
	(2882, 18, 'Merida',  'brave', 118),
	(2991, 1, 'Ariel',  'beauty', 119),
	(2992, 19, 'Belle',  'beauty', 119),
	(3001, 1, 'Ariel',  'frozen', 120),
	(3002, 20, 'Elsa',  'frozen', 120);
		


--expense 
INSERT INTO expense (expense_id, date_incurred, expense_payor_first_name,  user_id, total_amount, is_settled, group_id) VALUES
	(123456, '2023-01-14', 'Ryan', 3, 1076.00, 'Yes', 111),
	(123457, '2023-01-30', 'Jasmine', 17, 394.00, 'No', 117),
	(123458, '2023-02-04', 'Tris', 5, 1368.00, 'No', 112),
	(123459, '2023-02-22', 'Hermione', 13, 1472.00, 'No', 115), 
	(123460, '2023-03-10', 'Barbie', 11, 2217.00, 'No', 114), 
	(123461, '2023-03-28', 'Elsa', 20, 2292.00, 'No', 120), 
	(123462, '2023-04-07', 'Chad', 2, 1852.00, 'No', 111),
	(123463, '2023-04-17', 'Tony', 7, 3435.00, 'No', 113), 
	(123464, '2023-04-29', 'Belle', 19, 594.00, 'No', 119), 
	(123465, '2023-05-11', 'Natasha', 9, 1495.00, 'Yes', 113), 
	(123466, '2023-05-19', 'Merida', 18, 940.00, 'No', 118), 
	(123467, '2023-06-06', 'Rapunzel', 16, 1384.00, 'No', 116);



--payment
INSERT INTO payment(payment_id, expense_id, expense_payor_first_name, amount_to_be_paid, is_settled) VALUES
	(678910, 123457, 'Jasmine', 197, 'Yes'),
	(678911, 123458, 'Tris', 300, 'No'),
	(678912, 123459, 'Hermione', 368, 'Yes'),
	(678913, 123460, 'Barbie', 739, 'Yes'),
	(678914, 123463, 'Tony', 200, 'No'),
	(678915, 123464, 'Belle', 297, 'Yes');
