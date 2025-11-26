CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;

CREATE TABLE sharing AS
    SELECT base.course ,count(DISTINCT other.hall)
    FROM finals as base join finals as other
    WHERE base.course != other.course and base.hall==other.hall
    GROUP BY base.course;


CREATE TABLE pairs AS
  SELECT base.room ||" and " || other.room ||" together have "|| (base.seats+other.seats) || " seats"
  FROM sizes as base join sizes as other
  WHERE base.room<other.room and (base.seats+other.seats)>=1000
  ORDER BY base.seats+other.seats DESC;

CREATE TABLE big AS
  SELECT course
  FROM sizes join finals
  WHERE sizes.room =finals.hall
  GROUP BY course
  HAVING sum(sizes.seats)>=1000
;

CREATE TABLE remaining AS
  SELECT  course,SUM(seats)-MAX(seats) AS remaining
  FROM finals join sizes
  WHERE finals.hall = sizes.room
  GROUP BY course
;

