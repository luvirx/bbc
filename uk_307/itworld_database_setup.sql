-- Webentwicklung - Projekt-ITWorld - beggmm & bzimmj

-- Vorhandene Sachen löschen
-- -----------------------------------------------------------------------------
-- DROP DATABASE itworld;

-- Datenbank erstellen
-- -----------------------------------------------------------------------------
-- CREATE DATABASE itworld;

-- Datenbank itworld nutzen
USE itworld;

-- Tabellen erstellen
-- -----------------------------------------------------------------------------
CREATE TABLE adresse (
id INT AUTO_INCREMENT PRIMARY KEY,
strasse VARCHAR(45),
plz INT,
ort VARCHAR(45)
);

CREATE TABLE zustand (
id INT AUTO_INCREMENT PRIMARY KEY,
zustand VARCHAR(45)
);

CREATE TABLE kategorie (
id INT AUTO_INCREMENT PRIMARY KEY,
kategorie VARCHAR(50)
);

CREATE TABLE person (
id INT AUTO_INCREMENT PRIMARY KEY,
anrede VARCHAR(20), -- könnte eigentlich noch in eine weitere Tabelle unterteilt werden
vorname VARCHAR(45),
nachname VARCHAR(45),
geburtsdatum VARCHAR(10),
telefonNr VARCHAR(10),
email VARCHAR(50),
benutzername VARCHAR(45),
passwort CHAR(60),
adresse_id INT,
FOREIGN KEY(adresse_id) REFERENCES adresse(id)
);

CREATE TABLE produkt (
id INT AUTO_INCREMENT PRIMARY KEY,
produktname VARCHAR(45),
produktbeschrieb VARCHAR(500),
aufrufe INT,
person_id INT,
kategorie_id INT,
bild VARCHAR(80),
zustand_id INT,
preis DOUBLE,
FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE,
FOREIGN KEY(kategorie_id) REFERENCES kategorie(id),
FOREIGN KEY(zustand_id) REFERENCES zustand(id)
);

-- Statische Daten einfügen
-- -----------------------------------------------------------------------------
INSERT INTO zustand (zustand) VALUES
('Neu'),
('Gebraucht'),
('Defekt');

-- Statische Kategorien einfügeneral
INSERT INTO kategorie (kategorie) VALUES
('Grafikkarten'),
('Motherboards'),
('Prozessoren'),
('Arbeitsspeicher'),
('Gehaeuse'),
('Festplatten'),
('Lueftung'),
('Laufwerke'),
('Steckkarten'),
('Netzteile'),
('Tastaturen'),
('Maeuse'),
('Headsets'),
('Monitore'),
('Weiteres');
