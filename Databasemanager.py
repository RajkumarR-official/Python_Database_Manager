# install mysql.connector in terminal  by using < pip install mysql-connector-python > and impoting it
import mysql.connector as dbcon
# install tabulate in terminal < pip install mysql-connector-python > and impoting it
from tabulate import tabulate

print("Connecting to DB......")

con =dbcon.connect(host ="localhost",user="root",password="mysql",database="python")

print ("connected to DB successfully")

print("creating cursor")

cur = con.cursor()


class DB:
    def __init__(self) -> None:
        self.curbatabase="python"
        self.curtablename="student"
    
    # create a database and use this database for performing further sql queries
    def createdatabase(self,databasename,tablename,columnname_datatype):
        sql=f"create database {databasename};"
        sql1 =f"use {databasename};"
        cur.execute(sql)
        cur.execute(sql1)
        sql2=f"create  table {tablename} ({columnname_datatype}); "
        cur.execute(sql2)
        print("table created with colunm and datatype successfully")
        con.commit()
        self.curbatabase=databasename
        self.curtablename = tablename
        print("created a batabase and currently using this database")

    # method to create a table which get arguments like tablename and columnname with datatype, constraints too as string
    def createtable(self,tablename,columnname_datatype):
        sql=f"create table if not exists {tablename}({columnname_datatype}); "
        cur.execute(sql)
        con.commit()
        self.curtablename=tablename
        print("table created with colunm and datatype successfully")
    def insert(self,tablename=None,):
            # 
        if tablename!=None:
            sql=f"show columns from {tablename};"
            cur.execute(sql) 
            res=cur.fetchall()
            coln =','.join([row[0] for row in res])
            value = str(input(f"enter values in coma separated in this format{coln}: "))
            sql=f"insert into {self.curtablename} ({coln}) values({value});"
            cur.execute(sql)
            con.commit()
            self.curtablename=tablename
            print("value inserted successfully")

        else:
            sql=f"show columns from {self.curtablename};"
            cur.execute(sql)
            res=cur.fetchall()
            coln =','.join([row[0] for row in res])
            value = str(input(f"enter coma separated values in this format{coln}: "))
            print(value)
            sql=f"insert into {self.curtablename} ({coln}) values({value});"
            cur.execute(sql)
            con.commit()
            print("value inserted successfully")

    # method to read the table record from currently working with or can give value
    def read(self,tablename=None,database=None):
        if tablename is not None and database is not None:
            sql=f"use {database}"
            sql1=f"select * from {tablename}"
            cur.execute(sql)
            cur.execute(sql1)
            rows = cur.fetchall()
            con.commit()
            print("sucessfully selected table")
        if tablename is not None and database is  None:
            sql=f"select * from {tablename}"
            cur.execute(sql)
            rows = cur.fetchall()
            con.commit()
        if tablename is  None and database is  None:
            sql=f"select * from {self.curtablename}"
            cur.execute(sql)
            rows = cur.fetchall()
            con.commit()

        else:
            True    
        
        # Get column names from the cursor description
        headers = [column[0] for column in cur.description]
        # Print the table using tabulate
        table = tabulate(rows, headers, tablefmt="grid")
        print(table)

    # update method to update values in the table 
    def update(self,tablename=None, databasename=None):
        if databasename is None and tablename is not None:
            cname = str(input("enter the column name and value you want to update like, colunmname = value :  "))
            rname = str(input("enter the condition,to filter records like, colunmname = value :  "))
            sql=f"update  {tablename} set {cname} where {rname};"
            cur.execute(sql)
            print("table updated successfully ")
            con.commit()

        if tablename is not None and databasename is not None:
            cname = str(input("enter the column name and value you want to update like, colunmname = value :  "))
            rname = str(input("enter the condition,to filter records like, colunmname = value :  "))
            sql=f"use {databasename}"
            sql1=f"update  {tablename} set {cname} where {rname};"
            cur.execute(sql)
            cur.execute(sql1)
            print("table updated successfully ")
            con.commit()

        if databasename is None and tablename is  None:
            cname = str(input("enter the column name and value you want to update like, colun_mname = value :  "))
            rname = str(input("enter the condition,to filter records like, colunmname = value :  "))
            sql=f"update  {self.curtablename} set {cname} where {rname};"
            cur.execute(sql)
            print("table updated successfully ")
            con.commit()
        else:
            True
    # delete record from the table
    def delete(self,tablename=None,databasename =None):
        if tablename is not None and databasename is None:
            cname=str(input("Enter the condition to filter records and delete, like column_name =value."))
            sql=f"delete from {tablename} where {cname};"
            cur.execute(sql)
            print("record deleted successfully from the table")
            con.commit()
        
        if tablename is not None and databasename is not None:
            cname=str(input("Enter the condition to filter records and delete, like column_name =value."))
            sql=f"use {databasename}"
            cur.execute(sql)
            sql=f"delete from {tablename} where {cname};"
            cur.execute(sql)
            print("record deleted successfully from the table")
            con.commit()

        if tablename is  None and databasename is  None:
            cname=str(input("Enter the condition to filter records and delete, like column_name =value."))
            sql=f"delete from {self.curtablename} where {cname};"
            cur.execute(sql)
            print("record deleted successfully from the table")
            con.commit()
        
    def customized(self):
        sql =str("Enter a sql query to execute ; ")
        cur.execute(sql)
        rows = cur.fetchall()
        headers =[column[0] for column in cur._description]
        table= tabulate(rows,headers,tablefmt="grid")
        print(table)
    def showtables(self,databasename=None):
        if databasename is not None:
            sql =f"use {databasename};"
            sql1 ="show tables;"
            cur.execute(sql)
            cur.execute(sql1)
            rows=cur.fetchall()
            headers = [column[0] for column in cur.description]
            # Print the table using tabulate
            table = tabulate(rows, headers, tablefmt="grid")
            print(table)
        else:
            sql =f"use {self.curbatabase};"
            sql1 ="show tables;"
            cur.execute(sql)
            cur.execute(sql1)
            rows=cur.fetchall()
            headers = [column[0] for column in cur.description]
            # Print the table using tabulate
            table = tabulate(rows, headers, tablefmt="grid")
            print(table)

    def showdatabases(self):
        sql1 ="show databases;"
        cur.execute(sql1)
        rows=cur.fetchall()
        headers = [column[0] for column in cur.description]
        # Print the table using tabulate
        table = tabulate(rows, headers, tablefmt="grid")
        print(table)


    # options to perform 
    def options(self):
        print('''\n   Choose and enter an option from the list:\n      0 TO EXIT \n      1 TO CREATE A DATABASE AND TABLE  \n      2 TO CREATE A TABLE \n      3 TO INSERT A VALUE TO TABLE \n      4 TO UPDATE  RECORD\n      5 TO READ TABLE \n      6 TO DELETE RECORD FROM TABLE ''')

