# TODO implement database accessor here
from contextlib import contextmanager
import psycopg2
from psycopg2.extras import DictCursor

DATABASE_NAME = ''

@contextmanager
def session():
    conn = psycopg2.connect(
        database=DATABASE_NAME,
        host='postgresql',
        user='docker',
        port=5432,
        cursor_factory=DictCursor
    )
    conn.set_session(autocommit=True)
    curr = conn.cursor()
    yield curr
    curr.close()
    conn.close()

def register_bet(game_id: int, better_id: str, bettee_id: str, bet_condition: str, bet_amount: int):

    with session() as db:
        try:
            db.execute(
                'INSERT INTO active_bets (game_id, better_id, bettee_id, bet_condtion, bet_amount)\
                    VALUES (%(game_id)d, %(better_id)s, %(bettee_id)s, %(bet_condtion)s, %(bet_amount)d)',
                {'game_id' : game_id, 'better_id': better_id, 'bettee_id': bettee_id, 'bet_condition': bet_condition, 'bet_amount': bet_amount}
            )
            return db.rowcount > 0
        except Exception:
            return False