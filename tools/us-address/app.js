/* Test-address generator. All values are fictional or deliberately invalid.
   For form filling / QA / development only. */
(function () {
  'use strict';

  // ---------- shared name / street pools ----------
  var NAMES = {
    anglo: {
      m: ['James','Robert','Michael','David','William','Richard','Joseph','Thomas','Charles','Daniel','Matthew','Andrew','Joshua','Kevin','Brian','George','Edward','Jason','Ryan','Noah','Liam','Ethan','Lucas'],
      f: ['Mary','Patricia','Jennifer','Linda','Elizabeth','Barbara','Susan','Jessica','Sarah','Karen','Nancy','Lisa','Emily','Amanda','Melissa','Laura','Chloe','Sophie','Olivia','Emma','Ava','Mia','Grace','Alice'],
      l: ['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Wilson','Anderson','Taylor','Moore','Thomas','Jackson','White','Harris','Clark','Lewis','Walker','Hall','Young','King','Wright','Scott']
    },
    france: {
      m: ['Pierre','Jean','Michel','Alain','Philippe','Nicolas','Julien','Antoine','Thomas','Alexandre','Maxime','Lucas','Hugo','Gabriel','Louis'],
      f: ['Marie','Sophie','Nathalie','Isabelle','Celine','Camille','Julie','Emma','Lea','Chloe','Manon','Louise','Alice','Clara','Amandine'],
      l: ['Martin','Bernard','Dubois','Thomas','Robert','Richard','Petit','Durand','Leroy','Moreau','Simon','Laurent','Lefebvre','Michel','Garcia']
    },
    germany: {
      m: ['Hans','Jurgen','Klaus','Wolfgang','Stefan','Dieter','Michael','Thomas','Andreas','Matthias','Lukas','Jonas','Maximilian','Felix','Leon'],
      f: ['Maria','Anna','Ulrike','Gabriele','Hannelore','Petra','Sabine','Karin','Claudia','Stefanie','Lena','Mia','Emma','Hannah','Sophie'],
      l: ['Muller','Schmidt','Schneider','Fischer','Weber','Meyer','Wagner','Becker','Schulz','Hoffmann','Schaffer','Koch','Bauer','Richter','Klein']
    },
    japan: {
      m: ['Haruto','Sotaro','Yuto','Ren','Shota','Kaito','Riku','Yuki','Daiki','Takumi','Hiroki','Kenta','Sho','Ryo','Jun'],
      f: ['Sakura','Yui','Hana','Mio','Aoi','Rin','Mei','Hina','Kotone','Emi','Yuna','Haruka','Chie','Aya','Nana'],
      l: ['Sato','Suzuki','Takahashi','Tanaka','Watanabe','Ito','Yamamoto','Nakamura','Kobayashi','Kato','Yoshida','Yamada','Nishi','Ikeda','Hasegawa']
    },
    korea: {
      m: ['Minjun','Seojun','Jiho','Doyun','Jaehyun','Hyunwoo','Seungmin','Yejun','Haneul','Taeho','Junseo','Siwoo','Woojin','Sungho','Kangmin'],
      f: ['Seoyeon','Jiwoo','Somin','Yuna','Haeun','Jisoo','Mina','Sora','Nari','Bora','Doyeon','Chaewon','Yerin','Hana','Subin'],
      l: ['Kim','Lee','Park','Choi','Jeong','Kang','Cho','Yoon','Jang','Lim','Han','Oh','Seo','Shin','Hwang']
    },
    latineurope: {
      m: ['Marco','Alessandro','Francesco','Giulia','Luca','Andrea','Stefano','Javier','Carlos','Diego','Pablo','Sergio','Antonio','Manuel','Rafael'],
      f: ['Giulia','Francesca','Alessia','Sofia','Chiara','Martina','Maria','Laura','Carmen','Lucia','Marta','Elena','Isabel','Paula','Sara'],
      l: ['Rossi','Ferrari','Russo','Bianchi','Romano','Gallo','Costa','Garcia','Fernandez','Gonzalez','Rodriguez','Lopez','Martinez','Sanchez','Moreno']
    },
    netherlands: {
      m: ['Jan','Pieter','Jeroen','Bram','Sven','Thomas','Lucas','Daan','Sem','Tim','Kees','Maarten','Ruben','Willem','Floris'],
      f: ['Marieke','Annelies','Sanne','Lotte','Emma','Sophie','Eva','Mila','Noa','Fenna','Bente','Lieke','Amber','Jade','Roos'],
      l: ['Janssen','de Vries','van den Berg','Bakker','Visser','Smit','Meijer','de Boer','Mulder','Dijkstra','van Dijk','Hoving','Postma','Kuiper','van Leeuwen']
    },
    nordic: {
      m: ['Anders','Erik','Lars','Nils','Johan','Karl','Olof','Gustav','Magnus','Hakan','Bjorn','Sven','Mikael','Tomas','Fredrik'],
      f: ['Anna','Emma','Maria','Karin','Linn','Sara','Maja','Elin','Amanda','Johanna','Sofia','Alva','Ida','Ebba','Freja'],
      l: ['Andersson','Johansson','Karlsson','Nilsson','Eriksson','Larsson','Olsson','Persson','Svensson','Gustafsson','Lindberg','Berg','Axelsson','Bergstrom','Ek']
    },
    brazil: {
      m: ['Joao','Pedro','Paulo','Carlos','Lucas','Rafael','Felipe','Bruno','Gustavo','Andre','Diego','Thiago','Marcelo','Rodrigo','Caio'],
      f: ['Maria','Ana','Juliana','Beatriz','Larissa','Gabriela','Camila','Bruna','Luiza','Fernanda','Patricia','Isabela','Carla','Renata','Tatiana'],
      l: ['Silva','Santos','Oliveira','Souza','Lima','Ferreira','Costa','Gomes','Martins','Araujo','Melo','Barbosa','Carvalho','Ribeiro','Pereira']
    },
    india: {
      m: ['Raj','Amit','Vikram','Arjun','Rohan','Aditya','Sanjay','Deepak','Manish','Karthik','Rahul','Nikhil','Suresh','Ankit','Vivek'],
      f: ['Priya','Neha','Anjali','Pooja','Kavya','Sneha','Divya','Meera','Isha','Riya','Nisha','Shreya','Aditi','Lakshmi','Sunita'],
      l: ['Sharma','Verma','Patel','Singh','Kumar','Reddy','Mehta','Gupta','Iyer','Nair','Rao','Joshi','Desai','Chopra','Malhotra']
    },
    mexico: {
      m: ['Juan','Jose','Carlos','Miguel','Luis','Alejandro','Javier','Fernando','Ricardo','Diego','Emilio','Santiago','Pablo','Hector','Raul'],
      f: ['Maria','Guadalupe','Ana','Laura','Sofia','Valeria','Fernanda','Mariana','Daniela','Paola','Alejandra','Rosa','Elena','Lucia','Patricia'],
      l: ['Hernandez','Garcia','Martinez','Gonzalez','Lopez','Rodriguez','Perez','Sanchez','Ramirez','Torres','Flores','Rivera','Gomez','Diaz','Reyes']
    },
    china: {
      m: ['Wei','Ming','Jie','Hao','Jun','Lei','Tao','Bin','Kai','Yang','Chen','Yu','Xiang','Ning','Hui'],
      f: ['Li','Hua','Min','Jing','Yan','Mei','Ling','Xin','Yue','Fang','Na','Shan','Qin','Wen','Xia'],
      l: ['Wang','Li','Zhang','Liu','Chen','Yang','Zhao','Huang','Zhou','Wu','Xu','Sun','Ma','Zhu','Hu']
    }
  };

  var STREET_WEST = ['Maple','Oak','Cedar','Pine','Elm','Washington','Lincoln','Madison','Main','Market','High','Church','Park','Walnut','Birch','Willow','Rose','Lake','Hill','Sunset','Riverside','Forest','Valley','Ridge','Broadway','Green','Bay','Franklin','Clark','Union'];
  var SUFFIX_WEST = ['St','Ave','Rd','Blvd','Dr','Ln','Ct','Way','Pl'];
  var STREET_JP = ['Sakura','Nakano','Kita','Minami','Higashi','Nishi','Chuo','Yamato','Asahi','Momiji','Aoba','Miyuki','Shin','Kanda','Otsuka'];
  var STREET_KR = ['Gangnam','Sejong','Jongno','Euljiro','Teheran','Banpo','Yongsan','Hongik','Sinchon','Gwanghwamun','Namdaemun','Dongdaemun','Itaewon','Samseong','Yeoksam'];
  var SUFFIX_ASIA = ['-cho','-dori','-ro','-gu','-dong'];

  var COMPANIES = ['Northstar Labs','Acme Corp','Bluewave Media','Summit Systems','Pioneer Group','Vertex Solutions','Cedar Works','Orion Digital','Harbor Point LLC','Ironwood Partners'];
  var OCCUPATIONS = ['Software Engineer','Marketing Manager','Accountant','Teacher','Sales Representative','Data Analyst','Operations Manager','Customer Support','Project Manager','Designer','Consultant','Researcher'];
  // Public, non-functional test card numbers (Luhn-valid, no real account)
  var TEST_CARDS = [
    ['Visa','4111 1111 1111 1111'],
    ['Mastercard','5500 0000 0000 0004'],
    ['Amex','3782 822463 10005'],
    ['Discover','6011 1111 1111 1117']
  ];
  var EMAIL_DOMAINS = ['example.com','example.net','example.org','testmail.example'];

  // Fictional identity portraits — each record gets one at random.
  var AVATARS = [
    { src: '/img/aliens/qmark-pixel.png', name: 'Unknown' },
    { src: '/img/aliens/octopus-suit.png', name: 'Inky' },
    { src: '/img/aliens/cyborg-a.png', name: 'Unit-9' },
    { src: '/img/aliens/nebula-a.png', name: 'Nebula' },
    { src: '/img/aliens/human-b.png', name: 'Office Worker' }
  ];

  // ---------- helpers ----------
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function rnd(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
  function pad(n, len) { var s = String(n); while (s.length < len) s = '0' + s; return s; }
  function letters(n) { var s = ''; for (var i = 0; i < n; i++) s += String.fromCharCode(65 + rnd(0, 25)); return s; }
  function digit() { return String(rnd(0, 9)); }
  function alnum() { return letters(1) + digit() + letters(1); }

  // ---------- countries ----------
  // zone: [code, name, taxFreeFlag, ['City|zipPrefix', ...], [areaCodes...]]
  var US_ZONES = [
    ['AL','Alabama',0,['Birmingham|352','Montgomery|361','Huntsville|358','Mobile|366'],['205','334','256','251']],
    ['AK','Alaska',1,['Anchorage|995','Fairbanks|997','Juneau|998','Sitka|998'],['907']],
    ['AZ','Arizona',0,['Phoenix|850','Tucson|857','Mesa|852','Scottsdale|852'],['602','480','623','520']],
    ['AR','Arkansas',0,['Little Rock|722','Fayetteville|727','Fort Smith|729'],['501','479','870']],
    ['CA','California',0,['Los Angeles|900','San Diego|921','San Jose|951','San Francisco|941','Sacramento|958'],['213','310','415','650','408','619','858','916','925']],
    ['CO','Colorado',0,['Denver|802','Colorado Springs|809','Aurora|800','Boulder|803'],['303','720','719','970']],
    ['CT','Connecticut',0,['Hartford|061','Bridgeport|066','New Haven|065','Stamford|069'],['203','860']],
    ['DE','Delaware',1,['Wilmington|198','Dover|199','Newark|197','Middletown|197'],['302']],
    ['DC','District of Columbia',0,['Washington|200','Washington|202','Washington|205'],['202']],
    ['FL','Florida',0,['Miami|331','Orlando|328','Tampa|336','Jacksonville|322','St. Petersburg|337'],['305','321','407','813','904','727']],
    ['GA','Georgia',0,['Atlanta|303','Augusta|309','Columbus|319','Savannah|314'],['404','470','770','678','912','706']],
    ['HI','Hawaii',0,['Honolulu|968','Pearl City|967','Hilo|967'],['808']],
    ['ID','Idaho',0,['Boise|837','Meridian|836','Idaho Falls|834'],['208']],
    ['IL','Illinois',0,['Chicago|606','Aurora|605','Rockford|611','Springfield|627'],['312','773','630','847','217']],
    ['IN','Indiana',0,['Indianapolis|462','Fort Wayne|468','Evansville|477','South Bend|466'],['317','260','812','574']],
    ['IA','Iowa',0,['Des Moines|503','Cedar Rapids|524','Davenport|528'],['515','319','563','712']],
    ['KS','Kansas',0,['Wichita|672','Overland Park|662','Kansas City|661','Topeka|666'],['316','785','913']],
    ['KY','Kentucky',0,['Louisville|402','Lexington|405','Bowling Green|421','Covington|410'],['502','859','270']],
    ['LA','Louisiana',0,['New Orleans|701','Baton Rouge|708','Shreveport|711','Metairie|700'],['504','225','318','985']],
    ['ME','Maine',0,['Portland|041','Lewiston|042','Bangor|044'],['207']],
    ['MD','Maryland',0,['Baltimore|212','Columbia|210','Germantown|208','Silver Spring|209'],['410','301','443']],
    ['MA','Massachusetts',0,['Boston|021','Worcester|016','Springfield|011','Lowell|018'],['617','781','978','508','413']],
    ['MI','Michigan',0,['Detroit|482','Grand Rapids|495','Warren|480','Ann Arbor|481'],['313','586','810','248','734','269']],
    ['MN','Minnesota',0,['Minneapolis|554','Saint Paul|551','Rochester|559','Duluth|558'],['612','651','763','952','507','218']],
    ['MS','Mississippi',0,['Jackson|392','Gulfport|395','Southaven|386'],['601','662','228']],
    ['MO','Missouri',0,['Kansas City|641','Saint Louis|631','Springfield|658','Columbia|652'],['816','314','573','660','417']],
    ['MT','Montana',1,['Billings|591','Missoula|598','Great Falls|594','Bozeman|597','Helena|596'],['406']],
    ['NE','Nebraska',0,['Omaha|681','Lincoln|685','Bellevue|680'],['402','308']],
    ['NV','Nevada',0,['Las Vegas|891','Henderson|890','Reno|895','Carson City|897'],['702','775']],
    ['NH','New Hampshire',1,['Manchester|031','Nashua|030','Concord|033','Derry|030','Dover|038'],['603']],
    ['NJ','New Jersey',0,['Newark|071','Jersey City|073','Paterson|075','Elizabeth|072'],['973','201','908','732','856','609']],
    ['NM','New Mexico',0,['Albuquerque|871','Las Cruces|880','Rio Rancho|871','Santa Fe|875'],['505','575']],
    ['NY','New York',0,['New York|100','Brooklyn|112','Queens|113','Buffalo|142','Rochester|146','Albany|122'],['212','718','917','646','585','716','518']],
    ['NC','North Carolina',0,['Charlotte|282','Raleigh|276','Greensboro|274','Durham|277','Asheville|288'],['704','919','336','828','252','910']],
    ['ND','North Dakota',0,['Fargo|581','Bismarck|585','Grand Forks|582'],['701']],
    ['OH','Ohio',0,['Columbus|432','Cleveland|441','Cincinnati|452','Toledo|436','Akron|443'],['614','216','513','419','330','440']],
    ['OK','Oklahoma',0,['Oklahoma City|731','Tulsa|741','Norman|730','Broken Arrow|740'],['405','918','580']],
    ['OR','Oregon',1,['Portland|972','Eugene|974','Salem|973','Gresham|970','Hillsboro|971'],['503','971','541']],
    ['PA','Pennsylvania',0,['Philadelphia|191','Pittsburgh|152','Allentown|181','Erie|165'],['215','267','412','724','610','814']],
    ['RI','Rhode Island',0,['Providence|029','Cranston|029','Warwick|028'],['401']],
    ['SC','South Carolina',0,['Columbia|292','Charleston|294','North Charleston|294'],['803','843']],
    ['SD','South Dakota',0,['Sioux Falls|571','Rapid City|577','Aberdeen|574'],['605']],
    ['TN','Tennessee',0,['Nashville|372','Memphis|381','Knoxville|379','Chattanooga|374'],['615','901','865','423','931']],
    ['TX','Texas',0,['Houston|770','San Antonio|782','Dallas|752','Austin|787','Fort Worth|761','El Paso|799'],['713','832','281','210','972','469','512','817','915']],
    ['UT','Utah',0,['Salt Lake City|841','Provo|846','West Valley City|841','Ogden|844'],['801','385','435']],
    ['VT','Vermont',0,['Burlington|054','Essex|054','Montpelier|056','Rutland|057'],['802']],
    ['VA','Virginia',0,['Virginia Beach|234','Norfolk|235','Chesapeake|233','Richmond|232','Alexandria|223'],['757','804','703','540']],
    ['WA','Washington',0,['Seattle|981','Spokane|992','Tacoma|984','Vancouver|986','Bellevue|980'],['206','509','253','360','425']],
    ['WV','West Virginia',0,['Charleston|253','Huntington|257','Morgantown|265'],['304','681']],
    ['WI','Wisconsin',0,['Milwaukee|532','Madison|537','Green Bay|543','Kenosha|531'],['414','608','920','262']],
    ['WY','Wyoming',0,['Cheyenne|820','Casper|826','Laramie|820'],['307']]
  ];

  var COUNTRIES = [
    { code:'US', name:'United States', regionLabel:'State', regionCodeLabel:'State code', postalLabel:'ZIP code', taxFree:true, pool:'anglo', street:'west',
      zones:US_ZONES,
      postal:function(p){return p + pad(rnd(1,99),2);},
      phone:function(a){return '('+a+') '+rnd(200,989)+'-'+pad(rnd(0,9999),4);},
      id:function(){return pick(['666','900','901','902','903','904','905','906','907','908','909'])+'-'+pad(rnd(10,89),2)+'-'+pad(rnd(1000,9999),4);} },

    { code:'GB', name:'United Kingdom', regionLabel:'Country', regionCodeLabel:'Country code', postalLabel:'Postcode', taxFree:false, pool:'anglo', street:'west',
      zones:[
        ['ENG','England',0,['London|SW1A','Manchester|M1','Birmingham|B1','Bristol|BS1','Leeds|LS1','Liverpool|L1'],['020','0161','0121','0117','0113','0151']],
        ['SCT','Scotland',0,['Edinburgh|EH1','Glasgow|G1','Aberdeen|AB10','Dundee|DD1'],['0131','0141','01224','01382']],
        ['WLS','Wales',0,['Cardiff|CF10','Swansea|SA1','Bangor|LL57'],['029','01792','01248']],
        ['NIR','Northern Ireland',0,['Belfast|BT1','Derry|BT48','Lisburn|BT27'],['028']]
      ],
      postal:function(p){return p+' '+rnd(1,9)+letters(2);},
      phone:function(a){return a+' '+rnd(100,999)+' '+pad(rnd(0,9999),4);},
      id:function(){return 'QQ '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2)+' '+pick(['A','B','C','D']);} },

    { code:'FR', name:'France', regionLabel:'Region', regionCodeLabel:'Region code', postalLabel:'Postcode', taxFree:false, pool:'france', street:'west',
      zones:[
        ['IDF','Ile-de-France',0,['Paris|75','Versailles|78','Creteil|94','Bobigny|93'],['1']],
        ['PAC','Provence-Alpes-Cote d Azur',0,['Marseille|13','Nice|06','Toulon|83','Aix-en-Provence|13'],['4']],
        ['ARA','Auvergne-Rhone-Alpes',0,['Lyon|69','Grenoble|38','Saint-Etienne|42','Clermont-Ferrand|63'],['4']],
        ['NAQ','Nouvelle-Aquitaine',0,['Bordeaux|33','Limoges|87','Poitiers|86','Bayonne|64'],['5']],
        ['OCC','Occitanie',0,['Toulouse|31','Montpellier|34','Nimes|30','Perpignan|66'],['5']]
      ],
      postal:function(p){return p+pad(rnd(1,999),3);},
      phone:function(a){return '0'+a+' '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'DE', name:'Germany', regionLabel:'State', regionCodeLabel:'State code', postalLabel:'Postal code', taxFree:false, pool:'germany', street:'west',
      zones:[
        ['BY','Bavaria',0,['Munich|80','Nuremberg|90','Augsburg|86','Wurzburg|97'],['89','911','821','931']],
        ['BE','Berlin',0,['Berlin|10','Berlin|12','Berlin|13'],['30']],
        ['NW','North Rhine-Westphalia',0,['Cologne|50','Dusseldorf|40','Dortmund|44','Bonn|53'],['221','211','231','228']],
        ['HH','Hamburg',0,['Hamburg|20','Hamburg|21','Hamburg|22'],['40']],
        ['HE','Hesse',0,['Frankfurt|60','Wiesbaden|65','Kassel|34'],['69','611','561']],
        ['BW','Baden-Wuerttemberg',0,['Stuttgart|70','Mannheim|68','Karlsruhe|76','Freiburg|79'],['711','621','721','761']]
      ],
      postal:function(p){return p+pad(rnd(1,999),3);},
      phone:function(a){return '0'+a+' '+rnd(1000000,9999999);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'JP', name:'Japan', regionLabel:'Prefecture', regionCodeLabel:'Pref. code', postalLabel:'Postal code', taxFree:false, pool:'japan', street:'japan',
      zones:[
        ['13','Tokyo',0,['Tokyo|100','Shinjuku|160','Shibuya|150','Yokohama|220'],['03','03','03','045']],
        ['27','Osaka',0,['Osaka|530','Sakai|590','Toyonaka|560'],['06','072','06']],
        ['14','Kanagawa',0,['Yokohama|220','Kawasaki|210','Sagamihara|252'],['045','044','042']],
        ['23','Aichi',0,['Nagoya|450','Toyohashi|440','Okazaki|444'],['052','0532','0564']],
        ['01','Hokkaido',0,['Sapporo|060','Hakodate|040','Asahikawa|070'],['011','0138','0166']],
        ['40','Fukuoka',0,['Fukuoka|810','Kitakyushu|802','Kurume|830'],['092','093','0943']],
        ['26','Kyoto',0,['Kyoto|600','Uji|611','Maizuru|624'],['075','0774','0773']]
      ],
      postal:function(p){return p+'-'+pad(rnd(0,9999),4);},
      phone:function(a){return a+'-'+pad(rnd(1000,9999),4)+'-'+pad(rnd(1000,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'KR', name:'South Korea', regionLabel:'Province', regionCodeLabel:'Region code', postalLabel:'Postal code', taxFree:false, pool:'korea', street:'korea',
      zones:[
        ['11','Seoul',0,['Seoul|045','Gangnam|062','Jongno|030','Yongsan|043'],['02','02','02','02']],
        ['21','Busan',0,['Busan|489','Haeundae|481','Nampo|490'],['051','051','051']],
        ['23','Incheon',0,['Incheon|223','Bucheon|420','Namdong|216'],['032','032','032']],
        ['22','Daegu',0,['Daegu|419','Suseong|706','Dalseo|426'],['053','053','053']],
        ['29','Gyeonggi',0,['Suwon|163','Seongnam|132','Goyang|103','Yongin|171'],['031','031','031','031']]
      ],
      postal:function(p){return p+pad(rnd(10,99),2);},
      phone:function(a){return a+'-'+pad(rnd(1000,9999),4)+'-'+pad(rnd(1000,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'CA', name:'Canada', regionLabel:'Province', regionCodeLabel:'Prov. code', postalLabel:'Postal code', taxFree:false, pool:'anglo', street:'west',
      zones:[
        ['ON','Ontario',0,['Toronto|M5V','Ottawa|K1P','Hamilton|L8P','London|N6A'],['416','613','905','519']],
        ['QC','Quebec',0,['Montreal|H2Y','Quebec City|G1R','Laval|H7A'],['514','418','450']],
        ['BC','British Columbia',0,['Vancouver|V6B','Victoria|V8W','Surrey|V3T'],['604','250','778']],
        ['AB','Alberta',0,['Calgary|T2P','Edmonton|T5J','Red Deer|T4N'],['403','780','587']],
        ['MB','Manitoba',0,['Winnipeg|R3C','Brandon|R7A'],['204','431']]
      ],
      postal:function(p){return p+' '+digit()+pick('ABCDEFGHJKLMNPRSTVWXYZ'.split(''))+digit();},
      phone:function(a){return '('+a+') '+rnd(200,989)+'-'+pad(rnd(0,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'AU', name:'Australia', regionLabel:'State', regionCodeLabel:'State code', postalLabel:'Postcode', taxFree:false, pool:'anglo', street:'west',
      zones:[
        ['NSW','New South Wales',0,['Sydney|2000','Newcastle|2300','Wollongong|2500'],['02','02','02']],
        ['VIC','Victoria',0,['Melbourne|3000','Geelong|3220','Ballarat|3350'],['03','03','03']],
        ['QLD','Queensland',0,['Brisbane|4000','Gold Coast|4215','Cairns|4870'],['07','07','07']],
        ['WA','Western Australia',0,['Perth|6000','Fremantle|6160','Bunbury|6230'],['08','08','08']],
        ['SA','South Australia',0,['Adelaide|5000','Mount Gambier|5290'],['08','08']],
        ['TAS','Tasmania',0,['Hobart|7000','Launceston|7250'],['03','03']]
      ],
      postal:function(p){return p;},
      phone:function(a){return '('+a+') '+pad(rnd(1000,9999),4)+' '+pad(rnd(1000,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'IT', name:'Italy', regionLabel:'Region', regionCodeLabel:'Region code', postalLabel:'Postcode', taxFree:false, pool:'latineurope', street:'west',
      zones:[
        ['LAZ','Lazio',0,['Rome|001','Frosinone|031','Viterbo|011'],['06','0775','0761']],
        ['LOM','Lombardy',0,['Milan|201','Brescia|251','Bergamo|241'],['02','030','035']],
        ['CAM','Campania',0,['Naples|801','Salerno|841','Caserta|811'],['081','089','0823']],
        ['PIE','Piedmont',0,['Turin|101','Novara|281','Alessandria|151'],['011','0321','0131']],
        ['VEN','Veneto',0,['Venice|301','Verona|371','Padua|351'],['041','045','049']]
      ],
      postal:function(p){return p+pad(rnd(10,99),2);},
      phone:function(a){return a+' '+rnd(1000000,9999999);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'ES', name:'Spain', regionLabel:'Region', regionCodeLabel:'Region code', postalLabel:'Postcode', taxFree:false, pool:'latineurope', street:'west',
      zones:[
        ['MAD','Madrid',0,['Madrid|280','Alcala de Henares|288','Getafe|289'],['91','91','91']],
        ['CAT','Catalonia',0,['Barcelona|080','Girona|170','Tarragona|430'],['93','972','977']],
        ['AND','Andalusia',0,['Seville|410','Malaga|290','Granada|180'],['95','952','958']],
        ['VAL','Valencia',0,['Valencia|460','Alicante|030','Castellon|120'],['96','965','964']],
        ['GAL','Galicia',0,['Santiago|157','A Coruna|150','Vigo|362'],['981','981','986']]
      ],
      postal:function(p){return p+pad(rnd(10,99),2);},
      phone:function(a){return a+' '+pad(rnd(100,999),3)+' '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'NL', name:'Netherlands', regionLabel:'Province', regionCodeLabel:'Prov. code', postalLabel:'Postcode', taxFree:false, pool:'netherlands', street:'west',
      zones:[
        ['NH','North Holland',0,['Amsterdam|1011','Haarlem|2011','Almere|1311'],['020','023','036']],
        ['ZH','South Holland',0,['Rotterdam|3011','The Hague|2511','Leiden|2311'],['010','070','071']],
        ['UT','Utrecht',0,['Utrecht|3511','Amersfoort|3811','Hilversum|1211'],['030','033','035']],
        ['NB','North Brabant',0,['Eindhoven|5611','Tilburg|5011','Breda|4811'],['040','013','076']],
        ['GE','Gelderland',0,['Arnhem|6811','Nijmegen|6511','Apeldoorn|7311'],['026','024','055']]
      ],
      postal:function(p){return p+' '+letters(2);},
      phone:function(a){return a+' '+pad(rnd(100,999),3)+' '+pad(rnd(1000,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'SG', name:'Singapore', regionLabel:'District', regionCodeLabel:'District code', postalLabel:'Postal code', taxFree:false, pool:'china', street:'west',
      zones:[
        ['01','Central',0,['Singapore|018','Raffles Place|048','Orchard|023'],['6','6','6']],
        ['02','East',0,['Bedok|469','Pasir Ris|518','Tampines|529'],['6','6','6']],
        ['03','North',0,['Woodlands|738','Yishun|760','Sembawang|750'],['6','6','6']],
        ['04','West',0,['Jurong|608','Clementi|120','Bukit Batok|659'],['6','6','6']]
      ],
      postal:function(p){return p+pad(rnd(100,999),3);},
      phone:function(a){return a+pad(rnd(100,999),3)+' '+pad(rnd(1000,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'CH', name:'Switzerland', regionLabel:'Canton', regionCodeLabel:'Canton code', postalLabel:'Postal code', taxFree:false, pool:'germany', street:'west',
      zones:[
        ['ZH','Zurich',0,['Zurich|8000','Winterthur|8400','Uster|8610'],['44','52','44']],
        ['BE','Bern',0,['Bern|3011','Thun|3600','Biel|2501'],['31','33','32']],
        ['GE','Geneva',0,['Geneva|1201','Lancy|1122','Vernier|1214'],['22','22','22']],
        ['BS','Basel',0,['Basel|4001','Riehen|4125','Muttenz|4132'],['61','61','61']],
        ['VD','Vaud',0,['Lausanne|1003','Montreux|1820','Yverdon|1400'],['21','21','24']]
      ],
      postal:function(p){return p;},
      phone:function(a){return '0'+a+' '+pad(rnd(100,999),3)+' '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'SE', name:'Sweden', regionLabel:'County', regionCodeLabel:'County code', postalLabel:'Postal code', taxFree:false, pool:'nordic', street:'west',
      zones:[
        ['AB','Stockholm',0,['Stockholm|111','Solna|169','Huddinge|141'],['8','8','8']],
        ['O','Vastra Gotaland',0,['Gothenburg|411','Boraus|503','Trollhattan|311'],['31','33','32']],
        ['M','Skane',0,['Malmo|211','Lund|221','Helsingborg|252'],['40','46','42']],
        ['C','Uppsala',0,['Uppsala|752','Enkoping|744','Tierp|815'],['18','171','173']]
      ],
      postal:function(p){return p+' '+pad(rnd(10,99),2);},
      phone:function(a){return '0'+a+'-'+pad(rnd(100,999),3)+' '+pad(rnd(10,99),2)+' '+pad(rnd(10,99),2);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'BR', name:'Brazil', regionLabel:'State', regionCodeLabel:'State code', postalLabel:'Postal code', taxFree:false, pool:'brazil', street:'west',
      zones:[
        ['SP','Sao Paulo',0,['Sao Paulo|01310','Campinas|13010','Santos|11010'],['11','19','13']],
        ['RJ','Rio de Janeiro',0,['Rio de Janeiro|20040','Niteroi|24210','Petropolis|25600'],['21','21','24']],
        ['MG','Minas Gerais',0,['Belo Horizonte|30130','Uberlandia|38400','Juiz de Fora|36010'],['31','34','32']],
        ['PR','Parana',0,['Curitiba|80010','Londrina|86010','Foz do Iguacu|85860'],['41','43','45']],
        ['BA','Bahia',0,['Salvador|40010','Feira de Santana|44010','Itabuna|45600'],['71','75','73']]
      ],
      postal:function(p){return p+'-'+pad(rnd(100,999),3);},
      phone:function(a){return '('+a+') '+pad(rnd(10000,99999),5)+'-'+pad(rnd(1000,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'IN', name:'India', regionLabel:'State', regionCodeLabel:'State code', postalLabel:'PIN code', taxFree:false, pool:'india', street:'west',
      zones:[
        ['MH','Maharashtra',0,['Mumbai|400','Pune|411','Nagpur|440'],['22','20','712']],
        ['DL','Delhi',0,['New Delhi|110','Shahdara|110','Dwarka|110'],['11','11','11']],
        ['KA','Karnataka',0,['Bengaluru|560','Mysuru|570','Hubballi|580'],['80','821','836']],
        ['TN','Tamil Nadu',0,['Chennai|600','Coimbatore|641','Madurai|625'],['44','422','452']],
        ['UP','Uttar Pradesh',0,['Lucknow|226','Varanasi|221','Agra|282'],['522','542','562']]
      ],
      postal:function(p){return p+pad(rnd(1,999),3);},
      phone:function(a){return '+91 '+a+' '+pad(rnd(10000,99999),5)+' '+pad(rnd(10000,99999),5);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'MX', name:'Mexico', regionLabel:'State', regionCodeLabel:'State code', postalLabel:'Postal code', taxFree:false, pool:'mexico', street:'west',
      zones:[
        ['CMX','Mexico City',0,['Mexico City|060','Coyoacan|041','Polanco|115'],['55','55','55']],
        ['JAL','Jalisco',0,['Guadalajara|441','Zapopan|450','Tlaquepaque|455'],['33','33','33']],
        ['NLG','Nuevo Leon',0,['Monterrey|640','San Nicolas|664','Guadalupe|671'],['81','81','81']],
        ['MEX','State of Mexico',0,['Toluca|500','Naucalpan|530','Texcoco|561'],['722','55','595']],
        ['PUE','Puebla',0,['Puebla|720','Cholula|728','Tehuacan|757'],['222','222','238']]
      ],
      postal:function(p){return p+pad(rnd(10,99),2);},
      phone:function(a){return a+' '+pad(rnd(100,999),3)+' '+pad(rnd(1000,9999),4);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} },

    { code:'CN', name:'China', regionLabel:'Province', regionCodeLabel:'Prov. code', postalLabel:'Postal code', taxFree:false, pool:'china', street:'west',
      zones:[
        ['BJ','Beijing',0,['Beijing|100','Chaoyang|100','Haidian|100'],['10','10','10']],
        ['SH','Shanghai',0,['Shanghai|200','Pudong|201','Minhang|201'],['21','21','21']],
        ['GD','Guangdong',0,['Guangzhou|510','Shenzhen|518','Dongguan|523'],['20','755','769']],
        ['ZJ','Zhejiang',0,['Hangzhou|310','Ningbo|315','Wenzhou|325'],['571','574','577']],
        ['JS','Jiangsu',0,['Nanjing|210','Suzhou|215','Wuxi|214'],['25','512','510']]
      ],
      postal:function(p){return p+pad(rnd(1,999),3);},
      phone:function(a){return '0'+a+'-'+pad(rnd(10000000,99999999),8);},
      id:function(){return 'TEST'+pad(rnd(100000000,999999999),9);} }
  ];

  var COUNTRY_BY_CODE = {};
  COUNTRIES.forEach(function (c) { COUNTRY_BY_CODE[c.code] = c; });

  // ---------- generation ----------
  function chooseZone(country, mode, zoneCode) {
    var pool;
    if (mode === 'taxfree') pool = country.zones.filter(function (z) { return z[2] === 1; });
    else if (mode === 'zone') pool = country.zones.filter(function (z) { return z[0] === zoneCode; });
    else pool = country.zones;
    if (!pool.length) pool = country.zones;
    return pick(pool);
  }

  function streetFor(country, house) {
    if (country.street === 'japan') return pick(STREET_JP) + pick(SUFFIX_ASIA) + ' ' + house + ' ban';
    if (country.street === 'korea') return pick(STREET_KR) + ' ' + house;
    return house + ' ' + pick(STREET_WEST) + ' ' + pick(SUFFIX_WEST);
  }

  // opts: { country:'US', mode:'any'|'taxfree'|'zone', zone:'CA' }
  function generate(opts) {
    opts = opts || {};
    var country = COUNTRY_BY_CODE[opts.country] || COUNTRY_BY_CODE.US;
    var names = NAMES[country.pool] || NAMES.anglo;
    var zone = chooseZone(country, opts.mode, opts.zone);
    var cityZip = pick(zone[3]).split('|');
    var city = cityZip[0];
    var zipPrefix = cityZip[1];
    var gender = Math.random() < 0.5 ? 'Female' : 'Male';
    var first = pick(gender === 'Female' ? names.f : names.m);
    var last = pick(names.l);
    var year = rnd(1982, 2003);
    var house = rnd(102, 9898);
    var email = (first + '.' + last + rnd(1, 99)).toLowerCase().replace(/\s+/g, '') + '@' + pick(EMAIL_DOMAINS);
    var username = (first.charAt(0) + last + rnd(10, 99)).toLowerCase().replace(/\s+/g, '');
    var chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$';
    var pw = '';
    for (var i = 0; i < 12; i++) pw += chars.charAt(Math.floor(Math.random() * chars.length));
    var card = pick(TEST_CARDS);

    var rec = {
      'Full Name': first + ' ' + last,
      'Gender': gender,
      'Date of Birth': pad(rnd(1, 12), 2) + '/' + pad(rnd(1, 28), 2) + '/' + year,
      'Street Address': streetFor(country, house),
      'City': city
    };
    rec[country.regionLabel] = zone[1];
    rec[country.regionCodeLabel] = zone[0];
    rec[country.postalLabel] = country.postal(zipPrefix);
    rec['Phone'] = country.phone(pick(zone[4]));
    rec['Email'] = email;
    rec['Username'] = username;
    rec['Password'] = pw;
    rec['Occupation'] = pick(OCCUPATIONS);
    rec['Company'] = pick(COMPANIES);
    if (country.code === 'US') rec['SSN (invalid test value)'] = country.id();
    else rec['National ID (test)'] = country.id();
    rec['Card'] = card[0] + ' ' + card[1] + ' (test only)';
    rec._country = country.code;
    rec._taxFree = zone[2] === 1;
    rec._labels = { region: country.regionLabel, regionCode: country.regionCodeLabel, postal: country.postalLabel };
    rec._avatar = pick(AVATARS);
    rec._dossierId = '#' + (country.code === 'US' ? 'US' : country.code) + '-' + pad(rnd(1, 999), 3);
    return rec;
  }

  function fieldKeys(rec) {
    var keys = ['Full Name','Gender','Date of Birth','Street Address','City',
      rec._labels.region, rec._labels.regionCode, rec._labels.postal,
      'Phone','Email','Username','Password','Occupation','Company'];
    keys.push(rec._country === 'US' ? 'SSN (invalid test value)' : 'National ID (test)');
    keys.push('Card');
    return keys;
  }

  // ---------- DOM ----------
  if (typeof document !== 'undefined') {
    var countrySel = document.getElementById('country');
    var zoneSel = document.getElementById('zone');
    var freeOnly = document.getElementById('freeOnly');
    var count = document.getElementById('count');
    var output = document.getElementById('output');
    var currentCountry = 'US';
    var lastRecord = null;
    var ACTION_IDS = ['copyAll','exportJson','exportCsv','copyAllBottom'];

    function buildCountryOptions() {
      if (!countrySel) return;
      countrySel.innerHTML = COUNTRIES.map(function (c) {
        return '<option value="' + c.code + '">' + c.name + '</option>';
      }).join('');
      countrySel.value = currentCountry;
    }

    function buildZoneOptions() {
      if (!zoneSel) return;
      var country = COUNTRY_BY_CODE[currentCountry];
      var only = freeOnly && freeOnly.checked && country.taxFree;
      var pool = only ? country.zones.filter(function (z) { return z[2] === 1; }) : country.zones;
      var opts = ['<option value="">' + (only ? 'Tax-free only' : 'All ' + country.regionLabel.toLowerCase() + 's (random)') + '</option>'];
      pool.forEach(function (z) {
        opts.push('<option value="' + z[0] + '">' + z[1] + (z[2] === 1 ? ' (tax-free)' : '') + '</option>');
      });
      zoneSel.innerHTML = opts.join('');
      if (count) {
        count.textContent = only
          ? pool.length + ' tax-free ' + country.regionLabel.toLowerCase() + 's'
          : pool.length + ' ' + country.regionLabel.toLowerCase() + 's';
      }
    }

    function syncFreeUI() {
      var country = COUNTRY_BY_CODE[currentCountry];
      var show = !!country.taxFree;
      var row = document.getElementById('freeRow');
      if (row) row.hidden = !show;
      if (!show && freeOnly) freeOnly.checked = false;
      buildZoneOptions();
    }

    buildCountryOptions();
    syncFreeUI();

    if (countrySel) countrySel.addEventListener('change', function () {
      currentCountry = countrySel.value;
      syncFreeUI();
      lastRecord = null;
      if (output) output.innerHTML = '<p class="empty-state">Settings changed. Press Generate for a new dossier.</p>';
      var badge = document.getElementById('recordCount');
      if (badge) badge.textContent = '0 RECORD';
      var status = document.getElementById('status');
      if (status) status.textContent = 'Ready — one record will be generated';
      ACTION_IDS.forEach(function (id) { var b = document.getElementById(id); if (b) b.disabled = true; });
    });
    if (freeOnly) freeOnly.addEventListener('change', buildZoneOptions);

    function getOpts() {
      var country = COUNTRY_BY_CODE[currentCountry];
      if (freeOnly && freeOnly.checked && country.taxFree) return { country: currentCountry, mode: 'taxfree' };
      if (zoneSel && zoneSel.value) return { country: currentCountry, mode: 'zone', zone: zoneSel.value };
      return { country: currentCountry, mode: 'any' };
    }

    function copyText(text) {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).catch(function () { fallbackCopy(text); });
      } else fallbackCopy(text);
    }
    function fallbackCopy(text) {
      var ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); } catch (e) {}
      document.body.removeChild(ta);
    }
    function flash(btn) {
      var old = btn.textContent;
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = old; }, 1200);
    }

    function render(rec) {
      output.innerHTML = '';
      var card = document.createElement('article');
      card.className = 'record dossier';

      // dossier header — case id + clearance label
      var top = document.createElement('div');
      top.className = 'dossier-top';
      var caseId = document.createElement('span');
      caseId.className = 'dossier-id';
      caseId.textContent = rec._dossierId;
      var clearance = document.createElement('span');
      clearance.textContent = 'FICTIONAL IDENTITY / TEST DATA';
      top.appendChild(caseId);
      top.appendChild(clearance);
      card.appendChild(top);

      var main = document.createElement('div');
      main.className = 'dossier-main';

      // portrait with framing corners
      var photo = document.createElement('div');
      photo.className = 'dossier-photo';
      var img = document.createElement('img');
      img.src = rec._avatar.src;
      img.alt = 'Fictional portrait: ' + rec._avatar.name;
      photo.appendChild(img);
      ['c1', 'c2', 'c3', 'c4'].forEach(function (c) {
        var corner = document.createElement('span');
        corner.className = 'corner ' + c;
        photo.appendChild(corner);
      });
      var stamp = document.createElement('span');
      stamp.className = 'stamp';
      stamp.textContent = rec._avatar.name.toUpperCase();
      photo.appendChild(stamp);
      main.appendChild(photo);

      // address fields, same as before
      var info = document.createElement('div');
      info.className = 'dossier-info';
      var head = document.createElement('h3');
      head.textContent = COUNTRY_BY_CODE[rec._country].name + (rec._taxFree ? ' · Tax-free region' : '');
      info.appendChild(head);
      var dl = document.createElement('dl');
      fieldKeys(rec).forEach(function (key) {
        var row = document.createElement('div');
        row.className = 'row';
        var dt = document.createElement('dt');
        dt.textContent = key;
        var dd = document.createElement('dd');
        dd.textContent = rec[key];
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'copy-one';
        btn.textContent = 'Copy';
        btn.addEventListener('click', function () { copyText(String(rec[key])); flash(btn); });
        dd.appendChild(btn);
        row.appendChild(dt); row.appendChild(dd);
        dl.appendChild(row);
      });
      info.appendChild(dl);
      main.appendChild(info);
      card.appendChild(main);

      var foot = document.createElement('div');
      foot.className = 'dossier-foot';
      var footL = document.createElement('span');
      footL.appendChild(document.createTextNode('SUBJECT INDEXED — all fields '));
      var footB = document.createElement('b');
      footB.textContent = 'fictional / test only';
      footL.appendChild(footB);
      var footR = document.createElement('span');
      footR.textContent = 'DOSSIER ' + rec._dossierId + ' // TEST ADDRESS GENERATOR';
      foot.appendChild(footL);
      foot.appendChild(footR);
      card.appendChild(foot);

      output.appendChild(card);
    }

    function asText(rec) {
      return ['Record · ' + COUNTRY_BY_CODE[rec._country].name]
        .concat(fieldKeys(rec).map(function (k) { return k + ': ' + rec[k]; })).join('\n');
    }
    function download(name, text, type) {
      var blob = new Blob([text], { type: type });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = name;
      document.body.appendChild(a); a.click();
      document.body.removeChild(a);
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
    }

    function setActionsEnabled(on) {
      ACTION_IDS.forEach(function (id) {
        var b = document.getElementById(id);
        if (b) b.disabled = !on;
      });
    }

    var genBtn = document.getElementById('generate');
    if (genBtn) genBtn.addEventListener('click', function () {
      lastRecord = generate(getOpts());
      render(lastRecord);
      setActionsEnabled(true);
      var badge = document.getElementById('recordCount');
      if (badge) badge.textContent = '1 RECORD';
      var status = document.getElementById('status');
      if (status) status.textContent = '1 record generated · ' + COUNTRY_BY_CODE[lastRecord._country].name;
    });

    var copyAll = document.getElementById('copyAll');
    if (copyAll) copyAll.addEventListener('click', function () {
      if (!lastRecord) return;
      copyText(asText(lastRecord)); flash(copyAll);
    });
    var copyBottom = document.getElementById('copyAllBottom');
    if (copyBottom) copyBottom.addEventListener('click', function () {
      if (!lastRecord) return;
      copyText(asText(lastRecord)); flash(copyBottom);
    });
    var expJson = document.getElementById('exportJson');
    if (expJson) expJson.addEventListener('click', function () {
      if (!lastRecord) return;
      var o = {};
      fieldKeys(lastRecord).forEach(function (k) { o[k] = lastRecord[k]; });
      download('test-address.json', JSON.stringify(o, null, 2), 'application/json');
    });
    var expCsv = document.getElementById('exportCsv');
    if (expCsv) expCsv.addEventListener('click', function () {
      if (!lastRecord) return;
      var q = function (v) { return '"' + String(v).replace(/"/g, '""') + '"'; };
      var keys = fieldKeys(lastRecord);
      var lines = [keys.map(q).join(',')];
      lines.push(keys.map(function (k) { return q(lastRecord[k]); }).join(','));
      download('test-address.csv', '\ufeff' + lines.join('\n'), 'text/csv;charset=utf-8');
    });
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { generate: generate, COUNTRIES: COUNTRIES, fieldKeys: fieldKeys, COUNTRY_BY_CODE: COUNTRY_BY_CODE };
  }
})();
