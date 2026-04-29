---
title: "Restzetels en voorkeursstemmen"
url: "https://berthub.eu/articles/posts/restzetels-en-voorkeursstemmen/"
fetched_at: 2026-04-29T07:02:24.835585+00:00
source: "berthub.eu"
tags: [blog, raw]
---

# Restzetels en voorkeursstemmen

Source: https://berthub.eu/articles/posts/restzetels-en-voorkeursstemmen/

Vanaf een afstandje lijken dingen soms makkelijk. Maar van dichtbij valt het dan vaak tegen, met name als het goed gedaan moet worden. Zoals verkiezingen.
Ik hou het in dit artikel begrijpelijk en gebruik niet exact de woorden uit de kieswet. Ondanks dat ik weleens adviseer bij het bureau van de Kiesraad is dit allemaal
gehobby van mij persoonlijk
. Verder probeer ik hier een heldere uitleg te geven die niet opgaat voor absurde situaties, zoals dat alle stemmen op 1 partij zijn, of dat een partij niet genoeg kandidaten heeft ingeleverd etc. Het is wel de bedoeling dat deze pagina klopt voor normale Tweede Kamerverkiezingen! Voor gemeenteraad is het al weer (net) anders, overigens.
Aan het einde van dit document staan links naar de officiële uitleg van de Kiesraad
.
Verkiezingen
Ok, we hebben 150 zetels te verdelen. Er stemmen 9 miljoen mensen. Dat is dan 60.000 stemmen per zetel. Tot nu toe is het makkelijk.
De grootste partij heeft bijvoorbeeld 1,7 miljoen stemmen. Delen door 60.000, ze krijgen 28,33 zetels. Maar we kennen alleen maar hele zetels, we kunnen geen kandidaten in stukken zagen. Dus krijgen ze in eerste instantie 28 hele zetels.
Als we zo doorgaan met alle partijen krijgt iedere partij steeds net minder hele zetels dan er stemmen waren. Er blijft altijd een restje over. Zo kom je dus niet aan je 150 zetels.
Dit ziet er zo uit voor partijen A, B, C, D en E:
Je zou op dit moment kunnen zeggen, prima, de Tweede Kamer bestaat dit jaar uit 140 leden, en dan hoef je er verder ook niet meer over na te denken. Maar, helaas, we willen geen lege stoelen in de plenaire zaal, dus we moeten iets met de overgebleven stemmen en zetels.
Restzetels
We hebben in ons voorbeeld dus een paar zetels over. Die ‘restzetels’ gaan we 1 voor 1 uitdelen. Wie heeft er het meeste recht op een restzetel? In ons bovenstaande plaatje zijn dat op het oog duidelijk partijen B en E: zij hebben een duidelijk groter overschot aan stemmen die niet tot een zetel leidden. De kieswet legt het precies uit: een restzetel gaat naar die partij die, als ze de restzetel zouden krijgen, het hoogste aantal stemmen per zetel heeft. “Want die partij is er relatief het slechtste aan toe, en heeft de minste zetels per stem”.
Een concreet voorbeeld aan de hand van de
Tweede Kamer verkiezingen in 2023
. Hierbij is de
kiesdeler
1/150e van het aantal stemmen, en zoveel stemmen heb je dus nodig voor een hele zetel:
Kiesdeler 69551 38/75, er waren 10432726 stemmen
VVD: 22 (1589519 stemmen)
D66: 9 (656292 stemmen)
GROENLINKS / Partij van de Arbeid (PvdA): 23 (1643073 stemmen)
PVV (Partij voor de Vrijheid): 35 (2450878 stemmen)
CDA: 4 (345822 stemmen)
SP (Socialistische Partij): 4 (328225 stemmen)
Forum voor Democratie: 3 (232963 stemmen)
Partij voor de Dieren: 3 (235148 stemmen)
ChristenUnie: 3 (212532 stemmen)
Volt: 2 (178802 stemmen)
JA21: 1 (71345 stemmen)
Staatkundig Gereformeerde Partij (SGP): 3 (217270 stemmen)
DENK: 3 (246765 stemmen)
BBB: 6 (485551 stemmen)
Nieuw Sociaal Contract: 19 (1343287 stemmen)
140 zetels zijn toegekend, er zijn 10 restzetels
Het eerste wat opvalt is dat de kiesdeler echt als
breuk
wordt berekend: 69551 38/75. Niks geen floating point! Zo rolt de kieswet niet.
Daarna volgen de partijen die minstens een hele zetel hebben. Dit is belangrijk, want de partijen die dat niet gehaald hebben doen verder ook niet meer mee (bij de Tweede Kamerverkiezingen).
De laatste regel vertelt ons dat er 140 hele zetels uitgedeeld zijn. En dat we er dus nog 10 te gaan hebben. En daarvoor hebben we dan de volgende tabel, gesorteerd op het
aantal stemmen per zetel als ze de restzetel zouden krijgen
, aflopend:
BBB                                           69364 3/7 stemmen/zetel
CDA                                           69164 2/5 stemmen/zetel
VVD                                           69109 12/23 stemmen/zetel
GROENLINKS / Partij van de Arbeid (PvdA)      68461 3/8 stemmen/zetel
PVV (Partij voor de Vrijheid)                 68079 17/18 stemmen/zetel
Nieuw Sociaal Contract                        67164 7/20 stemmen/zetel
SP (Socialistische Partij)                    65645 stemmen/zetel
D66                                           65629 1/5 stemmen/zetel
DENK                                          61691 1/4 stemmen/zetel
Volt                                          59600 2/3 stemmen/zetel
Partij voor de Dieren                         58787 stemmen/zetel
Forum voor Democratie                         58240 3/4 stemmen/zetel
Staatkundig Gereformeerde Partij (SGP)        54317 1/2 stemmen/zetel
ChristenUnie                                  53133 stemmen/zetel
JA21                                          35672 1/2 stemmen/zetel
Restzetel 1 gaat naar BBB
Dit is dus per partij hoeveel stemmen per zetel die partij zou hebben ALS ze de restzetel zouden krijgen. En de partij met de meeste stemmen/zetel in dat geval krijgt hem ook echt. Want die waren tot dan toe er het slechtst aan toe. Dat is hier de BBB.
We hebben nu nog 9 zetels te gaan. Het algoritme in de kieswet zegt dat we dit proces gewoon moeten herhalen, wie is er nu het slechtste aan toe als ze (weer) een restzetel krijgen:
CDA                                           69164 2/5 stemmen/zetel
VVD                                           69109 12/23 stemmen/zetel
GROENLINKS / Partij van de Arbeid (PvdA)      68461 3/8 stemmen/zetel
PVV (Partij voor de Vrijheid)                 68079 17/18 stemmen/zetel
Nieuw Sociaal Contract                        67164 7/20 stemmen/zetel
SP (Socialistische Partij)                    65645 stemmen/zetel
D66                                           65629 1/5 stemmen/zetel
DENK                                          61691 1/4 stemmen/zetel
BBB                                           60693 7/8 stemmen/zetel
Volt                                          59600 2/3 stemmen/zetel
Partij voor de Dieren                         58787 stemmen/zetel
Forum voor Democratie                         58240 3/4 stemmen/zetel
Staatkundig Gereformeerde Partij (SGP)        54317 1/2 stemmen/zetel
ChristenUnie                                  53133 stemmen/zetel
JA21                                          35672 1/2 stemmen/zetel
Restzetel 2 gaat naar CDA
Nu staat het CDA bovenaan, die krijgen restzetel 2. Je zou kunnen denken dat je de restzetels gewoon op volgorde van dit lijstje uit kan delen, maar zo werkt het niet. Als een partij een restzetel krijgt staan ze daarna niet onderaan namelijk, zoals hier te zien bij de BBB, die staan in het midden, ondanks hun eerste restzetel. Bij de Tweede Kamer verkiezingen van 2023 kregen PVV, VVD en GL-PvdA ieder twee restzetels bijvoorbeeld:
Restzetel 1 gaat naar BBB
Restzetel 2 gaat naar CDA
Restzetel 3 gaat naar VVD
Restzetel 4 gaat naar GROENLINKS / Partij van de Arbeid (PvdA)
Restzetel 5 gaat naar PVV (Partij voor de Vrijheid)
Restzetel 6 gaat naar Nieuw Sociaal Contract
Restzetel 7 gaat naar PVV (Partij voor de Vrijheid)
Restzetel 8 gaat naar VVD
Restzetel 9 gaat naar GROENLINKS / Partij van de Arbeid (PvdA)
Restzetel 10 gaat naar SP (Socialistische Partij)
En zo zijn alle 150 zetels uitgedeeld.
Hier is de uitdraai van de officiele kiessoftware
.
Maar wie gaat er op die zetels zitten?
Ik begin met het simpele geval, waarbij een politieke partij 1 landelijke “gelijkluidende” lijst heeft ingediend.
Op zo’n lijst staan de kandidaten in een door de partij gekozen volgorde. Je zou denken dat de zetels ook in die volgorde uitgedeeld worden,
maar zo gaat het niet
.
Eerst kijken we naar de kandidaten die meer dan 25% van de kiesdeler aan stemmen gekregen hebben, en daar gaan de eerste zetels heen. Let wel, de partij moet dan wel genoeg zetels hebben. Het is niet zo dat als je maar drie zetels hebt, maar vier kandidaten met met meer dan 25%, dat je dan ineens vier zetels in mag nemen.
Als de kandidaten met 25% van de kiesdrempel geweest zijn, dan pas komt de rest aan de beurt, op volgorde van de lijst.
Het concept ‘voorkeursstem’ is daarmee geen afronding ofzo,
het zijn juist de belangrijkste kandidaten
. Pas daarna komt de rest in aanmerking.
Ieder Kamerverkiezing halen veel kandidaten de voorkeursdrempel, maar vaak waren dit al de kandidaten bovenaan de lijst, die toch al verkozen zouden worden. Maar nu alleen in een wat andere volgorde misschien.
Een klein handjevol kandidaten komt wel echt “met voorkeursstemmen” in de kamer, terwijl ze anders niet verkozen zouden zijn.
Citerend uit
parlement.com
over de vorige Tweede Kamerverkiezingen:
Er is één kandidaat met voorkeurstemmen gekozen. Dat is Daniëlle Hirsch (GroenLinks-PvdA), die in de plaats van Marleen Haage in de Kamer komt. Daarnaast behaalden nog 37 kandidaten voldoende voorkeurstemmen, maar zij hebben die niet nodig omdat ze ook zonder in de Kamer zouden gekomen zijn.
En het ingewikkelde geval?
Partijen kunnen ook verschillende
lijsten
indienen per
kieskring
. Dan kan je bijvoorbeeld in Limburg populaire Limburgers hoog plaatsen, en in Groningen juist weer Groningers. Dat trekt mogelijk extra stemmers. Je kunt zelfs kandidaten hebben die alleen in bepaalde kieskringen voorkomen.
Op zo’n moment wordt het allemaal vreselijk ingewikkeld wie er precies in de kamer komt, en in welke volgorde. Op een goeie dag begrijp ik het, maar het is erg niche.
Dit is overigens nog weer anders dan de zogeheten “lijstcombinatie”, waarbij partijen vroeger samen jacht konden maken op restzetels. Dit bleek zo ingewikkeld dat er we er mee opgehouden zijn.
De uitstekende mensen van de Kiesraad hebben diverse documenten voor wie exact wil weten hoe de zetelverdeling nou werkt:
Mocht je fouten ontdekken in het bovenstaande, mail me vooral op
bert@hubertnet.nl
- en vergeet niet te stemmen! Voor inspiratie, zie
NerdVote.nl
.
