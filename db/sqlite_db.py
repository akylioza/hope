import sqlite3


def sql_start():
    global base, cursor
    base = sqlite3.connect('db.sqlite3')
    cursor = base.cursor()
    if base:
        print('Database connected')

        base.execute(
            'CREATE TABLE IF NOT EXISTS item(item_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT , photo TEXT, price TEXT, category TEXT, FOREIGN KEY(category) REFERENCES course(category_id))'
        )
        base.execute(
            'CREATE TABLE IF NOT EXISTS category(category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT)'
        )
        base.execute(
            'CREATE TABLE IF NOT EXISTS comments(comment_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, grade TEXT, text TEXT)'
        )
        base.commit()



async def sql_delete_item(data):
    cursor.execute("DELETE FROM item WHERE item_id == ?", (data, ))
    base.commit()



async def sql_add_command(state, table):

    if table == 'item':
        insert_query = f'INSERT INTO {table} VALUES (?, ?, ?, ?, ?)'
        
    elif table == 'category':
        insert_query = f'INSERT INTO {table} VALUES (?, ?)'
    
    elif table == 'comments':
        insert_query = f'INSERT INTO {table} VALUES (?, ?, ?)'

    async with state.proxy() as data:
        cursor.execute(
            insert_query, (None, *data.values())
        )

        base.commit()

