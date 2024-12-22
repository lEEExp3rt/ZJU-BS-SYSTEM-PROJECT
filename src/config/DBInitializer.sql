/**
 * This script is used to initialize the database.
 */

create database if not exists `budget_bee` default character set utf8mb4 collate utf8mb4_bin;

drop table if exists `subscriptions`;
drop table if exists `prices`;
drop table if exists `products`;
drop table if exists `users`;

create table `users` (
    `user_id` int not null auto_increment,
    `user_name` varchar(63) unique not null,
    `password` varchar(63) not null,
    `email` varchar(255) unique not null,
    `create_time` timestamp not null,
    primary key (`user_id`)
) engine=InnoDB charset=utf8mb4;

create table `products` (
    `product_id` int not null,
    `product_name` varchar(63) not null,
    `description` varchar(255) default null,
    `url` varchar(255) default null,
    `image` varchar(255) default null,
    `category` varchar(63) default null,
    `scale` varchar(63) default null,
    `platform` varchar(15) default null,
    primary key (`product_id`)
) engine=InnoDB charset=utf8mb4;

create table `prices` (
    `product_id` int not null,
    `price` decimal(10,2) not null default 0.00,
    `checkpoint` timestamp not null,
    primary key (`product_id`, `checkpoint`),
    foreign key (`product_id`) references products(`product_id`)
) engine=InnoDB charset=utf8mb4;

create table `subscriptions` (
    `subscription_id` int not null auto_increment,
    `product_id` int not null,
    `user_id` int not null,
    `timer` time default null,
    `enable` boolean default true,
    primary key (`subscription_id`),
    foreign key (`product_id`) references products(`product_id`),
    foreign key (`user_id`) references users(`user_id`)
) engine=InnoDB charset=utf8mb4;