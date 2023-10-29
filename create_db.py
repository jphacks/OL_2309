import sqlite3

def create_userdb():
    db_name = 'User.db'
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user_table (id INTEGER PRIMARY KEY AUTOINCREMENT,\
        line_url STRING, instagram_url STRING, twitter_url STRING, facebook_url STRING, tiktok_url STRING);')

    con.commit()

    cur.close()
    con.close()

def main(): 
    create_userdb()

if __name__ == '__main__':
    main()