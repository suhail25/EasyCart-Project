use EasyCart;

insert into Seller values
("S21"	,"Raman",	"21","raman@mahoo.com",	"9711912198"),
("S3"	,"Piyush",	'3','piyush@mahoo.com',	'9711912188'),
("S5"	,"Mayank",	'5','mayank@mahoo.com',	'7811912198'),
("S7"	,"Gujjar",	'7','gujjar@mahoo.com',	'9711912177'),
("S9"	,"Seema",	'9','seema@mahoo.com',	'9751912198'),
("S11"	,"Priyanshi",'11',	'priyanshi@mahoo.com',	'9711926198'),
("S13"	,"Dhaman",'13',	'dhaman@mahoo.com',	'9711412198'),
("S15"	,"Jay",	'15','jay@mahoo.com',	'9711912218'),
("S17"	,"Jack",'17',	'jack@mahoo.com',	'9711912116'), 
("S19"	,"William",'19',	'william@mahoo.com',	'9711912198');

insert  into Customer values
('C2'	,'Shyam','2','shyam@mahoo.com',	'9711912199'),
('C4'	,'Mohit','4',	'mohit@mahoo.com',	'9711002198'),
('C6'	,'Madhav','6',	'madhav@mahoo.com',	'9811912198'),
('C8'	,'Nidhi','8',	'nidhi@mahoo.com',	'9711912777'),
('C10'	,'Sakshi','10',	'sakshi@mahoo.com',	'9711852198'),
('C12'	,'Atul'	,'12','atul@mahoo.com',	'9711912193'),
('C14'	,'Rathore','14', 'rathore@mahoo.com',	'9481912198'),
('C16'	,'Michael','16',	'michael@mahoo.com',	'9321912198'),
('C18'	,'Jem','18',	'jem@mahoo.com',	'9711912798'),
('C20'	,'Shona','20',	'shona@mahoo.com',	'9451912198');

Delete from Users;
insert into Users values

("1"	,"Admin",	"Admin","Admin",	"1111111111"),
("21"	,"Raman",	"21","raman@mahoo.com",	"9711912198"),
("3"	,"Piyush",	'3','piyush@mahoo.com',	'9711912188'),
("5"	,"Mayank",	'5','mayank@mahoo.com',	'7811912198'),
("7"	,"Gujjar",	'7','gujjar@mahoo.com',	'9711912177'),
("9"	,"Seema",	'9','seema@mahoo.com',	'9751912198'),
("11"	,"Priyanshi",'11',	'priyanshi@mahoo.com',	'9711926198'),
("13"	,"Dhaman",'13',	'dhaman@mahoo.com',	'9711412198'),
("15"	,"Jay",	'15','jay@mahoo.com',	'9711912218'),
("17"	,"Jack",'17',	'jack@mahoo.com',	'9711912116'), 
("19"	,"William",'19',	'william@mahoo.com',	'9711912198'),
('2'	,'Shyam','2','shyam@mahoo.com',	'9711912199'),
('4'	,'Mohit','4',	'mohit@mahoo.com',	'9711002198'),
('6'	,'Madhav','6',	'madhav@mahoo.com',	'9811912198'),
('8'	,'Nidhi','8',	'nidhi@mahoo.com',	'9711912777'),
('10'	,'Sakshi','10',	'sakshi@mahoo.com',	'9711852198'),
('12'	,'Atul'	,'12','atul@mahoo.com',	'9711912193'),
('14'	,'Rathore','14', 'rathore@mahoo.com',	'9481912198'),
('16'	,'Michael','16',	'michael@mahoo.com',	'9321912198'),
('18'	,'Jem','18',	'jem@mahoo.com',	'9711912798'),
('20'	,'Shona','20',	'shona@mahoo.com',	'9451912198');

