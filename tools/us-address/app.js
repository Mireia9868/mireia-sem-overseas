/* US test-address generator. All values are fictional or deliberately invalid.
   For form filling / QA / development only. */
(function () {
  'use strict';

  // [code, full name, taxFree, cities(city|zipPrefix), area codes]
  var STATES = [
    ['AL','Alabama',0,['Birmingham|352','Montgomery|361','Huntsville|358','Mobile|366'],['205','334','256','251']],
    ['AK','Alaska',1,['Anchorage|995','Fairbanks|997','Juneau|998','Sitka|998'],['907']],
    ['AZ','Arizona',0,['Phoenix|850','Tucson|857','Mesa|852','Scottsdale|852'],['602','480','623','520']],
    ['AR','Arkansas',0,['Little Rock|722','Fayetteville|727','Fort Smith|729','Jonesboro|724'],['501','479','870']],
    ['CA','California',0,['Los Angeles|900','San Diego|921','San Jose|951','San Francisco|941','Sacramento|958'],['213','310','415','650','408','619','858','916','925']],
    ['CO','Colorado',0,['Denver|802','Colorado Springs|809','Aurora|800','Boulder|803'],['303','720','719','970']],
    ['CT','Connecticut',0,['Hartford|061','Bridgeport|066','New Haven|065','Stamford|069'],['203','860']],
    ['DE','Delaware',1,['Wilmington|198','Dover|199','Newark|197','Middletown|197'],['302']],
    ['DC','District of Columbia',0,['Washington|200','Washington|202','Washington|205'],['202']],
    ['FL','Florida',0,['Miami|331','Orlando|328','Tampa|336','Jacksonville|322','St. Petersburg|337'],['305','321','407','813','904','727']],
    ['GA','Georgia',0,['Atlanta|303','Augusta|309','Columbus|319','Savannah|314'],['404','470','770','678','912','706']],
    ['HI','Hawaii',0,['Honolulu|968','Pearl City|967','Hilo|967','Kailua|967'],['808']],
    ['ID','Idaho',0,['Boise|837','Meridian|836','Idaho Falls|834','Caldwell|836'],['208']],
    ['IL','Illinois',0,['Chicago|606','Aurora|605','Rockford|611','Springfield|627'],['312','773','630','847','217']],
    ['IN','Indiana',0,['Indianapolis|462','Fort Wayne|468','Evansville|477','South Bend|466'],['317','260','812','574']],
    ['IA','Iowa',0,['Des Moines|503','Cedar Rapids|524','Davenport|528','Sioux City|511'],['515','319','563','712']],
    ['KS','Kansas',0,['Wichita|672','Overland Park|662','Kansas City|661','Topeka|666'],['316','785','913']],
    ['KY','Kentucky',0,['Louisville|402','Lexington|405','Bowling Green|421','Covington|410'],['502','859','270']],
    ['LA','Louisiana',0,['New Orleans|701','Baton Rouge|708','Shreveport|711','Metairie|700'],['504','225','318','985']],
    ['ME','Maine',0,['Portland|041','Lewiston|042','Bangor|044','South Portland|041'],['207']],
    ['MD','Maryland',0,['Baltimore|212','Columbia|210','Germantown|208','Silver Spring|209'],['410','301','443']],
    ['MA','Massachusetts',0,['Boston|021','Worcester|016','Springfield|011','Lowell|018'],['617','781','978','508','413']],
    ['MI','Michigan',0,['Detroit|482','Grand Rapids|495','Warren|480','Ann Arbor|481'],['313','586','810','248','734','269']],
    ['MN','Minnesota',0,['Minneapolis|554','Saint Paul|551','Rochester|559','Duluth|558'],['612','651','763','952','507','218']],
    ['MS','Mississippi',0,['Jackson|392','Gulfport|395','Southaven|386','Hattiesburg|394'],['601','662','228']],
    ['MO','Missouri',0,['Kansas City|641','Saint Louis|631','Springfield|658','Columbia|652'],['816','314','573','660','417']],
    ['MT','Montana',1,['Billings|591','Missoula|598','Great Falls|594','Bozeman|597','Helena|596'],['406']],
    ['NE','Nebraska',0,['Omaha|681','Lincoln|685','Bellevue|680','Grand Island|688'],['402','308']],
    ['NV','Nevada',0,['Las Vegas|891','Henderson|890','Reno|895','Carson City|897'],['702','775']],
    ['NH','New Hampshire',1,['Manchester|031','Nashua|030','Concord|033','Derry|030','Dover|038'],['603']],
    ['NJ','New Jersey',0,['Newark|071','Jersey City|073','Paterson|075','Elizabeth|072'],['973','201','908','732','856','609']],
    ['NM','New Mexico',0,['Albuquerque|871','Las Cruces|880','Rio Rancho|871','Santa Fe|875'],['505','575']],
    ['NY','New York',0,['New York|100','Brooklyn|112','Queens|113','Buffalo|142','Rochester|146','Albany|122'],['212','718','917','646','585','716','518']],
    ['NC','North Carolina',0,['Charlotte|282','Raleigh|276','Greensboro|274','Durham|277','Asheville|288'],['704','919','336','828','252','910']],
    ['ND','North Dakota',0,['Fargo|581','Bismarck|585','Grand Forks|582','Minot|587'],['701']],
    ['OH','Ohio',0,['Columbus|432','Cleveland|441','Cincinnati|452','Toledo|436','Akron|443'],['614','216','513','419','330','440']],
    ['OK','Oklahoma',0,['Oklahoma City|731','Tulsa|741','Norman|730','Broken Arrow|740'],['405','918','580']],
    ['OR','Oregon',1,['Portland|972','Eugene|974','Salem|973','Gresham|970','Hillsboro|971'],['503','971','541']],
    ['PA','Pennsylvania',0,['Philadelphia|191','Pittsburgh|152','Allentown|181','Erie|165','Reading|196'],['215','267','412','724','610','814']],
    ['RI','Rhode Island',0,['Providence|029','Cranston|029','Warwick|028','Newport|028'],['401']],
    ['SC','South Carolina',0,['Columbia|292','Charleston|294','North Charleston|294','Mount Pleasant|294'],['803','843']],
    ['SD','South Dakota',0,['Sioux Falls|571','Rapid City|577','Aberdeen|574','Brookings|570'],['605']],
    ['TN','Tennessee',0,['Nashville|372','Memphis|381','Knoxville|379','Chattanooga|374','Clarksville|370'],['615','901','865','423','931']],
    ['TX','Texas',0,['Houston|770','San Antonio|782','Dallas|752','Austin|787','Fort Worth|761','El Paso|799'],['713','832','281','210','972','469','512','817','915']],
    ['UT','Utah',0,['Salt Lake City|841','Provo|846','West Valley City|841','Ogden|844'],['801','385','435']],
    ['VT','Vermont',0,['Burlington|054','Essex|054','Montpelier|056','Rutland|057'],['802']],
    ['VA','Virginia',0,['Virginia Beach|234','Norfolk|235','Chesapeake|233','Richmond|232','Alexandria|223'],['757','804','703','540']],
    ['WA','Washington',0,['Seattle|981','Spokane|992','Tacoma|984','Vancouver|986','Bellevue|980'],['206','509','253','360','425']],
    ['WV','West Virginia',0,['Charleston|253','Huntington|257','Morgantown|265','Parkersburg|261'],['304','681']],
    ['WI','Wisconsin',0,['Milwaukee|532','Madison|537','Green Bay|543','Kenosha|531'],['414','608','920','262']],
    ['WY','Wyoming',0,['Cheyenne|820','Casper|826','Laramie|820','Gillette|827'],['307']]
  ];

  var TAX_FREE = STATES.filter(function (s) { return s[2] === 1; }).map(function (s) { return s[0]; });

  var FIRST_M = ['James','Robert','John','Michael','David','William','Richard','Joseph','Thomas','Charles','Christopher','Daniel','Matthew','Anthony','Mark','Donald','Steven','Paul','Andrew','Joshua','Kenneth','Kevin','Brian','George','Timothy','Ronald','Edward','Jason','Jeffrey','Ryan','Jacob','Gary','Nicholas','Eric','Jonathan','Stephen','Larry','Justin','Scott','Brandon'];
  var FIRST_F = ['Mary','Patricia','Jennifer','Linda','Elizabeth','Barbara','Susan','Jessica','Sarah','Karen','Nancy','Lisa','Margaret','Betty','Sandra','Ashley','Dorothy','Kimberly','Emily','Donna','Michelle','Carol','Amanda','Melissa','Deborah','Stephanie','Rebecca','Laura','Sharon','Cynthia','Amy','Angela','Helen','Anna','Brenda','Pamela','Nicole','Samantha','Katherine','Emma'];
  var LAST = ['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez','Hernandez','Lopez','Gonzalez','Wilson','Anderson','Thomas','Taylor','Moore','Jackson','Martin','Lee','Perez','Thompson','White','Harris','Sanchez','Clark','Ramirez','Lewis','Robinson','Walker','Young','Allen','King','Wright','Scott','Torres','Nguyen','Hill','Flores','Green','Adams','Nelson','Baker','Hall','Rivera','Campbell','Mitchell','Roberts','Carter'];
  var STREETS = ['Maple','Oak','Cedar','Pine','Elm','Washington','Lincoln','Jefferson','Madison','Main','Market','High','Church','Park','Walnut','Spruce','Birch','Willow','Rose','Lake','Hill','Sunset','Highland','Meadow','Riverside','Forest','Valley','Crescent','Ridge','Broadway','Green','Bay','Canal','Harbor','Franklin','Clark','Howard','Beacon','Harvard','Oxford','Cambridge','York','Bristol','Chestnut','Locust','Pearl','Mulberry','Union','Center'];
  var SUFFIX = ['St','Ave','Rd','Blvd','Dr','Ln','Ct','Way','Pl','Ter','Trl','Cir'];
  var OCCUPATIONS = ['Software Engineer','Marketing Manager','Accountant','Teacher','Registered Nurse','Sales Representative',' Consultant','Graphic Designer','Data Analyst','Operations Manager','Customer Support','Project Manager','Electrician','Pharmacist','Financial Advisor'];
  var COMPANIES = ['Northstar Labs','Acme Corp','Bluewave Media','Summit Systems','Pioneer Group','Vertex Solutions','Cedar Works','Orion Digital','Harbor Point LLC','Ironwood Partners'];
  // Public, non-functional test card numbers (Luhn-valid, no real account)
  var TEST_CARDS = [
    ['Visa','4111 1111 1111 1111'],
    ['Mastercard','5500 0000 0000 0004'],
    ['Amex','3782 822463 10005'],
    ['Discover','6011 1111 1111 1117']
  ];
  var EMAIL_DOMAINS = ['example.com','example.net','example.org','testmail.example'];

  function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
  function rndInt(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
  function pad(n, len) { var s = String(n); while (s.length < len) s = '0' + s; return s; }

  function chooseState(mode, code) {
    var pool;
    if (mode === 'taxfree') pool = STATES.filter(function (s) { return s[2] === 1; });
    else if (mode === 'state') pool = STATES.filter(function (s) { return s[0] === code; });
    else pool = STATES;
    if (!pool.length) pool = STATES;
    return pick(pool);
  }

  // opts: { mode: 'any'|'taxfree'|'state', state: 'CA' }
  function generate(opts) {
    opts = opts || {};
    var s = chooseState(opts.mode || 'any', opts.state);
    var cityZip = pick(s[3]).split('|');
    var city = cityZip[0];
    var zipPrefix = cityZip[1];
    var gender = Math.random() < 0.5 ? 'Female' : 'Male';
    var first = pick(gender === 'Female' ? FIRST_F : FIRST_M);
    var last = pick(LAST);
    var year = rndInt(1982, 2003);
    var month = rndInt(1, 12);
    var day = rndInt(1, 28);
    var house = rndInt(102, 9898);
    var street = pick(STREETS) + ' ' + pick(SUFFIX);
    var zip = zipPrefix + pad(rndInt(1, 99), 2);
    var area = pick(s[4]);
    var phone = '(' + area + ') ' + rndInt(200, 989) + '-' + pad(rndInt(0, 9999), 4);
    var email = (first + '.' + last + rndInt(1, 99)).toLowerCase() + '@' + pick(EMAIL_DOMAINS);
    var username = (first.charAt(0) + last + rndInt(10, 99)).toLowerCase();
    var chars = 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$';
    var pw = '';
    for (var i = 0; i < 12; i++) pw += chars.charAt(Math.floor(Math.random() * chars.length));
    var card = pick(TEST_CARDS);
    var ssnFirst = pick(['666', '900', '901', '902', '903', '904', '905', '906', '907', '908', '909']);
    var ssn = ssnFirst + '-' + pad(rndInt(10, 89), 2) + '-' + pad(rndInt(1000, 9999), 4);

    return {
      'Full Name': first + ' ' + last,
      'Gender': gender,
      'Date of Birth': pad(month, 2) + '/' + pad(day, 2) + '/' + year,
      'Street Address': house + ' ' + street,
      'City': city,
      'State': s[1],
      'State Code': s[0],
      'ZIP Code': zip,
      'Phone': phone,
      'Email': email,
      'Username': username,
      'Password': pw,
      'Occupation': pick(OCCUPATIONS).trim(),
      'Company': pick(COMPANIES),
      'SSN (invalid test value)': ssn,
      'Card': card[0] + ' ' + card[1] + ' (test only)',
      '_taxFree': s[2] === 1
    };
  }

  var FIELDS = ['Full Name','Gender','Date of Birth','Street Address','City','State','State Code','ZIP Code','Phone','Email','Username','Password','Occupation','Company','SSN (invalid test value)','Card'];

  // ---------- DOM wiring ----------
  if (typeof document !== 'undefined') {
    var taxFreeList = TAX_FREE.join(', ');
    var stateSelect = document.getElementById('state');
    var freeOnly = document.getElementById('freeOnly');
    var count = document.getElementById('count');
    var output = document.getElementById('output');

    // Build the dropdown from the same dataset the generator uses (single source of truth).
    var originalOptions = '';
    if (stateSelect) {
      var opts = ['<option value="">All states (random)</option>'];
      STATES.forEach(function (s) {
        opts.push('<option value="' + s[0] + '">' + s[1] + (s[2] === 1 ? ' (tax-free)' : '') + '</option>');
      });
      stateSelect.innerHTML = opts.join('');
      originalOptions = stateSelect.innerHTML;
    }

    function refreshCount() {
      var only = freeOnly && freeOnly.checked;
      if (!stateSelect) return;
      if (only) {
        stateSelect.disabled = true;
        stateSelect.value = '';
        stateSelect.innerHTML = '<option value="">Tax-free states only (' + taxFreeList + ')</option>';
        if (count) count.textContent = TAX_FREE.length + ' tax-free states';
      } else {
        stateSelect.disabled = false;
        stateSelect.innerHTML = originalOptions;
        if (count) count.textContent = (STATES.length - 1) + ' states + DC';
      }
    }
    if (freeOnly) freeOnly.addEventListener('change', refreshCount);
    refreshCount();

    function render(records) {
      output.innerHTML = '';
      records.forEach(function (rec, idx) {
        var card = document.createElement('article');
        card.className = 'record';
        var head = document.createElement('h3');
        head.textContent = 'Record ' + (idx + 1) + (rec._taxFree ? ' · Tax-free state' : '');
        card.appendChild(head);
        var dl = document.createElement('dl');
        FIELDS.forEach(function (key) {
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
        card.appendChild(dl);
        output.appendChild(card);
      });
    }

    function flash(btn) {
      var old = btn.textContent;
      btn.textContent = 'Copied';
      setTimeout(function () { btn.textContent = old; }, 1200);
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

    function getOpts() {
      if (freeOnly && freeOnly.checked) return { mode: 'taxfree' };
      if (stateSelect && stateSelect.value) return { mode: 'state', state: stateSelect.value };
      return { mode: 'any' };
    }
    function asText(recs) {
      return recs.map(function (r, i) {
        var lines = ['Record ' + (i + 1)];
        FIELDS.forEach(function (k) { lines.push(k + ': ' + r[k]); });
        return lines.join('\n');
      }).join('\n\n');
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

    var genBtn = document.getElementById('generate');
    if (genBtn) genBtn.addEventListener('click', function () {
      var n = Math.min(Math.max(parseInt(document.getElementById('quantity').value, 10) || 1, 1), 25);
      var recs = [];
      for (var i = 0; i < n; i++) recs.push(generate(getOpts()));
      window._records = recs;
      render(recs);
      var status = document.getElementById('status');
      if (status) status.textContent = n + ' record(s) generated.';
    });

    var copyAll = document.getElementById('copyAll');
    if (copyAll) copyAll.addEventListener('click', function () {
      if (!window._records) return;
      copyText(asText(window._records)); flash(copyAll);
    });
    var expJson = document.getElementById('exportJson');
    if (expJson) expJson.addEventListener('click', function () {
      if (!window._records) return;
      var clean = window._records.map(function (r) {
        var o = {}; FIELDS.forEach(function (k) { o[k] = r[k]; }); return o;
      });
      download('us-test-addresses.json', JSON.stringify(clean, null, 2), 'application/json');
    });
    var expCsv = document.getElementById('exportCsv');
    if (expCsv) expCsv.addEventListener('click', function () {
      if (!window._records) return;
      var q = function (v) { return '"' + String(v).replace(/"/g, '""') + '"'; };
      var lines = [FIELDS.map(q).join(',')];
      window._records.forEach(function (r) { lines.push(FIELDS.map(function (k) { return q(r[k]); }).join(',')); });
      download('us-test-addresses.csv', '\ufeff' + lines.join('\n'), 'text/csv;charset=utf-8');
    });
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { generate: generate, STATES: STATES, TAX_FREE: TAX_FREE, FIELDS: FIELDS };
  }
})();
