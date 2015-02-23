import sqlite3
import datetime

class AlarmDBException(Exception):
    pass


class AlarmDB(object):
    def __init__(self, dbname='alarmserver.db'):
        self.conn = sqlite3.connect(dbname)
        # CREATE TABLE events(id INT PRIMARY KEY, type TEXT, param INT, code INT, timestamp DATE)
        c = self.conn.cursor()
        try:
            c.execute('''CREATE TABLE
                events(id INT PRIMARY KEY,
                       type TEXT,
                       param INT,
                       code INT,
                       timestamp DATE)
                ''')
        except sqlite3.OperationalError:
            # table already exists
            pass

    def logevent(self, type, param, code):
        c = self.conn.cursor()

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute('''INSERT INTO events(type, param, code, timestamp)
                     VALUES (?,?,?,?)''', (type, param, code, timestamp))
        self.conn.commit()

    def lastevent(self, type, param):
        c = self.conn.cursor()
        c.execute('''SELECT code FROM events WHERE type=? and param=?''', (type, param,))
        data = c.fetchall()

        try:
            code = data[-1][0]
        except IndexError:
            raise AlarmDBException('Table is empty')

        # get last row, first item in tuple
        return code
