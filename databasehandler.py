import sqlite3
from movies import get_movie_list
class DatabaseHandler:

    def create_table(self,table):#cant use palceholders for table and column names
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                    Original_title text,
                    Original_language text,
                    Genre text,
                    Directors text,
                    Actors text,
                    Date text,
                    Description text
                    )""".format(table))
        self.conn.commit()

    def __init__(self,name):
        self.conn = sqlite3.connect('watched.db')
        self.cursor = self.conn.cursor()
        self.table_name = name
    
    def __enter__(self):
        return self        

    def __exit__(self,exception_type, exception_value, traceback):
        self.conn.commit()
        self.conn.close()

    #takes a request as a dict and stores it in the db
    def store(self,movie):
        values = (movie["Original_title"],movie["Original_language"],movie["Genre"],movie["Directors"],movie["Actors"],movie["Date"],movie["Description"],)
        l = self.cursor.execute("SELECT * FROM {} WHERE Original_title=?".format(self.table_name),(movie["Original_title"],)).fetchall()
        if len(l) > 0:
            return
        else:
            self.cursor.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?)".format(self.table_name),values)

    #takes an ip  and returns all the rows (requests) that came from that ip
    def read_all(self):
        l = self.cursor.execute("SELECT * FROM {}".format(self.table_name)).fetchall()
        return l
    
    def clear_table(self):
        self.cursor.execute("DELETE FROM {}".format(self.table_name))
        self.conn.commit()
    
    def close_connection(self):
        self.conn.commit()
        self.conn.close()

    #prints all the rows in the table
    def print_table(self):
        self.cursor.execute("SELECT * FROM {}".format(self.table_name))
        l = self.cursor.fetchall()
        for movie in l:
            print(movie)
        print("There are {} rows in the {} table".format(str(len(l)),self.table_name))


if __name__ == "__main__":
    with DatabaseHandler('user2') as db:
       movies = db.cursor.execute("SELECT * FROM user2").fetchall()
       m = get_movie_list()[0]
       db.store(m)
       r = db.cursor.execute("SELECT * FROM user2").fetchall()
       print(movies)
       print(r)
