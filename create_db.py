import sqlite3

def create_userdb():
    db_name = 'User.db'
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS user_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        line_url TEXT, 
        instagram_url TEXT, 
        twitter_url TEXT, 
        facebook_url TEXT, 
        tiktok_url TEXT
    );
    ''')

    con.commit()

    cur.close()
    con.close()

def main(): 
    create_userdb()

if __name__ == '__main__':
    main()