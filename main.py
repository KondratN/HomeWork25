# create database mycars;
# use mycars;
# create table car
# (
#     id int primary key auto_increment,
#     stamp varchar(20) not null,
#     country varchar(20) null,
#     year int not null,
#     engine int null,
#     price int not null,
#     color varchar(20) null
# );
# insert into car (stamp, country, year, engine, price, color)
# values ('BMW', null, 2020, 3.5, 20000, 'black'),
#        ('Toyota', 'Japan', 2021, 5.5,35000,null),
#        ('Ford','USA', 2019, null,45000,'white'),
#        ('Mercedes-benz', 'Germany', 2023, 4.5, 50000, null),
#        ('Geely', null, 2020, 1.6, 21000, 'red'),
#        ('Audi', 'Germany', 2023, null, 40000, 'yellow'),
#        ('Tesla', 'USA', 2019, null, 60000, 'white'),
#        ('Porsche', null, 2018, 5.5, 70000, 'black'),
#        ('Renault', 'France', 2023, 1.6, 20000, null),
#        ('Lynk', 'China', 2024, null, 350000, 'white');
#
# select stamp, country, color
# from car
# where year > 2020
# order by stamp desc ;
#
# select count(*) as stamp_count
# from car
# where stamp = 'Tesla';