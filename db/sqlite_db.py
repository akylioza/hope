import sqlite3


def sql_start():
    global base, cursor
    base = sqlite3.connect('db.sqlite3')
    cursor = base.cursor()
    if base:
        print('Database connected')
        base.execute(
            'CREATE TABLE IF NOT EXISTS item(name TEXT , photo TEXT, price TEXT, category TEXT)'
        )
        base.commit()


async def sql_add_command(state, table):
    if table == 'item':
        insert_query = f'INSERT INTO {table} VALUES (?, ?, ?, ?)'

    async with state.proxy() as data:
        cursor.execute(
            insert_query, tuple(data.values())
        )
        base.commit()

