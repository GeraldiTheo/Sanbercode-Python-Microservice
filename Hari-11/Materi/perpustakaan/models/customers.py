from mysql.connector import connect

class database:
    def __init__(self):
        try:
            self.db = connect(host='localhost',
                              database='perpustakaan',
                              user='geraldi',
                              password='geraldi')
        except Exception as e:
            print(e)
    
    def showUsers(self):
        try:
            query = " SELECT * FROM customers "
            
            cursor = self.db.cursor()
            cursor.execute(query)
            
            data = cursor.fetchall() 
            
            return data
            
        except Exception as e:
            print(e)
    
    def showUserById(self, **params):
        try:
            
            userid = params['userid']
            
            query = " SELECT * FROM customers WHERE userid = {}  LIMIT 1".format(userid)
            
            cursor = self.db.cursor()
            cursor.execute(query)
            
            data = cursor.fetchall() 
            
            return data[0]
            
        except Exception as e:
            print(e)
    
    def insertUser(self, **params):
        try:
            column = ', '.join(list(params['values'].keys()))
            values = tuple(list(params['values'].values()))
            crud_query = '''insert into customers ({0}) values {1};'''.format(column, values)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def updateUserById(self, **params):
        try:
            userid = params['userid']
            values = self.restructureParams(**params['values'])
            crud_query = '''update customers set {0} where userid = {1};'''.format(values, userid)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def deleteUserById(self, **params):
        try:
            userid = params['userid']
            crud_query = '''delete from customers where userid = {0};'''.format(userid)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
    
    def dataCommit(self):
        self.db.commit()
        
    def restructureParams(self, **data):
        list_data = ['{0} = "{1}"'.format(item[0],item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result