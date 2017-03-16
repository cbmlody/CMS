DROP TABLE IF EXISTS `USERS`;
DROP TABLE IF EXISTS `ATTENDANCES`;
DROP TABLE IF EXISTS `SUBMISSIONS`;
DROP TABLE IF EXISTS `CHECKPOINTS`;
DROP TABLE IF EXISTS `ROLES`;
DROP TABLE IF EXISTS `TEAMS`;
DROP TABLE IF EXISTS `ASSIGNMENTS`;

CREATE TABLE `USERS` (`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,`login`	TEXT NOT NULL UNIQUE,`password`	TEXT NOT NULL,`full_name`	TEXT NOT NULL,`role_ID`	INTEGER NOT NULL,`team_ID`	INTEGER);

CREATE TABLE `ATTENDANCES` (
	`user_ID`	INTEGER NOT NULL,
	`date`	TEXT NOT NULL,
	`status`	INTEGER NOT NULL
);

CREATE TABLE `SUBMISSIONS` (`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,`user_ID`	INTEGER NOT NULL,`submission_date`	TEXT NOT NULL,`content`	TEXT NOT NULL,`grade`		INTEGER,`assignment_ID`	INTEGER NOT NULL,`team_ID`	INTEGER);

CREATE TABLE `CHECKPOINTS` (`user_ID`	INTEGER NOT NULL UNIQUE,`card`	TEXT NOT NULL);

CREATE TABLE `ROLES` (`ID`	INTEGER NOT NULL UNIQUE,`name`	TEXT NOT NULL);

CREATE TABLE `TEAMS` (`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,`name`	TEXT NOT NULL UNIQUE);

CREATE TABLE `ASSIGNMENTS` (`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,`title`	TEXT NOT NULL UNIQUE,`due_date`	TEXT NOT NULL,`max_points`	INTEGER NOT NULL,`as_team`	INTEGER NOT NULL);

INSERT INTO `USERS`(`ID`,`login`,`password`,`full_name`,`role_ID`,`team_ID`) VALUES (1,'jerzy','1234','Jerzy Mardaus',0,NULL);
INSERT INTO `USERS`(`ID`,`login`,`password`,`full_name`,`role_ID`,`team_ID`) VALUES (2,'kati','1234','Kati Płachecka',2,NULL);
INSERT INTO `USERS`(`ID`,`login`,`password`,`full_name`,`role_ID`,`team_ID`) VALUES (3,'miriam','1234','Miriam Bałazińska',2,NULL);
INSERT INTO `USERS`(`ID`,`login`,`password`,`full_name`,`role_ID`,`team_ID`) VALUES (4,'rafal','1234','Rafał Stępień',1,NULL);
INSERT INTO `USERS`(`ID`,`login`,`password`,`full_name`,`role_ID`,`team_ID`) VALUES (5,'mateusz','1234','Mateusz Ostafil',1,NULL);
INSERT INTO `USERS`(`ID`,`login`,`password`,`full_name`,`role_ID`,`team_ID`) VALUES (6,'endriu','1234','Andrzej Abdcd',3,1);
INSERT INTO `USERS`(`ID`,`login`,`password`,`full_name`,`role_ID`,`team_ID`) VALUES (7,'tomi','1234','Tomasz Kowal',3,NULL);

INSERT INTO `TEAMS`(`ID`,`name`) VALUES (1,'Podgrzybek');

INSERT INTO `ROLES`(`ID`,`name`) VALUES (0,'Manager');
INSERT INTO `ROLES`(`ID`, `name`) VALUES (1, 'Mentor');
INSERT INTO `ROLES`(`ID`, `name`) VALUES (2, 'Employee');
INSERT INTO `ROLES`(`ID`, `name`) VALUES (3, 'Student');

INSERT INTO `ASSIGNMENTS`(`title`,`due_date`,`max_points`,`as_team`) VALUES ('CMS','17-02-2017',72,1);
INSERT INTO `ASSIGNMENTS`(`title`,`due_date`,`max_points`,`as_team`) VALUES ('SMC','26-02-2017',36,0);

INSERT INTO `SUBMISSIONS`(`user_ID`,`submission_date`,`content`,`grade`,`assignment_ID`,`team_ID`) VALUES (6,'16-02-2017','https://github.com/',36,1,1);
INSERT INTO `SUBMISSIONS`(`user_ID`,`submission_date`,`content`,`grade`,`assignment_ID`,`team_ID`) VALUES (6,'19-02-2017','https://github.com/dawda',12,2,1);

INSERT INTO `ATTENDANCES` VALUES (6,'15-02-2017',1);
INSERT INTO `ATTENDANCES` VALUES (7,'15-02-2017',0);

CREATE UNIQUE INDEX `attendance_unique` ON `ATTENDANCES` (`user_ID` ,`date` );
CREATE UNIQUE INDEX `submission_unique` ON `SUBMISSIONS` (`user_ID` ,`assignment_ID` );