import os,urllib
server = <database server>
database = <database name>
username = <user name>
password = <password

runenv = os.environ['RUNENV']
if runenv == 'local':
    drivername = 'SQL Server'
else:
    drivername = 'ODBC Driver 17 for SQL Server'
conDEBUG = 'DRIVER={'+drivername+'};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password

print(conDEBUG)
conDEBUG = urllib.parse.quote_plus(conDEBUG)
conDEBUG = "mssql+pyodbc:///?odbc_connect=%s" % conDEBUG