obj = DB()
try:
    while True:
        obj.options()
        n =int(input("Enter a number :  "))
        if n>-1 and n<7  :
            if n==0:
                break
            if n== 1:
                obj.showdatabases()
                dbn=str(input("enter the  databasename you want to create "))
                tname= str(input("Enter the tablename you want to create"))
                colname= str(input("enter the column_name and its datatype , constraints ( columnname1 datatype1 constraints1,columnname2.............. (if any )) "))
                obj.createdatabase(dbn,tname,colname)      
            if n== 2:
                obj.showtables()
                tname=str(input("enter the table name you want to create"))
                cname=str(input("enter  columnname_datatype in comma separated format"))
                obj.createtable(tname,cname)
            if n== 3:
                sn= int(input(f"choose any one option\n      1 if you want to use active database and its table \n      2 if you want to use different table in the current active database \n      3 if you want to use different database and table   \n      0 to go main options  "))
                if sn==1:
                    obj.read()
                    obj.insert()
                    True

                if sn==2:
                    obj.showtables()
                    tname =str(input("enter a existing table name in this database : "))
                    obj.read(tname)
                    obj.insert(tname)
                    True

                if sn==3:
                    obj.showdatabases()
                    dname =str(input("enter a existing database name : "))
                    obj.showtables(dname)
                    tname =str(input("enter a existing table name in this database : "))
                    obj.insert(tname,dname)
                    True
                else:
                    True
            if n== 5:

                sn= int(input(f'''       choose any one option\n      1 if you want to use active database and its table \n      2 if you want to use different table in the current active database \n      3 if you want to use different database and table that already exist \n      0 to go main options  :  '''))
                
                if sn==1:
                    obj.read()
                    True
                
                if sn==2:
                    obj.showtables()
                    tname =str(input("enter a table name  "))
                    obj.read(tname)
                    True
                if sn==3:
                    obj.showdatabases()
                    dname =str(input("enter a existing  database "))
                    obj.showtables(dname)
                    tname =str(input("enter a existing table name in this database "))
                    obj.read(tname,dname)
                    True
                if sn==0:
                    True    
            if n ==4:
                un= int(input(f'''         choose any one option\n      1 if you want to use active database and its table for updating records \n      2 if you want to use different database and table that already exist for updating records \n      3 to update different table in the active database  \n      0 to main  options:  '''))
                if un == 1:
                    obj.read()
                    obj.update()
                    True
                if un == 2:
                    obj.showdatabases()
                    dname =str(input("enter a existing  database ")) 
                    obj.showtables(dname)                   
                    tname =str(input("enter a existing table name in this database "))
                    obj.read(tname, dname)
                    obj.update(tname,dname)
                    True
                if un == 3:
                   obj.showtables()
                   tname =str(input("enter a existing table name in this database "))
                   obj.read(tname)  
                   obj.update(tname)   
                   True   
                else:
                    True                
            if n== 6:
                dn= int(input(f'''choose any one option\n      1 if you want to use active database and its table for deleting records \n      2 if you want to use different database and  table that already exist.  \n       3 to delete different table records in the active database  \n       0 to main  options'''))
                if dn == 1:
                    obj.read()
                    obj.delete()
                    True
                if dn == 2:
                    obj.showdatabases()
                    dname =str(input("enter a existing  database "))
                    obj.showtables(dname)  
                    tname =str(input("enter a existing table name in this database "))
                    obj.read(tname)
                    obj.delete(tname,dname)
                    True
                if dn == 3:
                    obj.showtables()
                    tname =str(input("enter a existing table name in this database "))
                    obj.read(tname)
                    obj.delete(tname)        
                else:
                    True     
            
            else:
                True
        else:
            True

except Exception as e:
    print("ERROR:  ",e)

con.close()
print("bd closed successfully")