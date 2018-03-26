CREATE DATABASE 
	`libro`
	default charset utf8
	collate utf8_general_ci;

use `libro`;

CREATE table `autors`(
	`id` int not null auto_increment,
	`name` varchar(255) not null,
	primary key(`id`))
	ENGINE=InnoDB;

CREATE table `book`(
	`id` int not null auto_increment,
	`name` varchar(255) not null,
	`autor_id` int not null,
	primary key(`id`))
	ENGINE=InnoDB;

CREATE table `genres`(
	`id` int not null auto_increment,
	`name` varchar(255) not null,

	primary key(`id`))
	ENGINE=InnoDB;

INSERT INTO `autors`(`name`)
VALUES ('Ali', 'Frank', 'Goul', 'Juan', 'Juan', 'Don');

--один ко многим
alter table `book`
add foreign key(`autors_id`)
references `autors`(`id`) 
on delete cascade;

--многие ко многим
CREATE table `boog_genres`(
	`book_id` int not null,
	`genre_id` int not null,
	foreign key (`book_id`) references `book`(`id`) on delete cascade,
	foreign key (`genre_id`) references `genres`(`id`) on delete cascade
		)ENGINE=InnoDB