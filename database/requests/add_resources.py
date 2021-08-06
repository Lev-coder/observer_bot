from database.database import Database
from database.tables.resources import Resurces

class AddResources:

    def __init__(self,link,last_modified):
        self.link = link
        self.last_modified = last_modified

    def start(self):
        database = Database()

        self.databaseName = database.getDatabaseName()
        self.cursor = database.getCursor()
        self.resourceTable= Resurces.getTableName()

        self.addResource(self.link,self.last_modified)

        Database.saveChange()

    def addResource(self):
        return self.cursor.execute(self.sqlCommand())

    def sqlCommand(self):
        return f""" 
        INSERT INTO {self.databaseName}.{self.userTable}(link,last_modified) 
        VALUES ({self.link},{self.last_modified})
        """
