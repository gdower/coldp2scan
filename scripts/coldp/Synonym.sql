DROP TABLE IF EXISTS Synonym;
CREATE TABLE Synonym (
    taxonID VARCHAR(100),
    nameID VARCHAR(100),
    status VARCHAR(20),
    remarks TEXT,
    INDEX(taxonID(100)),
    INDEX(nameID(100))
) DEFAULT CHARSET=utf8mb4;