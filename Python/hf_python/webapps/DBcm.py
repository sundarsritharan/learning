import mysql.connector

""" Empty classes to implement custom exceptions """

class ConnectionError(Exception):
    pass

class CredentialError(Exception):
    pass

class SQLError(Exception):
    pass


class UseDatabase:
    """ Module to manage MySQL context for the web app """ 

    def __init__(self, config: dict ) -> None:
        """ Initialize the class """ 
        self.configuration = config

    def __enter__(self) -> 'cursor':

        try:
            """ Setup method for the DB context management """ 
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor =  self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialError(err)

    def __exit__(self, exec_type, exec_value, exec_trace) -> None:
         """ Tear down method for the DB context management """ 
         # commit database changes
         self.conn.commit()
         # close the cursor 
         self.cursor.close()
         #close the connection
         self.conn.close()

         if exec_type is mysql.connector.ProgrammingError:
             raise SQLError(exec_value)
         elif exec_type:
            raise exec_type(exec_value)