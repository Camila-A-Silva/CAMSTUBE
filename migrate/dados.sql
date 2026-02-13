INSERT INTO `camstube`.`genero`
(`nome_genero`,
`icone`,
`cor`)
VALUES
("Rock","","red"),
("Pop","","blue"),
("MPB","","#FACADA");

INSERT INTO `camstube`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
("OMI",
"03:10",
"Cheerleaders",
"https://upload.wikimedia.org/wikipedia/pt/6/63/Capa_de_Cheerleader.jpg",
"POP"),
("Tim Maia",
"02:48",
"Não Quero Dinheiro",
"https://pt.wikipedia.org/wiki/N%C3%A3o_Quero_Dinheiro_%28S%C3%B3_Quero_Amar%29#/media/Ficheiro:Tim_Maia_1971.jpeg",
"MPB"),
("Justin Bieber",
"02:32",
"Baby",
"https://pt.wikipedia.org/wiki/Baby_%28can%C3%A7%C3%A3o_de_Justin_Bieber%29#/media/Ficheiro:Baby_Single.jpg",
"Pop");
