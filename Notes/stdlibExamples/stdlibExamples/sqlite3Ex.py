import argparse
import sqlite3

def main():
    conn = sqlite3.connect(args.db)
    c = conn.cursor()
    c.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    # save the changes, note the use of conn not c
    conn.commit()
    conn.close()
    
    conn = sqlite3.connect(args.db)
    c = conn.cursor()

    # tell me what is wrong with this next line?
    c.execute("SELECT * FROM stocks WHERE symbol = '{}'".format('RHAT'))
    print(c.fetchone())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('db', help='The name of the db file to connect to.')
    args = parser.parse_args()
    main()