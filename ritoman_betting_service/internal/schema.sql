-- schema.sql
\c rbsdb;

-- TODO create table definitions here
CREATE TABLE IF NOT EXISTS active_bets (
    game_id INT,
    better_id VARCHAR,
    bettee_id VARCHAR,
    bet_condtion VARCHAR,
    bet_amount INT, 
    PRIMARY KEY (game_id, better_id, bettee_id)
)