# Contenido de la demo Hostal Antigua Morellana (Valencia) (es/ca/en/fr). Hechos de hostalam.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble dos camas','Doble matrimonio','Habitación adaptada'],'ca':['Doble dos llits','Doble matrimoni','Habitació adaptada'],'en':['Twin room','Double bed room','Adapted room'],'fr':['Chambre twin','Chambre double','Chambre adaptée']}
RD={
'es':['Para 1 o 2 personas, con 2 camas individuales, baño privado, escritorio y colchones viscoelásticos.','Para 2 personas, con cama de matrimonio, baño privado, escritorio y colchones viscoelásticos.','El hostal dispone de habitaciones adaptadas para personas con movilidad reducida.'],
'ca':['Per a 1 o 2 persones, amb 2 llits individuals, bany privat, escriptori i matalassos viscoelàstics.','Per a 2 persones, amb llit de matrimoni, bany privat, escriptori i matalassos viscoelàstics.','L\'hostal disposa d\'habitacions adaptades per a persones amb mobilitat reduïda.'],
'en':['For 1 or 2 people, with 2 single beds, private bathroom, desk and memory-foam mattresses.','For 2 people, with a double bed, private bathroom, desk and memory-foam mattresses.','The hostel has rooms adapted for people with reduced mobility.'],
'fr':['Pour 1 ou 2 personnes, avec 2 lits simples, salle de bains privée, bureau et matelas à mémoire de forme.','Pour 2 personnes, avec un lit double, salle de bains privée, bureau et matelas à mémoire de forme.','L\'hostal dispose de chambres adaptées aux personnes à mobilité réduite.']}
ART={
'hero':('arches',3401,['#f4e9da','#e6c79c','#c08a4e','#1f4f6b','#123247']),
'intro':('columns',3402,['#eef2f4','#f6f8f9','#b8893e','#1f4f6b','#123247']),
'r1':('arches',3411,['#f2e8da','#e2c296','#b9844a','#1f4f6b','#123247']),
'r2':('columns',3412,['#edf1f3','#f5f7f8','#c08c40','#245774','#15384d']),
'r3':('skyline',3413,['#1f3d55','#e48a5f','#f9d19b','#1d3a52','#152c3f','#0e1e2b']),
'g1':('hills',3421,['#e6ecd9','#f1e6c4','#f6cf8a','#a9c19e','#80a085','#587767']),
'g2':('arches',3422,['#f3e8d9','#e4c49a','#bc874c','#1f4f6b','#123247']),
'g3':('skyline',3423,['#23435c','#e2a160','#f6d59e','#21405a','#183247','#102231']),
'g4':('columns',3424,['#eef2f4','#f6f8f9','#b8893e','#1f4f6b','#123247']),
'g5':('arches',3425,['#f1e6d7','#dfbe92','#b58148','#1f4f6b','#123247']),
'g6':('hills',3426,['#e3ead6','#f0e5c2','#f4cf8c','#9fbf96','#6f9a72','#4d7550'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal Antigua Morellana · Hostal en el centro histórico de Valencia, junto al Mercado Central',see_rooms='Ver habitaciones',hero_k='Valencia · Centro histórico',hero_t='Vive la experiencia Morellana',hero_s='En un edificio del siglo XVIII, a 140 metros de la Lonja de la Seda y a pocos pasos del Mercado Central.',
 intro_t='Un alojamiento acogedor y familiar',intro_p1='Hostal Antigua Morellana está en el Carrer d´En Bou, 2, en pleno centro histórico: el Mercado Central, la Lonja de la Seda y la Catedral quedan a unos minutos a pie.',
 intro_p2='Tiene 18 habitaciones con baño privado, aire acondicionado, calefacción, TV, WiFi gratuito y colchones viscoelásticos. Recepción 24 horas y un equipo bilingüe.',
 stats=['Edificio del siglo XVIII','18 habitaciones','Recepción 24 horas','Habitaciones adaptadas'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Sus dos tipos de habitación doble y las habitaciones adaptadas.',
 svcs=['Recepción 24 horas','WiFi gratuito en todo el hostal','Aire acondicionado y calefacción','Colchones viscoelásticos','Consigna de equipajes','Servicio de lavandería','Área de café y bebidas','Información turística y reserva de entradas'],
 loc_p='Carrer d´En Bou, 2 · 46001 Valencia, a 140 metros de la Lonja de la Seda y a 400 metros de la plaza de la Virgen.',
 chips=['¿Qué habitaciones tiene?','¿Hay parking?','¿A qué hora es el check-in?','¿Cómo se reserva?']),
'ca':dict(title='Hostal Antigua Morellana · Hostal al centre històric de València, al costat del Mercat Central',see_rooms='Veure habitacions',hero_k='València · Centre històric',hero_t='Viu l\'experiència Morellana',hero_s='En un edifici del segle XVIII, a 140 metres de la Llotja de la Seda i a pocs passos del Mercat Central.',
 intro_t='Un allotjament acollidor i familiar',intro_p1='L\'Hostal Antigua Morellana és al Carrer d´En Bou, 2, en ple centre històric: el Mercat Central, la Llotja de la Seda i la Catedral queden a uns minuts a peu.',
 intro_p2='Té 18 habitacions amb bany privat, aire condicionat, calefacció, TV, WiFi gratuït i matalassos viscoelàstics. Recepció 24 hores i un equip bilingüe.',
 stats=['Edifici del segle XVIII','18 habitacions','Recepció 24 hores','Habitacions adaptades'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Els seus dos tipus d\'habitació doble i les habitacions adaptades.',
 svcs=['Recepció 24 hores','WiFi gratuït a tot l\'hostal','Aire condicionat i calefacció','Matalassos viscoelàstics','Consigna d\'equipatges','Servei de bugaderia','Zona de cafè i begudes','Informació turística i reserva d\'entrades'],
 loc_p='Carrer d´En Bou, 2 · 46001 València, a 140 metres de la Llotja de la Seda i a 400 metres de la plaça de la Mare de Déu.',
 chips=['Quines habitacions té?','Hi ha pàrquing?','A quina hora és el check-in?','Com es reserva?']),
'en':dict(title='Hostal Antigua Morellana · Hostel in Valencia\'s historic centre, next to the Central Market',see_rooms='See the rooms',hero_k='Valencia · Historic centre',hero_t='Live the Morellana experience',hero_s='In an 18th-century building, 140 metres from the Silk Exchange and a few steps from the Central Market.',
 intro_t='A cosy, family-run place to stay',intro_p1='Hostal Antigua Morellana is at Carrer d´En Bou, 2, right in the historic centre: the Central Market, the Silk Exchange and the Cathedral are a few minutes\' walk away.',
 intro_p2='It has 18 rooms with private bathroom, air conditioning, heating, TV, free WiFi and memory-foam mattresses. 24-hour reception and a bilingual team.',
 stats=['18th-century building','18 rooms','24-hour reception','Adapted rooms'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Its two double room types and the adapted rooms.',
 svcs=['24-hour reception','Free WiFi throughout','Air conditioning and heating','Memory-foam mattresses','Luggage storage','Laundry service','Coffee and drinks area','Tourist information and ticket booking'],
 loc_p='Carrer d´En Bou, 2 · 46001 Valencia, 140 metres from the Silk Exchange and 400 metres from Plaza de la Virgen.',
 chips=['What rooms does it have?','Is there parking?','What time is check-in?','How do I book?']),
'fr':dict(title='Hostal Antigua Morellana · Hostal dans le centre historique de Valence, près du Marché Central',see_rooms='Voir les chambres',hero_k='Valence · Centre historique',hero_t='Vivez l\'expérience Morellana',hero_s='Dans un bâtiment du XVIIIe siècle, à 140 mètres de la Bourse de la Soie et à deux pas du Marché Central.',
 intro_t='Un hébergement chaleureux et familial',intro_p1='L\'Hostal Antigua Morellana se trouve Carrer d´En Bou, 2, en plein centre historique : le Marché Central, la Bourse de la Soie et la Cathédrale sont à quelques minutes à pied.',
 intro_p2='Il compte 18 chambres avec salle de bains privée, climatisation, chauffage, TV, WiFi gratuit et matelas à mémoire de forme. Réception 24 heures et équipe bilingue.',
 stats=['Bâtiment du XVIIIe siècle','18 chambres','Réception 24 heures','Chambres adaptées'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Ses deux types de chambre double et les chambres adaptées.',
 svcs=['Réception 24 heures','WiFi gratuit partout','Climatisation et chauffage','Matelas à mémoire de forme','Consigne à bagages','Service de blanchisserie','Espace café et boissons','Infos touristiques et réservation de billets'],
 loc_p='Carrer d´En Bou, 2 · 46001 Valence, à 140 mètres de la Bourse de la Soie et à 400 mètres de la place de la Vierge.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','À quelle heure est le check-in ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
ES='https://www.hostalam.com/es/availability'; EN='https://www.hostalam.com/en/availability'
BOOK=dict(mode='engine',url={'es':ES,'ca':ES,'en':EN,'fr':EN})
D=dict(name='Hostal Antigua Morellana',ac='#1f4f6b',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Carrer d´En Bou, 2 · 46001 Valencia',phones=['+34 963 915 773'],emails=['info@hostalam.com'],maps='Hostal Antigua Morellana, Carrer d\'En Bou 2, Valencia',t=T)
META=dict(repo='demo-hostal-antigua-morellana-valencia',name='Hostal Antigua Morellana',legal_name='Antigua Morellana S.L.',registry_ids=['CIF B96621743'],
 url='https://www.hostalam.com/',domain='hostalam.com',municipality='Valencia',province='Valencia',sector='hostal en el centro histórico de Valencia',
 read_at='2026-10-29T08:05:00+01:00',created_at='2026-10-29T08:45:00+01:00',built_at='2026-10-29T08:45:00+01:00',audit_date='2026-10-29T07:56:00+01:00',
 rating=dict(value=4.8,coincide=['telefono','web'],date='2026-10-29T06:57:00+01:00',url='https://www.google.com/maps/place/Hostal+Antigua+Morellana/@39.4746528,-0.3771854,17z/data=!4m9!3m8!1s0xd604f4d9da6f17b:0x3d00cdeb8dadc716!5m2!4m1!1i2!8m2!3d39.4746528!4d-0.3771854!16s%2Fg%2F1tn02kqn?hl=es&entry=ttu&g_ep=EgoyMDI2MTAyMC4wIKXMDSoASAFQAw%3D%3D'),
 book=dict(mode='engine',url=BOOK['url'],note='Los botones Reservar van a la pagina de disponibilidad de su propia web (hostalam.com/es/availability y /en/availability, con su motor onetbooking); su web solo tiene es/en, asi que ca enlaza la version es y fr la en. La demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿Tienen habitaciones adaptadas?','K05'),('¿Admiten mascotas?','K06'),('¿Dónde está?','K07'),('¿A qué distancia está la Lonja?','K08'),('¿A qué hora es el check-in?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el correo?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Què tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('Teniu habitacions adaptades?','K05'),('Admeteu mascotes?','K06'),('On és?','K07'),('A quina distància és la Llotja?','K08'),('A quina hora és el check-in?','K09'),('Com reservo?','K10'),('Quin és el correu?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('Do you have adapted rooms?','K05'),('Are pets allowed?','K06'),('Where is it?','K07'),('How far is the Silk Exchange?','K08'),('What time is check-in?','K09'),('How do I book?','K10'),('What is the email?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Qu\'ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('Avez-vous des chambres adaptées ?','K05'),('Les animaux sont-ils admis ?','K06'),('Où est-ce ?','K07'),('À quelle distance est la Bourse de la Soie ?','K08'),('À quelle heure est le check-in ?','K09'),('Comment réserver ?','K10'),('Quel est l\'e-mail ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}
