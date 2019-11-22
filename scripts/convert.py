from zipfile import ZipFile
from glob import glob
import urllib.parse
import requests
import mysql.connector
import coldpy.name


# extends coldpy data model with methods for finding parent names
class Name(coldpy.name.Name):
    parent_names = {'order': '',
                    'nanorder': '',
                    'suborder': '',
                    'infraorder': '',
                    'parvorder': '',
                    'superfamily': '',
                    'family': '',
                    'subfamily': '',
                    'genus': '',
                    'subgenus': '',
                    'superspecies': '',
                    'subsuperspecies': '',
                    'species': '',
                    'subspecies': '',
                    'tribe': '',
                    'subtribe': ''}

    def add_parent_name(self, key, value):
        self.parent_names[key] = value


def get_parent(child):
    cursor.execute(
        "SELECT Name.* FROM Taxon INNER JOIN Name ON Taxon.nameID = Name.ID WHERE Taxon.ID=(SELECT DISTINCT parentID FROM Taxon WHERE nameID = '" + str(
            child.id) + "');")
    rows = cursor.fetchall()
    if len(rows) > 1:
        raise Exception('The following taxon has more than 1 parent: ' + str(child))
    elif len(rows) == 1:
        parent = rows[0]
        return Name(
            parent[0],
            parent[1],
            parent[2],
            parent[3],
            parent[4],
            parent[5],
            parent[6],
            parent[7],
            parent[8],
            parent[9],
            parent[10],
            parent[11],
            parent[12],
            parent[13],
            parent[14],
            parent[15])
    else:
        return None


def get_synonyms(name):
    cursor.execute(
        "SELECT DISTINCT scientificName, authorship FROM Name INNER JOIN Synonym ON Name.ID = Synonym.nameID WHERE taxonID = (SELECT DISTINCT ID FROM Taxon WHERE nameID = " + name.id + " LIMIT 1)")
    synonym_rows = cursor.fetchall()
    synonyms = ''
    for synonym in synonym_rows:
        synonyms += ' '.join([synonym[0], synonym[1]]).strip() + '; '
    return synonyms


def gnparser(name):
    url = 'http://gnparser:4334/api?q=' + \
          urllib.parse.quote(name)
    return requests.get(url).json()["namesJson"][0]


if __name__ == "__main__":

    # find the zip archive
    print("Extracting the zip archive to coldp directory...")
    zip_files = glob('/raw/*.zip')
    if len(zip_files) > 1:
        raise Exception("Only converting 1 zip file is currently supported.")
    # extract the zip archive
    zipfilePath = (zip_files[0])
    zip = ZipFile(zipfilePath)
    zip.extractall("/var/lib/mysql-files")
    zip.close()

    # import the csv files to the database
    print("Creating MySQL database schema...")
    cnx = mysql.connector.connect(user='root', password='helloworld', host='database', database='convert',
                                  auth_plugin='mysql_native_password', ssl_disabled=True)
    cursor = cnx.cursor()
    with open('sql/coldp.sql') as f:
        cursor.execute(f.read(), multi=True)
    cursor.close()
    cnx.close()

    # import data
    print("Importing data into MySQL database...")
    cnx = mysql.connector.connect(user='root', password='helloworld', host='database', database='convert',
                                  auth_plugin='mysql_native_password', ssl_disabled=True)
    cursor = cnx.cursor()
    cursor.execute(
        "LOAD DATA INFILE '/var/lib/mysql-files/Synonym.csv' INTO TABLE Synonym CHARACTER SET utf8mb4 COLUMNS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;")
    cursor.execute(
        "LOAD DATA INFILE '/var/lib/mysql-files/Name.csv' INTO TABLE Name CHARACTER SET utf8mb4 COLUMNS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;")
    cursor.execute(
        "LOAD DATA INFILE '/var/lib/mysql-files/Taxon.csv' INTO TABLE Taxon CHARACTER SET utf8mb4 COLUMNS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;")
    cnx.commit()

    # select species and subspecies
    print("Finding parent names of species and subspecies and their synonyms...")
    cursor.execute(
        "SELECT * FROM Name LEFT JOIN Synonym ON Name.ID = Synonym.nameID WHERE `rank` IN ('species', 'subspecies') AND Synonym.taxonID IS NULL;")
    species_list = cursor.fetchall()
    species_names = []
    for species in species_list:
        species_name = Name(
            species[0],
            species[1],
            species[2],
            species[3],
            species[4],
            species[5],
            species[6],
            species[7],
            species[8],
            species[9],
            species[10],
            species[11],
            species[12],
            species[13],
            species[14],
            species[15])

        this_name = species_name
        while this_name is not None:
            this_name = get_parent(this_name)
            if this_name is not None:
                species_name.add_parent_name(this_name.rank, this_name.scientific_name)
        species_names.append(species_name)

    print("Writing output tsv to scan directory...")
    output = open('scan/output.tsv', 'w')
    headers = ['order', 'suborder', 'infraorder', 'parvorder', 'nanorder', 'superfamily', 'family', 'subfamily',
               'genus', 'subgenus', 'superspecies', 'subsuperspecies', 'species', 'subspecies', 'tribe', 'subtribe',
               'species', 'author', 'synonyms']
    output.write('\t'.join(headers))

    for species in species_names:
        parsed_name = gnparser(species.scientific_name)
        synonyms = get_synonyms(species)
        output.write('\t'.join(
            [species.parent_names['order'],
             species.parent_names['suborder'],
             species.parent_names['infraorder'],
             species.parent_names['parvorder'],
             species.parent_names['nanorder'],
             species.parent_names['superfamily'],
             species.parent_names['family'],
             species.parent_names['subfamily'],
             species.parent_names['genus'],
             species.parent_names['subgenus'],
             species.parent_names['superspecies'],
             species.parent_names['subsuperspecies'],
             species.parent_names['species'],
             species.parent_names['subspecies'],
             species.parent_names['tribe'],
             species.parent_names['subtribe'],
             species.scientific_name,
             species.authorship,
             synonyms]) + '\n')
    cnx.close()
