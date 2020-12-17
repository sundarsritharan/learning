#exception handling 

try:
    with open('my_file.txt') as fs:
        file_data = fs.read()
    print(file_data)
except FileNotFoundError:
    print('Error: The data file is missing.')
except PermissionError:
    print("Error: You don't have permission to access data file.")
except Exception as err:
    print('oops :-( something went wrong.')

"""
def myfunc(*args):
    for a in args:
        print(a, sep='->',end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k,v in kwargs.items():
        print(k,v,sep='->',end=' ')
    if kwargs:
        print()

myfunc('sundar','priya','diya','nidhi')
#my_family = {,,}
myfunc2(hus = 'sundar',wife = 'priya',daug1 = 'diya',daug2 = 'nidhi')
myfunc2()
myfunc()

# nested functions returning inner function 
def outer() -> None:
    # function returning another function """ """ 
    def inner() -> None:
       #inner function """  """ 
        print('This is inner function.')
    
    print('This is outer function. Retruning inner function.')
    return inner

i = outer()
print(type(i))
i()


# nested functions example
def outer() -> None:
    # an example outer function """ """ 
    def inner() -> None:
        print('This is inner function. ')
    
    print('This is outer function.Invoking inner function.')
    inner()

outer()

# a simple function that invokes another function 
#show how you can pass a function as arugument to another function and invoke it.  

def apply(func: object, value: object) -> object:
    # invoke the input function 
    return func(value)

apply(print,4)
print(apply(id,4))
print(apply(type,42))
print(apply(len,'Marvin'))
print(apply(type,apply))



# commands for mysql connection

mysql -u root -p 
# connnec to mysql command line


sudo /usr/local/mysql/support-files/mysql.server start
sudo /usr/local/mysql/support-files/mysql.server stop
sudo /usr/local/mysql/support-files/mysql.server restart

"""

@app.route('/viewlogs')
@check_logged_in
def view_the_log() -> 'html':
    
    try:
    
        """ view the logs of request and response """
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """ select phrase,letters,ip,browser_string,results from log """
            cursor.execute(_SQL)
            contents = cursor.fetchall()

            # Hard coded titles
            titles = ('Phrase','Letters','Remote_addr','User_agent','Results')
        
            return render_template('viewlog.html',
                                the_title='View Log',
                                the_row_titles=titles,
                                the_data=contents,)
    
    except mysql.connector.errors.InterfaceError as err:
        print('Is your database switched on? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))



import mysql.connector

""" Empty class to implement custom exception """
class ConnectionError(Exception):
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