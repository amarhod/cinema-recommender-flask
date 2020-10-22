from BioFilmer.recommender import read_file

l2 = [{'Actors': ' George Mackay, Dean-Charles Chapman, Richard Madden, Benedict '
            'Cumberbatch, Colin Firth, Mark Strong',
  'Date': ' 31 jan 2020',
  'Description': 'Två brittiska soldater får i uppdrag att ta sig långt in '
                 'bakom fiendelinjen för att varna ett regemente för ett '
                 'bakhåll som tyskarna planerar.',
  'Directors': ' Sam Mendes',
  'Genre': 'Drama, Krig',
  'Original_language': ' Engelska ',
  'Original_title': ' 1917'},
 {'Actors': ' Christos Loulis, Ulrich Tukur',
  'Date': ' 10 jul 2020',
  'Description': 'I kölvattnet av börskraschen som startade i USA 2007 är '
                 'Grekland 2015 ett land på ruinens brant. Bakom lyckta dörrar '
                 'försöker landets finansminister Gianis Varoufakis rädda vad '
                 'som räddas kan genom hårda åtstramningsförslag. Allt för att '
                 'Grekland inte ska knuffas ut ur EU och ned i en evig '
                 'skuldfälla...',
  'Directors': ' Costa-Gavras ',
  'Genre': 'Drama, Thriller',
  'Original_language': ' Franska,  Tyska,  Engelska,  Grekiska ',
  'Original_title': ' Adults in the Room'},
 {'Actors': ' Will Smith, Martin Lawrence',
  'Date': ' 17 jan 2020',
  'Description': 'Poliserna Mike Lowrey och Marcus Burnett är tillbaka en '
                 'sista gång i "Bad Boys for Life".',
  'Directors': ' Adil El Arbi, Bilall Fallah',
  'Genre': 'Action, Komedi',
  'Original_language': ' Engelska ',
  'Original_title': ' Bad Boys for Life'},
 {'Actors': ' Christian Bale, Michael Caine, Ken Watanabe, Liam Neeson, Katie '
            'Holmes, Gary Oldman, Rutger Hauer, Morgan Freeman',
  'Date': ' 24 jun 2020',
  'Description': 'Den ursprungliga berättelsen om hur Bruce Wayne bestämmer '
                 'sig för det goda och sitt alter ego Batman. Bruce Wayne ser '
                 'sina föräldrar mördas och vill hämnas på förövaren. Men - '
                 'han inser att hämnd inte löser något, utan blir i stället '
                 'Batman.',
  'Directors': ' Christopher Nolan',
  'Genre': 'Action, Äventyr',
  'Original_language': ' Engelska ',
  'Original_title': ' Batman Begins'},
 {'Actors': ' Hugo Krajcik, Julia Pirzadeh, Frank Dorsin, Yussra El Abdouni, '
            'Arvid Berg, Björn Gustafsson, Suzanne Reuter',
  'Date': ' 5 aug 2020',
  'Description': 'Det är Bert Ljungs och hans kompisar Åkes och Lill-Eriks '
                 'första dag på högstadiet. På skolan är Yoghurt-Leila den '
                 'stora stjärnan. Hon går i nian, är reklammodell, cool och '
                 'precis alla beundrar henne. Så fort Bert får syn på Leila '
                 'faller han pladask. Men hur ska han få henne att lägga märke '
                 'till honom, han går ju bara i sjuan?! Kanske kan Amira, ny i '
                 'Berts klass och lillasyster till Leila, vara till hjälp?',
  'Directors': ' Michael Lindgren',
  'Genre': 'Familj',
  'Original_language': ' Svenska ',
  'Original_title': ' Berts dagbok'},
 {'Actors': ' Katie Holmes, Owain Yeoman, Ralph Ineson',
  'Date': ' 24 jun 2020',
  'Description': 'Helt omedvetna om familjen Heelshires mardrömslika historia '
                 'flyttar en ung familj in i gästhuset på deras gård, väldigt '
                 'snart lär deras son känna en ny vän, som visar sig vara en '
                 'mystisk och extremt människolik docka som kallas för Brahms.',
  'Directors': ' William Brent Bell',
  'Genre': 'Skräck, Thriller',
  'Original_language': ' Engelska ',
  'Original_title': ' Brahms: The Boy II'},
 {'Actors': ' Jesper Christensen, Bodil Jørgensen, Mads Reuther, Sara Viktoria '
            'Bjerregaard, Lue Dittmann Støvelbæk, Sylvester Byder, Gustav '
            'Dyekjær Giese, Pernille Højmark, Cyron Melville, Claes Malmberg',
  'Date': ' 29 maj 2020',
  'Description': 'När Tyskland ockuperar Danmark förändras tillvaron för den '
                 'framgångsrike fabrikör Skov, och frågan hur han ska agera '
                 'med hedern i behåll blir brännande aktuell. Denna skildring '
                 'av andra världskrigets grepp om en dansk familj under de '
                 'första ockupationsåren 1940-43 blev en succé på danska '
                 'biografer, med närmare 400 000 besökare.',
  'Directors': ' Anders Refn',
  'Genre': 'Drama',
  'Original_language': ' Danska ',
  'Original_title': ' De forbandede år'},
 {'Actors': ' Dixie Egerickx, Colin Firth, Julie Walters, Edan Hayhurst, Isis '
            'Davis',
  'Date': ' 17 jul 2020',
  'Description': 'Mary Lennox är en lättirriterad och oälskad 10-årig flicka '
                 'född i Indien till rika brittiska föräldrar.\n'
                 'När föräldrarna plötsligt dör skickas Mary tillbaka till '
                 'England, där hon får bo med sin morbror Archibald Craven på '
                 'hans avlägsna herrgård bland hedarna i Yorkshire.\n'
                 'Hos farbrorn börjar Mary förstå många av familjens '
                 'hemligheter, framförallt efter att hon träffat sin sjuklige '
                 'kusin Colin, som levt avskärmad i en av husets flyglar.\n'
                 'De båda kantstötta, lite udda barnen läker varandra genom '
                 'sin upptäckt av en hemlig, osannolik trädgård gömd på ägorna '
                 'till egendomen Misselthwaite. En magisk och äventyrlig plats '
                 'som ska komma att förändra deras liv för alltid.',
  'Directors': ' Marc Munden',
  'Genre': 'Drama, Familj, Fantasy',
  'Original_language': ' Engelska ',
  'Original_title': ' The Secret Garden'},
 {'Actors': ' Tom Hardy, Cillian Murphy, Kenneth Branagh, Mark Rylance, Harry '
            "Styles, James D'Arcy",
  'Date': ' 24 jun 2020',
  'Description': 'Dunkirk är berättelsen om de hundratusentals brittiska och '
                 'allierade trupper som blir invaderade och omringade på '
                 'stranden vid Dunkerque av fientliga styrkor under andra '
                 'världskriget.',
  'Directors': ' Christopher Nolan',
  'Genre': 'Action, Drama, Krig',
  'Original_language': ' Engelska ',
  'Original_title': ' Dunkirk'},
 {'Actors': ' Chris Pratt, Tom Holland, Julia Louis-Dreyfus, Octavia Spencer',
  'Date': ' Engelska ',
  'Description': 'Disney/Pixar tar dig med till en fantasivärld fylld med '
                 'alver där vi möter två tonårsbröder som ger sig ut på ett '
                 'extraordinärt äventyr -  de vill undersöka om det '
                 'fortfarande finns magi i världen.',
  'Directors': ' Dan Scanlon',
  'Genre': 'Äventyr, Komedi, Familj',
  'Original_language': ' Onward',
  'Original_title': ' Victor Segell, Edvin Ryding, Nina Hjelmkvist, Gladys del '
                    'Pilar'},
 {'Actors': ' Sean Astin, Josh Brolin, Jeff Cohen, Corey Feldman, Kerri Green, '
            'Martha Plimpton, Jonathan Ke Quan, Anne Ramsey',
  'Date': ' 14 aug 2020',
  'Description': '"Här händer det aldrig något", säger Mikey, ledaren för '
                 'Dödskallegänget. Han vet inte att han och hans sex kompisar '
                 'snart kommer få mer än nog av spänning och mystik. Allt '
                 'börjar när de hittar Enögde Willies skattkarta. De känner '
                 'genast igen några viktiga landmärken och anar var skatten '
                 'finns.',
  'Directors': ' Richard Donner',
  'Genre': 'Äventyr, Action, Komedi',
  'Original_language': ' Engelska ',
  'Original_title': ' The Goonies'},
 {'Actors': ' Gerard Butler, Morena Baccarin, Scott Glenn',
  'Date': ' 12 aug 2020',
  'Description': 'Familjen Garrity kämpar för att överleva samtidigt som en '
                 'dödlig komet är på väg mot jorden. John, hans fru Allison '
                 'och deras lilla son Nathan gör en riskfylld resa för att ta '
                 'sig till en säker plats. När världen nås av skrämmande '
                 'nyheter om kometens dödliga framfart upplever familjen '
                 'Garrity både det bästa och värsta hos mänskligheten '
                 'samtidigt som de kämpar mot den ökade paniken och '
                 'laglösheten runt omkring dem. Nedräkningen till den globala '
                 'apokalypsen närmar sig och familjens desperata flykt '
                 'kulminerar i ett sista-minuten-flyg till en möjlig fristad.',
  'Directors': ' Ric Roman Waugh',
  'Genre': 'Action, Thriller',
  'Original_language': ' Engelska ',
  'Original_title': ' Greenland'},
 {'Actors': ' Laura Birn, Johannes Holopainen, Pirkko Saisio',
  'Date': ' 14 aug 2020',
  'Description': 'Året är 1915. Helene Schjerfbecks konstnärskap håller på att '
                 'falla i glömska. Det är år sedan hon hade sin senaste '
                 'utställning. Men så dyker en konsthandlare dyker upp med '
                 'stora planer för Helene. Och hon får kontakt med beundraren '
                 'och amatörmålaren Einar Reuter. Livet får en nytändning och '
                 'blir aldrig mer sig likt.',
  'Directors': ' Antti Jokinen',
  'Genre': 'Drama',
  'Original_language': ' Finska ',
  'Original_title': ' Helene'},
 {'Actors': ' Leonardo DiCaprio, Ken Watanabe, Marion Cotillard, Tom Hardy, '
            'Michael Caine, Joseph Gordon-Levitt',
  'Date': ' 24 jun 2020',
  'Description': 'Dom Cobb är den absolut bästa tjuven i den farliga konsten i '
                 'att extrahera: stjäla värdefulla hemligheter från djupt inne '
                 'i det undermedvetna under drömstadiet. Detta har gjort honom '
                 'till en åtråvärd spelare i en ny värld av industrispionage, '
                 'men också till en internationell flykting och kostat honom '
                 'allt han någonsin älskat. Nu erbjuds Cobb en chans till '
                 'försoning. Ett sista jobb kan ge honom tillbaka hans liv men '
                 'bara om han kan uppnå det omöjliga – att plantera en idé.',
  'Directors': ' Christopher Nolan',
  'Genre': 'Action, Thriller',
  'Original_language': ' Engelska ',
  'Original_title': ' Inception'},
 {'Actors': ' Matthew McConaughey, Anne Hathaway, Jessica Chastain, Matt '
            'Damon, John Lithgow, Michael Caine',
  'Date': ' 24 jun 2020',
  'Description': 'En grupp forskare får ett avgörande uppdrag - att resa till '
                 'andra stjärnsystem och utforska om vi har en framtid i '
                 'rymden.',
  'Directors': ' Christopher Nolan',
  'Genre': 'Äventyr, Drama, Sci-Fi',
  'Original_language': ' Engelska ',
  'Original_title': ' Interstellar'},
 {'Actors': ' Roman Griffin Davis, Thomasin McKenzie, Taika Waititi, Sam '
            'Rockwell, Scarlett Johansson, Rebel Wilson, Stephen Merchant',
  'Date': ' 10 jan 2020',
  'Description': 'En andra världskriget-satir om en ensam tysk pojke vars '
                 'världsbild vänds upp och ned när han upptäcker att hans '
                 'mamma gömmer en ung judisk flicka på vinden. Med hjälp av '
                 'sin idiotiska låtsasvän Adolf Hitler måste han nu '
                 'konfrontera sina nationalistiska fördomar.',
  'Directors': ' Taika Waititi',
  'Genre': 'Komedi, Drama',
  'Original_language': ' Engelska ',
  'Original_title': ' Jojo Rabbit'},
 {'Actors': ' Karen Gillan, Dwayne Johnson, Kevin Hart, Jack Black, Danny '
            'DeVito, Danny Glover, Madison Iseman, Alex Wolff, Morgan Turner, '
            "Ser'Darius Blain",
  'Date': ' 6 dec 2019',
  'Description': 'Gänget är tillbaka i "Jumanji: The Next Level", men spelet '
                 'har ändrats. När de återvänder till spelet för att rädda en '
                 'från gänget upptäcker dem att inget är som de förväntar sig. '
                 'De kommer att behöva ge sig i kast med nya okända delar som '
                 'torra öknar och snöiga berg, för att fly världens farligaste '
                 'spel.',
  'Directors': ' Jake Kasdan',
  'Genre': 'Action, Äventyr, Komedi',
  'Original_language': ' Engelska ',
  'Original_title': ' Jumanji: The Next Level'},
 {'Actors': ' Brie Larson, Michael B. Jordan, Jamie Foxx, Rob Morgan, Tim '
            "Blake Nelson, Rafe Spall, O'Shea Jackson Jr., Karan Kendrick",
  'Date': ' 17 jan 2020',
  'Description': 'Efter att den unge advokaten Bryan Stevenson han tagit '
                 'examen från Harvard har han en rad välbetalda jobb att välja '
                 'på. Istället åker han till Alabama för att försvara '
                 'felaktigt dömda människor, och människor som inte haft råd '
                 'med ordentligt juridiskt försvar, med stöd av den lokala '
                 'advokaten Eva Ansley. Ett av hans första, och mest '
                 'uppseendeväckande fall är Walter McMillians, som 1987 dömdes '
                 'till döden för ett uppmärksammat mord på en 18-årig flicka '
                 'trots övertygande bevis på hans oskuld. Det enda '
                 'vittnesmålet mot McMillian kom från en kriminell – som '
                 'dessutom haft anledning att ljuga i rätten. De följande åren '
                 'blir Bryan indragen i en labyrint av juridiskt och politiskt '
                 'manövrerande och öppen rasism när han kämpar för Walter och '
                 'andra liknande fall. Han har varken oddsen eller systemet på '
                 'sin sida.',
  'Directors': ' Destin Daniel Cretton',
  'Genre': 'Drama',
  'Original_language': ' Engelska ',
  'Original_title': ' Just Mercy'},
 {'Actors': ' Polly Stjärne, Nils Kendle, Rani Pyne, Tomas Norström, Tomas Von '
            'Brömssen, Alexej Manvelov, Anna Bjelkerud, Lia Boysen, Ulla '
            'Skoog, David Wiberg, Peter Viitanen',
  'Date': ' 7 feb 2020',
  'Description': 'Lasse och Maja har fått sin detektivbyrå nedlagd av '
                 'polischefen i närliggande Kristinelund när Klara söker upp '
                 'dem. Hon behöver hjälp med att bevisa att hennes pappa '
                 'Ferdinand är oskyldig till tågrånet han dömts för. Lasse och '
                 'Maja ser nu sin stora chans att få upprättelse, att visa att '
                 'de visst kan lösa brott!',
  'Directors': ' Moa Gammel',
  'Genre': 'Familj',
  'Original_language': ' Svenska ',
  'Original_title': ' LasseMajas detektivbyrå - Tågrånarens hemlighet'},
 {'Actors': ' Mimmi Sandén, Gabriel Odenhammar, Göran Berlander, Adil Backman, '
            'Ayla Kabaca, Adam Fietz, Oscar Rosberg, Anders Öjebo, Claes '
            'Grufman, Dominique Pålsson Wiklund, Figge Norling, Frank '
            'Thunfors, Fredrik Hiller, Hugo Gummeson, Jennie Jahns, Jesper '
            'Adefelt, Juni Kinell, Magnus Mark, Oscar Harryson, Paulina Åberg',
  'Date': ' 7 aug 2020',
  'Description': 'Följ med till Hemskogens underbara värld, befolkad av '
                 'listiga och snälla djur; Latte Igelkott, Ekorren Tjum och '
                 'många andra. I skogen råder torka men det sägs att det finns '
                 'en magisk vattensten i björnarnas rike... Latte är en '
                 'ovanligt stöddig liten igelkott och ger sig av ensam för att '
                 'hämta stenen. Men för att komma dit måste Latte ta sig genom '
                 'lodjurens och vargarnas riken. Och om hon lyckas ta sig dit, '
                 'hur skall hon då kunna röva bort vattenstenen från '
                 'björnarnas borg?',
  'Directors': ' Nina Wels, Regina Welker',
  'Genre': 'Animerat, Familj',
  'Original_language': ' Engelska,  Tyska ',
  'Original_title': ' Latte Igel und der magische Wasserstein'},
 {'Actors': ' Anouk Aimée, Jean-Louis Trintignant, Monica Bellucci, Marianne '
            'Denicourt',
  'Date': ' 7 aug 2020',
  'Description': 'Anne och Jean-Louis träffades för mer än 50 år sedan. Han, '
                 'en racerförare och hon, en scripta. Deras berättelse '
                 'förevigades i en film som för alltid förändrade vår syn på '
                 'kärlek. Nu fortsätter deras historia tillsammans efter att '
                 'Jean-Louis son sökt upp Anne efter alla dessa år och '
                 'återförenar de två igen. En film om att minnas och om hur '
                 'kärlek kan överleva trots tidens oundvikliga gång.',
  'Directors': ' Claude Lelouch',
  'Genre': 'Drama',
  'Original_language': ' Franska ',
  'Original_title': ' The Best Years of a Life'},
 {'Actors': ' Tom Hardy, Charlize Theron, Nicholas Hoult',
  'Date': ' 31 jul 2020',
  'Description': 'I resterna efter en ödelagd värld strider människorna mot '
                 'varandra i en kamp för överlevnad. Ensamvargen Max och '
                 'kvinnan Imperator Furiosa kan inte undvika att dras in i det '
                 'fullskaliga vägkrig som rasar.',
  'Directors': ' George Miller',
  'Genre': 'Action, Äventyr, Sci-Fi',
  'Original_language': ' Engelska ',
  'Original_title': ' Mad Max: Fury Road - klassiker'},
 {'Actors': ' Rosamund Pike, Sam Riley, Anya Taylor-Joy, Jonathan Aris',
  'Date': ' 24 jun 2020',
  'Description': 'Från 1870-talet till modern tid, "Marie Curie: Pionjär. '
                 'Geni. Rebell" är en resa genom Marie Curies liv – hennes '
                 'passionerade förhållanden, vetenskapliga genombrott och '
                 'konsekvenserna som följde för henne och världen. Efter att '
                 'hon träffat och gift sig med forskaren Pierre Curie '
                 'förändrar de tillsammans vetenskapen genom upptäckten av '
                 'radioaktivitet. Genialiteten bakom paret Curies upptäckter '
                 'och det påföljande Nobelpriset gör också att de hamnar i '
                 'omvärldens strålkastarljus.',
  'Directors': ' Marjane Satrapi',
  'Genre': 'Drama, Romantik',
  'Original_language': ' Engelska ',
  'Original_title': ' Radioactive'},
 {'Actors': ' Hedda Stiernstedt, Rolf Lassgård, Lena Endre, Klas Wiljergård, '
            'Nour El Refai, Kajsa Ernst, Ralph Carlsson, Vilhelm Blomgren, '
            'Mårten Klingberg, Natalie Minnevik',
  'Date': ' 21 feb 2020',
  'Description': 'Efter att ha brutit upp med pojkvännen återvänder Hanna, 28, '
                 'till Alingsås för ett vikariat på lokalnyheterna. När hennes '
                 'älskade pappa, prästen med det stora skägget, avslöjar att '
                 'han egentligen vill vara Marianne vänds Hannas värld upp och '
                 'ner. Men för pappa Marianne finns ingen återvändo, hon måste '
                 'äntligen få vara den hon är. Det blir en omtumlande resa för '
                 'Hanna som varken kände sig själv eller sin pappa så väl som '
                 'hon trodde. En varm feelgood-berättelse om modet att vara '
                 'sig själv och lyckan över att bli älskad för den man är.',
  'Directors': ' Mårten Klingberg',
  'Genre': 'Drama',
  'Original_language': ' Svenska ',
  'Original_title': ' Min pappa Marianne'},
 {'Actors': ' Arndís Hrönn Egilsdóttir, Hinrik Ólafsson, Sigurður '
            'Sigurjónsson, Hannes Óli Ágústsson, Ragnhildur Gísladóttir, '
            'Sveinn Ólafur Gunnarsson, Jens Albinus',
  'Date': ' 17 jul 2020',
  'Description': 'Den viljestarka, upproriska mjölkbonden Inga bestämmer sig '
                 'för att förklara krig mot det kooperativ som styr med '
                 'maffiametoder i ett litet isländskt samhälle. Oddsen är emot '
                 'henne efter makens plötsliga bortgång, gården är skuldsatt '
                 'och mjölkpriserna pressade. Men Inga sätter man sig inte på '
                 'i första taget! När hon konfronterats med kooperativets '
                 'hänsynslöse chef står det klart för henne att hon måste få '
                 'med sig byns övriga bönder på sin sida för att vinna.',
  'Directors': ' Grímur Hákonarson',
  'Genre': 'Drama',
  'Original_language': ' Isländska ',
  'Original_title': ' The County/Héraðið'},
 {'Actors': ' Choi Woo-shik, Park So-dam, Chang Hyae-Jin, Song Kang-ho',
  'Date': ' 20 dec 2019',
  'Description': 'Ki-taeks familj är en färgstark skara som hankar sig fram '
                 'genom livet med hjälp av påhittighet och list. Men några '
                 'pengar har de inte. Så när sonen, Ki-Woo, erbjuds jobbet som '
                 'privatlärare till dottern i en rik familj så tvekar han inte '
                 'en sekund. Väl på plats börjar han smida planer för resten '
                 'av sin familj som en efter en får jobb i det nya huset. Men '
                 'lögnerna blir allt fler och det dröjer inte länge innan '
                 'situationen är helt utom kontroll ...',
  'Directors': ' Bong Joon-ho',
  'Genre': 'Komedi, Drama',
  'Original_language': ' Koreanska ',
  'Original_title': ' Gisaengchung'},
 {'Actors': ' Gang Dong-won, Lee Jung-hyun, John D. Michaels',
  'Date': ' 5 aug 2020',
  'Description': '"Peninsula" äger rum fyra år efter zombieutbrottet i "Train '
                 'to Busan".',
  'Directors': ' Yeon Sang-ho',
  'Genre': 'Action, Skräck',
  'Original_language': ' Koreanska ',
  'Original_title': ' Peninsula'},
 {'Actors': ' Daniel Kaluuya, Jodie Turner-Smith, Bokeem Woodbine, Chloë '
            'Sevigny, Flea , John Sturgill Simpson, Indya Moore',
  'Date': ' 6 mar 2020',
  'Description': 'Både hyllad och högaktuell, nu kommer Queen & Slim på bio '
                 'igen! En kärlekshistoria som\n'
                 'skildrar våldet och rasismen i USA. Med oscarnominerade '
                 'Daniel Kaluuya och Jodie Turner-Smith i huvudrollerna.',
  'Directors': ' Melina Matsoukas',
  'Genre': 'Drama',
  'Original_language': ' Engelska ',
  'Original_title': ' Queen & Slim'},
 {'Actors': ' Taron Egerton, Jamie Bell, Bryce Dallas Howard, Richard Madden',
  'Date': ' 29 maj 2019',
  'Description': 'Berättelsen om legendaren Elton Johns liv, från de tidiga '
                 'åren som underbarn vid Royal Academy of Music genom hans '
                 'långa och betydande musikaliska samarbete med Bernie Taupin.',
  'Directors': ' Dexter Fletcher',
  'Genre': 'Biografi, Drama, Musik',
  'Original_language': ' Engelska ',
  'Original_title': ' Rocketman'},
 {'Actors': ' Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams',
  'Date': ' 24 jun 2020',
  'Description': 'Tre år efter Dödsstjärnans förintelse har Imperiets makt '
                 'åter stigit. Efter att rebellerna brutalt övermannas av '
                 'imperiet på isplaneten Hoth börjar Luke Skywalker sin '
                 'jedi-träning med den uråldrige jedimästaren Yoda, medan hans '
                 'vänner förföljs av Darth Vader.',
  'Directors': ' Irvin Kershner',
  'Genre': 'Action, Äventyr, Sci-Fi',
  'Original_language': ' Engelska ',
  'Original_title': ' Star Wars: The Empire Strikes Back'},
 {'Actors': ' Jim Carrey, James Marsden, Neal Mcdonough',
  'Date': ' 19 feb 2020',
  'Description': 'Sonics försöker hantera det märkliga livet på jorden '
                 'tillsammans med sin nyfunna, mänskliga bästa vän Tom '
                 'Wachowski. Sonic och Tom samarbetar för att försöka stoppa '
                 'den skurkaktiga Dr Robotnik från att fånga Sonic och använda '
                 'sina enorma krafter för att ta över världen.',
  'Directors': ' Jeff Fowler',
  'Genre': 'Action, Äventyr, Komedi, Familj',
  'Original_language': ' Engelska ',
  'Original_title': ' Sonic the Hedgehog'},
 {'Actors': ' Christian Bale, Heath Ledger, Maggie Gyllenhaal, Gary Oldman, '
            'Michael Caine, Morgan Freeman, Aaron Eckhart',
  'Date': ' 24 jun 2020',
  'Description': 'Nu har den mörke riddaren bestämt sig: han ska en gång för '
                 'alla få ett slut på den organiserade brottsligheten i Gotham '
                 'City. Till sin hjälp har han polischef Jim Gordon och '
                 'åklagare Harvey Dent - och de visar sig vara en sällsynt bra '
                 'brottsbekämpartrio. Men snart stöter de på patrull, då den '
                 'genialiske mästerskurken Jokern träder in på spelplanen. Han '
                 'skapar snabbt total anarki i staden och tvingar Batman '
                 'farligt nära fel sida av lagen.',
  'Directors': ' Christopher Nolan',
  'Genre': 'Action, Drama',
  'Original_language': ' Engelska ',
  'Original_title': ' The Dark Knight'},
 {'Actors': ' Christian Bale, Tom Hardy, Marion Cotillard, Anne Hathaway, '
            'Morgan Freeman, Michael Caine',
  'Date': ' 24 jun 2020',
  'Description': 'Nu återvänder Christopher Nolan med den episka avslutande '
                 'delen i Dark Knight-trilogin.',
  'Directors': ' Christopher Nolan',
  'Genre': 'Action, Äventyr',
  'Original_language': ' Engelska ',
  'Original_title': ' The Dark Knight Rises'},
 {'Actors': ' Matthew McConaughey, Colin Farrell, Hugh Grant, Charlie Hunnam, '
            'Henry Golding, Michelle Dockery, Jeremy Strong, Eddie Marsan',
  'Date': ' 26 feb 2020',
  'Description': 'Amerikanen Mickey Pearson har skapat ett mycket lönsamt '
                 'marijuanaimperium i London. När ryktet sprids att Pearson '
                 'vill sälja sin lukrativa verksamhet till högstbjudande '
                 'sparkar det igång intriger, planer, mutor och utpressning.',
  'Directors': ' Guy Ritchie',
  'Genre': 'Action, Komedi',
  'Original_language': ' Engelska ',
  'Original_title': ' The Gentlemen'},
 {'Actors': ' Pete Davidson, Marisa Tomei, Bel Powley, Steve Buscemi',
  'Date': ' 24 jul 2020',
  'Description': 'Scotts liv sattes på paus när hans pappa, som var brandman, '
                 'dog när Scott var sju år. Nu är han i 20-årsåldern, har '
                 'uppnått väldigt lite och hans dröm om att bli tatuerare '
                 'verkar ligga långt utom räckhåll. När hans ambitiösa yngre '
                 'syster ger sig iväg till college bor Scott fortfarande kvar '
                 'hos sin utmattade mamma, som är akutsjuksköterska, och '
                 'tillbringar dagarna med att röka gräs och hänga med polarna '
                 'Oscar, Igor och Richie. I hemlighet har han ihop det med med '
                 'sin barndomsvän Kelsey.',
  'Directors': ' Judd Apatow',
  'Genre': 'Komedi',
  'Original_language': ' Engelska ',
  'Original_title': ' The King of Staten Island'},
 {'Actors': ' Orlando Bloom, Scott Eastwood, Caleb Landry Jones',
  'Date': ' 17 jul 2020',
  'Description': 'Den sanna historien om slaget vid Kamdesh i Afghanistan, där '
                 '53 amerikanska soldater omringades av 400 talibanska '
                 'rebeller vid världens dödligaste militära utpost, Outpost '
                 'Keaton. Basen byggdes ursprungligen för att engagera '
                 'lokalbefolkningen i samhällsprojekt, men var belägen längst '
                 'ner i en brant dal och var under konstant hot att '
                 'attackeras. När beslut äntligen togs om att stänga basen '
                 'fick den talibanska gruppen reda på det och attackerade med '
                 'full kraft. Baserad på bästsäljande roman av CNN:s '
                 'korrespondent Jake Tapper.',
  'Directors': ' Rod Lurie',
  'Genre': 'Krig, Drama',
  'Original_language': ' Engelska ',
  'Original_title': ' The Outpost'},
 {'Actors': ' Shia LaBeouf, Dakota Johnson, John Hawkes, Thomas Haden Church, '
            'Bruce Dern, Zack Gottsagen',
  'Date': ' 20 mar 2020',
  'Description': 'Zak är en ung man med Downs syndrom. Han rymmer från ett '
                 'sjukhem för att följa sin dröm och träna på den '
                 'professionella wrestling-skolan med sin stora idol, The Salt '
                 'Water Redneck. Efter ett udda händelseförlopp träffar han '
                 'Tyler, en småkriminell på flykt, som blir Zaks osannolika '
                 'tränare och allierade. Tillsammans upplever de livet, '
                 'dricker whisky, fångar fisk och Zak lär sig både att simma '
                 'och skjuta gevär. När Eleanor, en snäll sköterska som '
                 'anklagas för Zaks rymning, hittar dem övertygar de henne att '
                 'följa med på deras resa.',
  'Directors': ' Tyler Nilson, Michael Schwartz',
  'Genre': 'Äventyr, Komedi',
  'Original_language': ' Engelska ',
  'Original_title': ' The Peanut Butter Falcon'},
 {'Actors': ' Yoo Gong, Dong-Seok Ma, Yu-Mi Jeong',
  'Date': ' 3 mar 2017',
  'Description': 'Passagerarna på expresståget mellan Seoul och Busan '
                 'upptäcker att de är fast på tåget mitt under en '
                 'Zombie-epidemi. Kaos och förvirring råder både utanför och '
                 'inne på tåget, men ett gäng överlevare gör allt vad de kan '
                 'för att inte bli infekterade själva eller att hamna i '
                 'händerna på alla blodtörstiga zombies.',
  'Directors': ' Sang-Ho Yeon',
  'Genre': 'Action, Skräck, Thriller',
  'Original_language': ' Koreanska ',
  'Original_title': ' Busanhaeng'},
 {'Actors': ' Russell Crowe, Jimmi Simpson, Gabriel Bateman, Caren Pistorius',
  'Date': ' 31 jul 2020',
  'Description': 'En stressad mamma råkar tuta på fel bil vid ett rödljus '
                 'under rusningstid. Ett ödesdigert misstag som gör henne '
                 'själv och alla hon älskar till måltavlor för en man som '
                 'tröttnat på allt och bestämt sig för att lära världen en '
                 'sista läxa.',
  'Directors': ' Derrick Borte',
  'Genre': 'Thriller',
  'Original_language': ' Engelska ',
  'Original_title': ' Unhinged'},
 {'Actors': ' Lambert Wilson, Olga Kurylenko, Sidse Babett Knudsen, Riccardo '
            'Scamarcio, Eduardo Noriega',
  'Date': ' 17 jul 2020',
  'Description': 'Nio översättare har lyckats få ett riktigt drömjobb. '
                 'Tillsammans ska de översätta den avslutande delen av en '
                 'omåttligt populär fantasytrilogi. Hemlighetsmakeriet inför '
                 'boksläppet är på den nivån att de får utföra arbetet '
                 'isolerade i en lyxigt inredd bunker.',
  'Directors': ' Régis Roinsard',
  'Genre': 'Drama, Thriller',
  'Original_language': ' Engelska,  Franska ',
  'Original_title': ' Les traducteurs'}]

def get_movie_list():
  df = read_file()
  movie_list = df.values.tolist()
  #Extract the image names from the urls. Needed later to find local copies in Flask/static/images 
  for movie in movie_list:
    url=movie[-1]
    url_path=url.split('/')
    name = url_path[len(url_path)-1]
    movie[-1] = name
  return movie_list