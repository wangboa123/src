
drop database blog;
create database blog;

use blog;

drop table test;
create table test(id int auto_increment primary key,user_name char(128) not null,passwd char(128) not null,user_job char(128) not null);

drop table login;
create table login(id int auto_increment primary key,user_name char(128) not null,passwd char(128) not null,user_job char(128) not null);
insert into login(user_name,passwd,user_job) values('wangke','123','teacher')
	