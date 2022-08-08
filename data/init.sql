CREATE DATABASE patents;

ALTER DATABASE patents CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use patents;

CREATE TABLE patentData (
    id INT NOT NULL AUTO_INCREMENT, /* column numbers incremented automagically */
    pID VARCHAR (50), /* patent ID, e.g., number assigned */
    title VARCHAR (500), /* patent title, will be used for semantic similarity */
    abstract VARCHAR (500), /* this will be used for comparison of entered string to stored strings */
    inventor VARCHAR (500), /* could be more than one inventor, long names */
    publicationDate date,
    resultLink VARCHAR (100), /* this will be stored as a URL */
    PRIMARY KEY (id)
);


