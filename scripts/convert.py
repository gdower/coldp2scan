from zipfile import ZipFile
from glob import glob
import csv
import mysql.connector

# find the zip archive
zip_files = glob('/raw/*.zip')
if len(zip_files) > 1:
    raise Exception("Only converting 1 zip file is currently supported.")

# extract the zip archive
zipfilePath = (zip_files[0])
zip = ZipFile(zipfilePath)
zip.extractall("tmp")
zip.close()



# import the csv files to the database
cnx = mysql.connector.connect(user='root', password='helloworld', host='database', database='convert', auth_plugin='mysql_native_password')
cursor = cnx.cursor()
with open('coldp/Synonym.sql') as f:
    cursor.execute(f.read(), multi=True)
cursor.close()
cnx.close()

# import data
cnx = mysql.connector.connect(user='root', password='helloworld', host='database', database='convert', auth_plugin='mysql_native_password')
cursor = cnx.cursor()
csv_data = csv.DictReader(open('tmp/Synonym.csv'), delimiter='\t')

for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO Synonym (taxonID, nameID, status, remarks) VALUES (%s,%s,%s,%s);", (row['taxonID'], row['nameID'], row['status'], row['remarks']))

cnx.commit()
cnx.close()



# convert the data
