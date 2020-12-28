import sqlite3

#not the best way to handle the database since some of these queries may be vulnerable to sql injections 
class DatabaseHandler:

    def create_table(self,table):#cant use palceholders for table and column names
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                    Original_title text,
                    Original_language text,
                    Genre text,
                    Directors text,
                    Actors text,
                    Date text,
                    Description text,
                    Rating int
                    )""".format(table))
        self.conn.commit()

    def __init__(self,name):
        self.conn = sqlite3.connect('../watched.db')
        self.cursor = self.conn.cursor()
        self.table_name = name
    
    def __enter__(self):
        return self        

    def __exit__(self,exception_type, exception_value, traceback):
        self.conn.commit()
        self.conn.close()

    #takes a movie with its info as a dict and stores it in the db
    def store(self,movie):
        values = (movie["Original_title"].strip(),movie["Original_language"],movie["Genre"],movie["Directors"],movie["Actors"],movie["Date"],movie["Description"],movie["Rating"],)
        l = self.cursor.execute("SELECT * FROM {} WHERE Original_title=?".format(self.table_name),(movie["Original_title"].strip(),)).fetchall()
        if len(l) > 0:
            return
        else:
            self.cursor.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,?)".format(self.table_name),values)

    #returns all the values in the table as a list of dictionaries
    def read_all_rows(self):
        value = []
        l = self.cursor.execute("SELECT * FROM {}".format(self.table_name)).fetchall()
        for movie in l:
             value.append({"Original_title": movie[0],
             "Original_language": movie[1],
             "Genre": movie[2],
             "Directors":movie[3],
             "Actors": movie[4],
             "Date": movie[5],
             "Description":movie[6]})
        return value

    def get_rating(self,title):
        try:
            l = self.cursor.execute("SELECT Rating FROM {} WHERE Original_title=?".format(self.table_name),(title,)).fetchall()
            return l[0]
        except Exception as e:
            print(e)
            return 0
        
    
    #clears the table 
    def clear_table(self):
        self.cursor.execute("DELETE FROM {}".format(self.table_name))
        self.conn.commit()
    
    def close_connection(self):
        self.conn.commit()
        self.conn.close()
    
    def delete_table(self):
        self.cursor.execute("DROP TABLE {}".format(self.table_name))
        self.conn.commit()

    #prints all the rows in the table
    def print_table(self):
        self.cursor.execute("SELECT * FROM {}".format(self.table_name))
        l = self.cursor.fetchall()
        for movie in l:
            print(movie)
        print("There are {} rows in the {} table".format(str(len(l)),self.table_name))

    def show_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(self.cursor.fetchall())


if __name__ == "__main__":
    with DatabaseHandler('user1') as db:
       # db.clear_table()
        r = db.read_all_rows()
        print(r)
        db.show_tables()
