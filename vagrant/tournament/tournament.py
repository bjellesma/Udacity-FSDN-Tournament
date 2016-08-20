#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches;")
    #update player matches to zero
    c.execute("UPDATE players SET matches = 0, wins = 0, loses = 0;")
    db.commit()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players;")
    db.commit()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT count(*) FROM players;")
    results = c.fetchone()
    #if rows are empty (nonetype)
    if results is None:
        return 0
    else:
        return results[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    db.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT id, name, wins, matches FROM players ORDER BY wins DESC;")
    return c.fetchall()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    #you need to use %s even when passing a number
    c.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);", (winner, loser,))
    #update winner and loser
    c.execute("UPDATE players SET matches = matches + 1, wins = wins + 1 WHERE id = (%s);", (winner,))
    c.execute("UPDATE players SET matches = matches + 1, loses = loses + 1 WHERE id = (%s);", (loser,))
    db.commit()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    rows = playerStandings()
    swissPairingsList = []
    #iterate over every two elements in list
    # https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list/5389578#5389578
    for x,y in zip(rows[0::2], rows[1::2]):
        pair = (x[0], x[1], y[0], y[1])
        swissPairingsList.append(pair)
    return swissPairingsList
