import pypyodbc as odbc # Import the pypyodbc module. pip install pypyodbc

# uid = <username>;
# pwd = <password>;


class Service:
    
    def __init__(self, driverName, serverName, dbName):
        self.connection_string = f'''
                Driver={driverName};
                Server={serverName};
                Database={dbName};
                Trusted_Connection=True;
                '''
        
    def get_connection(self):
        return odbc.connect(self.connection_string)
    
    def get_data(self, query, connection):
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        
    def insert_data(self, query, connection):
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return cursor.rowcount
    
    def close_connection(self, connection):
        connection.close()