insert into product values
('27',	'GRITSTONES	Unisex',' Cotton Tie Dye Full Sleeves Shirt', 	'S13',	'Fashion and Clothing',	750, 20, 4.1, 12),
('28',	'Dennis Lingo Men', 'Stretchable Green Button Down Slim Fit Casual Shirt',	'S15'	,'Fashion and Clothing', 700, 20, 4.0, 16),
('29',	'Ben Martin	Men Denim',' Regular Fit Jeans Blue',	'S17',	'Fashion and Clothing',	850, 25, 4.3, 8),
('30',	'KRAVE	Women Striped ','Green Regular Fit Shirt',	'S3','Fashion and Clothing' , 900,	10, 3.6, 12),
('31',	'The Searchers',	'Director John Ford',	'S5',	'Entertainment', 750, 20, 3.8, 24),
('32',	'Raging Bull',	'Director Martin Scorsese',	'S9',	'Entertainment', 800, 15, 3.6, 16),
('33',	'The Deer Hunter',	'Director Michael Cimino',	'S7',	'Entertainment'	,900 ,40, 4.2, 10),
('34',	'Citizen Kane',	'Director Orson Welles', 'S5',	'Entertainment', 500, 30, 3.8, 6),
('35',	'Ran',	'Director Akira Kurusowa',	'S19'	,'Entertainment', 600, 30, 4.2, 13),
('36',	'A Man Search for Meaning',	'Author Viktor Frankl'	,'S19',	'Books', 1000, 20, 4.0, 10),
('37',	'A Search in Secret India',	'Author Paul Brunton',	'S13',	'Books',	1500,	15, 4.2, 12),
('38',	'The Light of Asia',	'Author Edwin Arnold',	'S3'	,'Books'	,500	,20, 3.5, 14),
('39',	'Nokia 8','	Charcoal 64GB 6GB RAM',	'S15',	'Consumer Electronics',	15000,	5, 3.4, 22),
('40',	'Skull Candy Riff',	'Gray Built-In Microphone',	'S7',	'Consumer Electronics',	1000,	10, 3.6, 23),
('41',	'ASUS F570','	Black AMD Quad Core 8GB RAM	','S7'	,'Consumer Electronics'	,25000	,25, 4.0, 12),
('42',	'Elle	Women', 'Slim Pants Red',	'S9'	,'Fashion and Clothing'	,800	,15, 4.0, 11),
('43',	'RM Fengshui Marble Turtle','	Decoration Gifting',	'S17',	'Fashion and Clothing',	1500,	10, 3.4, 16),
('44',	'Decals Design',' Flowers Branch	Wall Sticker',	'S17',	'Fashion and Clothing',	2000,	10, 3.3, 17),
('45',	'Furniture Cafe ','Zigzag Corner Wall Mount Shelf,	Wall Decoration',	'S15'	,'Fashion and Clothing',	1600,	15, 4.0, 11),
('46',	'The Idiot',	'Author Fyodor Dostoevsky'	,'S13'	,'Books',	1000,	20, 3.4, 32),
('47',	'Youbella	Bohemian',' Multicolor Metal Earrings For Women',	'S7',	'Home decoration',	12000,	10, 3.4, 23),
('48',	'Shining Diva Fashion','	Oxidized Silver Ring for Women'	,'S17',	'Home decoration',	25000,	5, 3.2, 18),
('49',	'Sukkhi	Gold',' Plated Jewellery Set for Women',	'S5'	,'Home decoration',	22000,	10, 3.8, 12),
('50',	'YouBella Jewellery',' Set	Silver Crystal Rhinestone Choker Necklace for Women',	'S13',	'Home decoration'	,25000,	10, 4.3, 11),
('51',	'Dettol Hand Sanitizer',	'Dettol Instant Hand Sanitizer - 50 ml',	'S9','Covid Emergencies',	200,	50, 3.7, 18),
('52','Disposable Mask	','ARNV 3-Ply Disposable Surgical Mask, Set of 50','	S9','Covid Emergencies'	,500,	15, 3.8, 17);

