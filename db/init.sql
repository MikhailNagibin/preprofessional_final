create table tests (
id serial primary key unique,
adres_testa varchar(255)
);

create table tails (
id serial unique,
test_id int,
nomer_taila int,
nomer_massiva int,
data int
);

create table coords (
test_id int,
lestner_x int,
listner_y int,
sendner_x int,
sendner_y int,
price_cuper int,
price_engel int
);



