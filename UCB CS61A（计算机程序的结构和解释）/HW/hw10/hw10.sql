CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT  child
  FROM dogs join parents ON dogs.name =parents.parent
  ORDER BY dogs.height
  DESC
;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name ,size
  FROM dogs JOIN sizes 
  ON dogs.height<=sizes.max and dogs.height>sizes.min
  ;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT old.child as old_child ,new.child as new_child
  FROM   parents as old join parents as new
  WHERE old.child<new.child and old.parent=new.parent
;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, "|| siblings.old_child || " and " || siblings.new_child ||", have the same size: "|| new.size
  FROM siblings join size_of_dogs as old join size_of_dogs as new 
  ON new.name =siblings.new_child and old.name =siblings.old_child
  WHERE new.size=old.size
;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur , max(height)-min(height)  as height_range
  FROM dogs
  GROUP BY fur
  HAVING max(height)<=1.3*AVG(height) and min(height)>=0.7*AVG(height)
;

