"""
This file is used to initialize the database.
"""

class DatabaseInitializer:
    """
    Database initializer.    
    """

    def __init__(self):
        """
        Constructor.
        """

        pass

    def sqlDropUsers(self) -> str:
        """
        Drop the `users` table.
        """
    
        return "drop table if exists `users`;"
    
    def sqlDropProducts(self) -> str:
        """
        Drop the `products` table.
        """
    
        return "drop table if exists `products`;"
    
    def sqlDropPrices(self) -> str:
        """
        Drop the `prices` table.
        """
    
        return "drop table if exists `prices`;"
    
    def sqlDropSubscriptions(self) -> str:
        """
        Drop the `subscriptions` table.
        """
    
        return "drop table if exists `subscriptions`;"
    
    def sqlCreateUsers(self) -> str:
        """
        Create the `users` table.
        """
    
        return """
            create table `users` (
                `user_id` int not null auto_increment,
                `user_name` varchar(63) unique not null,
                `password` varchar(63) not null,
                `email` varchar(255) unique not null,
                `create_time` timestamp not null,
                primary key (`user_id`)
            ) engine=InnoDB charset=utf8mb4;
        """
    
    def sqlCreateProducts(self) -> str:
        """
        Create the `products` table.
        """

        return """
            create table `products` (
                `product_id` int not null auto_increment,
                `product_name` varchar(63) not null,
                `category` varchar(63) default null,
                `description` varchar(255) default null,
                `scale` varchar(63) default null,
                `image` varchar(255) default null,
                `platform` varchar(15) default null,
                primary key (`product_id`)
            ) engine=InnoDB charset=utf8mb4;
        """
    
    def sqlCreatePrices(self) -> str:
        """
        Create the `prices` table.
        """

        return """
            create table `prices` (
                `product_id` int not null,
                `price` decimal(10,2) not null default 0.00,
                `checkpoint` timestamp not null,
                primary key (`product_id`, `checkpoint`),
                foreign key (`product_id`) references products(`product_id`)
            ) engine=InnoDB charset=utf8mb4;
        """
    
    def sqlCreateSubscriptions(self) -> str:
        """
        Create the `subscriptions` table.
        """

        return """
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
        """

if __name__ == '__main__':
    initializer = DatabaseInitializer()
    print(initializer.sqlDropUsers())
    print(initializer.sqlDropPrices())
    print(initializer.sqlDropProducts())
    print(initializer.sqlDropSubscriptions())
    print(initializer.sqlCreateUsers())
    print(initializer.sqlCreateProducts())
    print(initializer.sqlCreatePrices())
    print(initializer.sqlCreateSubscriptions())