DROP DATABASE IF EXISTS solarAdventures;
CREATE DATABASE solarAdventures;

CREATE TABLE clasificacion(
ID INT NOT NULL auto_increment,
nombre VARCHAR(15),
puntos INT,
PRIMARY KEY (ID)
);

DELIMITER $$
CREATE TRIGGER puntos_negativos AFTER INSERT ON clasificacion FOR EACH ROW
BEGIN
IF NEW.puntos<0 THEN
UPDATE clasificacion SET puntos = 0 WHERE ID = NEW.ID;
END IF;
END$$
DELIMITER ;