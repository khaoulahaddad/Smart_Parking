CREATE TABLE Place (
	num INTEGER(5) PRIMARY KEY,
	etat CHAR(1) CHECk(etat in ('O','l')),
	prix INTEGER(8) DEFAULT 0
);


