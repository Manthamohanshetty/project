create database score_board;
use score_board;
create table score_entry(
	score int primary key,
    wickets int not null,
    player_name varchar(100),
    runs int not null,
    balls int not null,
    fours int not null,
    sixes int not null,
    Average int not null
);

create table bowlers(
	score int,
	Bowler_name varchar(200),
    no_of_overs int not null,
    no_of_runs int not null,
    no_of_wickets int not null,
    no_of_maidens int not null,
    economy float not null,
    foreign key (score) references score_entry(score)
);
    
    