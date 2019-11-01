-- On efface la table musique (optionnel) :

DROP TABLE musique;

-- On crée une table musique :

CREATE TABLE IF NOT EXISTS musique (
  id            SERIAL PRIMARY KEY,
  Name          TEXT,
  Artist        TEXT,
  Album         TEXT,
  Genre         TEXT,
  Kind          TEXT,
  Size          TEXT, -- sera BIGINT
  Total_Time    TEXT, -- sera INT
  Disc_Number   TEXT, -- sera INT
  Disc_Count    TEXT, -- sera INT
  Track_Number  TEXT, -- sera INT
  Track_Count   TEXT, -- sera INT
  Year          TEXT, -- sera INT
  Bit_Rate      TEXT, -- sera INT
  Sample_Rate   TEXT  -- sera INT
);
-- Ici on importe en TEXT car INT n'accepte pas un string vide "" depuis XML

-- On importe le fichier XML dans Postgres :

INSERT INTO musique (Name,Artist,Album,Genre,Kind,Size,Total_Time,Disc_Number,Disc_Count,Track_Number,Track_Count,Year,Bit_Rate,Sample_Rate)
SELECT
  (unnest(xpath('//librairie/morceau/Name/@value', x)))::text AS Name,
  (unnest(xpath('//librairie/morceau/Artist/@value', x)))::text AS Artist,
  (unnest(xpath('//librairie/morceau/Album/@value', x)))::text AS Album,
  (unnest(xpath('//librairie/morceau/Genre/@value', x)))::text AS Genre,
  (unnest(xpath('//librairie/morceau/Kind/@value', x)))::text AS Kind,
  (unnest(xpath('//librairie/morceau/Size/@value', x)))::text AS Size,
  (unnest(xpath('//librairie/morceau/Total_Time/@value', x)))::text AS Total_Time,
  (unnest(xpath('//librairie/morceau/Disc_Number/@value', x)))::text AS Disc_Number,
  (unnest(xpath('//librairie/morceau/Disc_Count/@value', x)))::text AS Disc_Count,
  (unnest(xpath('//librairie/morceau/Track_Number/@value', x)))::text AS Track_Number,
  (unnest(xpath('//librairie/morceau/Track_Count/@value', x)))::text AS Track_Count,
  (unnest(xpath('//librairie/morceau/Year/@value', x)))::text AS Year,
  (unnest(xpath('//librairie/morceau/Bit_Rate/@value', x)))::text AS Bit_Rate,
  (unnest(xpath('//librairie/morceau/Sample_Rate/@value', x)))::text AS Sample_Rate
FROM unnest(xpath('//librairie', pg_read_file('//Users/user/Desktop/musique/Musique_extraite.xml')::xml)) AS x;

-- On change les &amp; en & :

UPDATE musique
SET 
  Name = REPLACE(Name, '&amp;', '&'),
  Artist = REPLACE(Artist, '&amp;', '&'),
  Album = REPLACE(Album, '&amp;', '&'),
  Genre = REPLACE(Genre, '&amp;', '&'),
  Kind = REPLACE(Kind, '&amp;', '&');

-- On change les textes vides "" en valeur NULL :

UPDATE musique SET Disc_Number  = NULL WHERE Disc_Number  = '';
UPDATE musique SET Disc_Count   = NULL WHERE Disc_Count   = '';
UPDATE musique SET Track_Number = NULL WHERE Track_Number = '';
UPDATE musique SET Track_Count  = NULL WHERE Track_Count  = '';
UPDATE musique SET Year         = NULL WHERE Year         = '';

-- On change les strings en nombres :

ALTER TABLE musique
ALTER COLUMN Size         TYPE BIGINT USING size::bigint,
ALTER COLUMN Total_Time   TYPE INT    USING Total_Time::integer,
ALTER COLUMN Disc_Number  TYPE INT    USING Disc_Number::integer,
ALTER COLUMN Disc_Count   TYPE INT    USING Disc_Count::integer,
ALTER COLUMN Track_Number TYPE INT    USING Track_Number::integer,
ALTER COLUMN Track_Count  TYPE INT    USING Track_Count::integer,
ALTER COLUMN Year         TYPE INT    USING Year::integer,
ALTER COLUMN Bit_Rate     TYPE INT    USING Bit_Rate::integer,
ALTER COLUMN Sample_Rate  TYPE INT    USING Sample_Rate::integer;



------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------


-- Pour imprimer les artistes :

SELECT DISTINCT artist FROM musique ORDER BY Artist;

-- Pour imprimer plein de choses :

SELECT id,Name,Artist,Album FROM musique ORDER BY id LIMIT 100;

-- Imprimer les artistes qui ont le plus long nom :

SELECT Artist, LENGTH(Artist)
FROM musique
GROUP BY Artist
ORDER BY LENGTH(Artist) DESC
LIMIT 40;

-- Pour avoir les tounes qui ont le plus long nom :

SELECT Name,Artist,LENGTH(Name)
FROM musique
ORDER BY LENGTH(Name) DESC
LIMIT 40;

-- Pour avoir les albums qui ont le plus long nom :

SELECT Album,LENGTH(Album)
FROM musique
GROUP BY Album
ORDER BY LENGTH(Album) DESC
LIMIT 40;


-- Pour avoir la durée moyenne des chansons (en minutes) :
SELECT AVG(Total_Time)/60000
FROM musique;
-- Ça me donne 4 min 3 secondes.


-- Pour avoir les fichiers les plus lourds :
SELECT Name, Artist, Album, size
FROM musique
ORDER BY size DESC
LIMIT 100;

-- Pour avoir la moyenne des tailles :
SELECT AVG(size)
FROM musique;

-- Pour les genres :
SELECT DISTINCT Genre
FROM musique
ORDER BY Genre;

-- Pour trier les morceaux selon leur durée :
SELECT Name,Artist,Album,Total_Time
FROM musique
ORDER BY Total_Time DESC
LIMIT 40;

-- Pour avoir la durée du plus long morceau de chaque album :
SELECT DISTINCT Album,MAX(Total_Time)
FROM musique
GROUP BY Album
ORDER BY MAX(Total_Time) DESC;

-- Pour avoir la durée moyenne des morceaux d'un artiste :
SELECT artist, AVG(total_time/(60*1000.0)) AS duree
FROM musique
GROUP BY Artist
ORDER BY duree LIMIT 40;

-- Pour avoir l'année moyenne des morceaux d'un artiste (pondéré selon le nombre de morceaux) :
SELECT artist, AVG(year) AS annee_moy
FROM musique
GROUP BY Artist
ORDER BY annee_moy LIMIT 40;











