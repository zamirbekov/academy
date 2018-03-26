CREATE DATABASE `library`
SET DEFAULT CHARSET utf8
COLLATE utf8_general_ci;

USE `library`;

CREATE TABLE `books`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(100) NOT NULL,
	`author` VARCHAR(100) NOT NULL,
	`genre` VARCHAR(100),
	`year` DATE NOT NULL,
	`ISBN` INT NOT NULL,
	PRIMARY KEY(`id`)	
) ENGINE=InnoDB;

INSERT INTO `books`(`name`, `author`, `genre`, `year`, `ISBN`)
VALUES ('Little Prince', 'Antuan de Sent-Exuperi', 'novel', '1956', 2390100920),
VALUES ('The old man and', 'Ernes Hemingway', 'novel', '1951', 134243234),
VALUES ('Dune', 'Frank Garbert', 'nover', '1800', 234234234),
VALUES ('The Kite Runner', 'Khaled Hosseini', 'novel', '2004', 123424124),
VALUES ('A thousand splendid suns', 'Khaled Hosseini', 'novel', '1996', 114342342),
VALUES ('1984', 'George Orwell', 'dystopia', '1950', 3423423423),
VALUES ('Ten little Niggers', 'Agata Kristi', 'detective', '1980', 234234234);

CREATE TABLE `author`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(100) NOT NULL,
	`born_date` DATE NOT NULL,
	`national` VARCHAR(100),
	PRIMARY KEY(`id`)	
) ENGINE=InnoDB;

INSERT INTO `books`(`name`, `born_date`, `national`)
VALUES ('Khaled Hosseini', '1996-02-25', 'afgan'),
VALUES ('Antuan de Sent-Exuperi', '1900-02-15', 'francian'),
VALUES ('Agata Kristi', '1890-09-23', 'british'),
VALUES ('George Orwell', '1876-12-12', 'americano'),
VALUES ('Ernes Hemingway', '1903-06-03', 'americano'),
VALUES ('Frank Garbert', '1906-06-06', 'german');

CREATE TABLE `genres`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(100) NOT NULL,
	PRIMARY KEY(`id`)	
) ENGINE=InnoDB;

INSERT INTO `genres`(`name`)
VALUES ('detective'),
VALUES ('novel'),
VALUES ('dystopia'),
VALUES ('drama'),
VALUES ('non-fiction'),
VALUES ('fantasy'),
VALUES ('fiction'),
VALUES ('history');