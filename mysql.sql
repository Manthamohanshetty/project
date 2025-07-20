create database librare;
use librare;

create table librarian(
	book_id int primary key,
    stock int not null,
    available varchar(20)
);

create table student(
	student_id varchar(100) not null,
    book_id int,
    foreign key (book_id) references librarian(book_id)
);