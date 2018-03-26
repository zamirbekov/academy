create database `onetoone` default charset utf8
collate utf8_general_ci;

use `onetoone`;

create table `users`(
	`id` int not null auto_increment,
	`login` varchar(100) not null,
	`pass` varchar(100) not null,
	primary key(`id`)
	)engine=InnoDB;

create table `profile`(
	`id` int not null unique,
	`first_name` varchar(100) not null,
	`last_name` varchar(100) not null,
	foreign key(`id`) references `users`(`id`)
	)engine=InnoDB;

insert into `users` (`login`, `pass`) 
	values(
	"user1", "passsss"),
	"user2", "pass2"),
	"user3", "pas3");

insert into `profile` (`id`,`first_name`, `last_name`) 
	values(	1,"user", "userbekovich"),
	2,"usergul", "userbekovna"),
	3,"userbek", "userbekov");

select avr(age) age, min(age) as min, max(age) as max from accounts;

select id, avg(age) as age, first_name from accounts groub by id having age>60; --group by - kogda dve stolbsy gruppiruet po ih svyazke

select * from accounts where age>50 order by first_name asc limit 3; 



