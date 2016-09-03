-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--create a new tournament database
--saves a lot of time in development because the database is always reinstanuated
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

--player table
create table players(
  id serial primary key,
  name text
);

--matches table
--This table must be listed second as it has reference data
create table matches(
  id serial primary key,
  winner_id integer REFERENCES players(id),
  loser_id integer REFERENCES players(id)
);

-- create winscounter view which joins matches and players tables to
-- count the number of wins by player.
CREATE VIEW wincounter
AS
  SELECT players.id,
         players.name,
         COUNT(matches.winner_id) AS wins
  FROM   players
         LEFT JOIN matches
                ON players.id = matches.winner_id
  GROUP  BY players.id;

  -- create losecounter view which joins matches and players tables to
  -- count the number of loses by player.
  CREATE VIEW losecounter
  AS
    SELECT players.id,
           players.name,
           COUNT(matches.loser_id) AS loses
    FROM   players
           LEFT JOIN matches
                  ON players.id = matches.loser_id
    GROUP  BY players.id;

    -- create matchescounter view which joins players tables to wincounter and losecounter view to
    -- count the number of matches by player.
    -- This reduces the number of queries we need to make in python
    CREATE VIEW matchescounter
    AS
      SELECT players.id,
             players.name,
             SUM(wincounter.wins + losecounter.loses) AS matches
      FROM   players
             LEFT JOIN wincounter
                    ON players.id = wincounter.id
              LEFT JOIN losecounter
                     ON players.id = losecounter.id
      GROUP  BY players.id;
