CREATE DATABASE 
	`test`
SET DEFAULT CHARSET utf8
COLLATE utf8_general_ci;

USE `test`;

CREATE TABLE `cars`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`model` VARCHAR(20) NOT NULL,
	`year` INT NOT NULL,
	`color` VARCHAR(20),
	`volum` FLOAT NOT NULL,
	`wtf_date` DATE NOT NULL,
	PRIMARY KEY(`id`)	
) ENGINE=InnoDB;

select id, first_name from `users`;

INSERT INTO `cars`(`model`, `year`, `color`, `volum`, `wtf_date`)
VALUES ("PORSHE 911", 2014, 'yellow', 8.4, '2018-02-09');

ALTER TABLE `cars` ADD `owner` VARCHAR(100); --добавить столбец

ALTER TABLE `cars` MODIFY COLUMN model VARCHAR(100); --изменяет кол-во символов

ALTER TABLE `cars` DROP COLUMN `wtf_date`; --удаляет столбец

UPDATE `cars` SET `owner`="Emil" WHERE `id`=1;

SELECT people.name, cars.model from `people` INNER JOIN `cars` ON people.name = cars.owner; --INNER JOIN

