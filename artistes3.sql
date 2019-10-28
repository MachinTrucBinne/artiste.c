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
  Size          BIGINT,
  Total_Time    INT,
  Disc_Number   INT,
  Disc_Count    INT,
  Track_Number  INT,
  Track_Count   INT,
  Year          INT,
  Bit_Rate      INT,
  Sample_Rate   INT
);

-- On importe le fichier XML dans Postgres :

INSERT INTO musique (Name,Artist,Album,Genre,Kind,Size,Total_Time,Disc_Number,Disc_Count,Track_Number,Track_Count,Year,Bit_Rate,Sample_Rate)
SELECT
  (unnest(xpath('//librairie/morceau/Name/text()', x)))::text AS Name,
  (unnest(xpath('//librairie/morceau/Artist/text()', x)))::text AS Artist,
  (unnest(xpath('//librairie/morceau/Album/text()', x)))::text AS Album,
  (unnest(xpath('//librairie/morceau/Genre/text()', x)))::text AS Genre,
  (unnest(xpath('//librairie/morceau/Kind/text()', x)))::text AS Kind,
  (unnest(xpath('//librairie/morceau/Size/text()', x)))::text::bigint AS Size,
  (unnest(xpath('//librairie/morceau/Total_Time/text()', x)))::text::int AS Total_Time,
  (unnest(xpath('//librairie/morceau/Disc_Number/text()', x)))::text::int AS Disc_Number,
  (unnest(xpath('//librairie/morceau/Disc_Count/text()', x)))::text::int AS Disc_Count,
  (unnest(xpath('//librairie/morceau/Track_Number/text()', x)))::text::int AS Track_Number,
  (unnest(xpath('//librairie/morceau/Track_Count/text()', x)))::text::int AS Track_Count,
  (unnest(xpath('//librairie/morceau/Year/text()', x)))::text::int AS Year,
  (unnest(xpath('//librairie/morceau/Bit_Rate/text()', x)))::text::int AS Bit_Rate,
  (unnest(xpath('//librairie/morceau/Sample_Rate/text()', x)))::text::int AS Sample_Rate
FROM unnest(xpath('//librairie', pg_read_file('//Users/user/Desktop/musique/Musique_extraite.xml')::xml)) AS x;


-- Ensuite on change les &amp; en & :

UPDATE 
   musique
SET 
   Name = REPLACE(Name, '&amp;', '&'),
   Artist = REPLACE(Artist, '&amp;', '&'),
   Album = REPLACE(Album, '&amp;', '&'),
   Genre = REPLACE(Genre, '&amp;', '&'),
   Kind = REPLACE(Kind, '&amp;', '&');




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


-- Pour avoir la durée moyenne des chansons (en millisecondes) :
SELECT AVG(Total_Time)
FROM musique;
-- Pour l'avoir en minutes il faut diviser par 1000*60.
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






