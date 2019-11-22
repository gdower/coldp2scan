DROP TABLE IF EXISTS Synonym;
CREATE TABLE Synonym (
    taxonID VARCHAR(100),
    nameID VARCHAR(100),
    status VARCHAR(20),
    remarks TEXT,
    INDEX(taxonID(100)),
    INDEX(nameID(100))
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS Taxon;
CREATE TABLE Taxon (
    ID VARCHAR(100),
    parentID VARCHAR(100),
    nameID VARCHAR(100),
    provisional TEXT,
    accordingTo TEXT,
    accordingToID VARCHAR(100),
    accordingToDate TEXT,
    referenceID TEXT,
    extinct TEXT,
    temporalRangeStart TEXT,
    temporalRangeEnd TEXT,
    lifezone TEXT,
    link TEXT,
    remarks TEXT,
    INDEX(ID(100)),
    INDEX(parentID(100)),
    INDEX(nameID(100)),
    INDEX(accordingToID(100))
) DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS Name;
CREATE TABLE Name (
    ID VARCHAR(100),
    scientificName TEXT,
    authorship TEXT,
    `rank` VARCHAR(20),
    genus TEXT,
    infragenericEpithet TEXT,
    specificEpithet TEXT,
    infraspecificEpithet TEXT,
    publishedInID VARCHAR(100),
    publishedInPage TEXT,
    publishedInYear TEXT,
    original TEXT,
    code TEXT,
    status TEXT,
    link TEXT,
    remarks TEXT,
    INDEX(ID(100)),
    INDEX(publishedInID(100))
) DEFAULT CHARSET=utf8mb4;