insert into product values
('27',	'GRITSTONES	Unisex',' Cotton Tie Dye Full Sleeves Shirt', 	'S3',	'Fashion and Clothing',	750, 20, 3.8, 12),
('28',	'Dennis Lingo Men', 'Stretchable Green Button Down Slim Fit Casual Shirt',	'S5'	,'Fashion and Clothing', 700, 20, 4.2, 16),
('29',	'Ben Martin	Men Denim',' Regular Fit Jeans Blue',	'S7',	'Fashion and Clothing',	850, 25, 4.1, 8),
('30',	'KRAVE	Women Striped ','Green Regular Fit Shirt',	'S13','Fashion and Clothing' , 900,	10, 3.9, 12),
('31',	'The Searchers',	'Director John Ford',	'S15',	'Entertainment', 750, 20, 3.6, 24),
('32',	'Raging Bull',	'Director Martin Scorsese',	'S19',	'Entertainment', 800, 15, 3.8, 16),
('33',	'The Deer Hunter',	'Director Michael Cimino',	'S17',	'Entertainment'	,900 ,40, 4.1, 10),
('34',	'Citizen Kane',	'Director Orson Welles', 'S15',	'Entertainment', 500, 30, 3.4, 6),
('35',	'Ran',	'Director Akira Kurusowa',	'S21'	,'Entertainment', 600, 30, 4.0, 13),
('36',	'A Man Search for Meaning',	'Author Viktor Frankl'	,'S9',	'Books', 1000, 20, 4.4, 10),
('37',	'A Search in Secret India',	'Author Paul Brunton',	'S3',	'Books',	1500,	15, 4.1, 12),
('38',	'The Light of Asia',	'Author Edwin Arnold',	'S13'	,'Books'	,500	,20, 3.8, 14),
('39',	'Nokia 8','	Charcoal 64GB 6GB RAM',	'S5',	'Consumer Electronics',	15000,	5, 3.6, 22),
('40',	'Skull Candy Riff',	'Gray Built-In Microphone',	'S3',	'Consumer Electronics',	1000,	10, 3.5, 23),
('41',	'ASUS F570','	Black AMD Quad Core 8GB RAM	','S21'	,'Consumer Electronics'	,25000	,25, 4.1, 12),
('42',	'Elle	Women', 'Slim Pants Red',	'S11'	,'Fashion and Clothing'	,800	,15, 4.2, 11),
('43',	'RM Fengshui Marble Turtle','	Decoration Gifting',	'S9',	'Fashion and Clothing',	1500,	10, 3.8, 16),
('44',	'Decals Design',' Flowers Branch	Wall Sticker',	'S7',	'Fashion and Clothing',	2000,	10, 3.7, 17),
('45',	'Furniture Cafe ','Zigzag Corner Wall Mount Shelf,	Wall Decoration',	'S5'	,'Fashion and Clothing',	1600,	15, 4.4, 11),
('46',	'The Idiot',	'Author Fyodor Dostoevsky'	,'S3'	,'Books',	1000,	20, 2.9, 32),
('47',	'Youbella	Bohemian',' Multicolor Metal Earrings For Women',	'S17',	'Home decoration',	12000,	10, 3.7, 23),
('48',	'Shining Diva Fashion','	Oxidized Silver Ring for Women'	,'S11',	'Home decoration',	25000,	5, 3.5, 18),
('49',	'Sukkhi	Gold',' Plated Jewellery Set for Women',	'S21'	,'Home decoration',	22000,	10, 4.2, 12),
('50',	'YouBella Jewellery',' Set	Silver Crystal Rhinestone Choker Necklace for Women',	'S3',	'Home decoration'	,25000,	10, 4.1, 11),
('51',	'Dettol Hand Sanitizer',	'Dettol Instant Hand Sanitizer - 50 ml',	'S19','Covid Emergencies',	200,	50, 3.8, 18),
('52','Disposable Mask	','ARNV 3-Ply Disposable Surgical Mask, Set of 50','	S19','Covid Emergencies'	,500,	15, 3.7, 17);

insert into cart values
('R02',	'Nokia 8'	,'P01',	'C02',	15000,	'2020-01-01',	'2020-01-08'),
('R04',	'Skull Candy Riff'	,'P03',	'C04',	1000,	'2020-01-10',	'2020-01-17'),
('R09',	'A Search in Secret India',	'P09',	'C06',	1500,	'2019-03-12',	'2019-03-19'),
('R08',	'The Light of Asia'	,'P11',	'C08',	500,	'2020-02-16',	'2020-02-21'),
('R10',	'A Man Search for Meaning',	'P07',	'C10',	1000,	'2020-04-13'	,'2020-04-21'),
('R12',	'RM Fengshui Marble Turtle',	'P33',	'C12',	1500,	'2020-03-21',	'2020-03-28'),
('R14',	'Raging Bull'	,'P15',	'C14',	'800',	'2020-02-11',	'2020-02-18'),
('R16',	'ASUS F570',	'P05',	'C16',	25000,	'2020-03-22',	'2020-03-29'),
('R18',	'Citizen Kane',	'P19',	'C18',	500,	'2020-03-17',	'2020-03-24'),
('R20',	'Ran'	,'P21',	'C20',	600,	'2020-02-18',	'2020-02-25');

