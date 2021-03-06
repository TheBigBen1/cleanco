terms_by_type = {
   'Corporation': ['company', 'incorporated', 'corporation', 'corp.', 'corp', 'inc',
      '& co.', '& co', 'inc.', 's.p.a.', 'n.v.', 'a.g.', 'ag', 'aktiengesellschaft', 'nuf', 's.a.', 's.f.',
      'oao', 'co.', 'co'
   ],
   'General Partnership': ['soc.col.', 'stg', 'd.n.o.', 'ltda.', 'v.o.s.', 'a spol.',
      u've\xc5\x99. obch. spol.', 'kgaa', 'o.e.', 's.f.', 's.n.c.', 's.a.p.a.', 'j.t.d.',
      'v.o.f.', 'sp.j.', 'og', 'sd', ' i/s', 'ay', 'snc', 'oe', 'bt.', 's.s.', 'mb',
      'ans', 'da', 'o.d.', 'hb', 'pt'
   ],
   'Joint Stock / Unlimited': ['unltd', 'ultd', 'sal', 'unlimited', 'saog', 'saoc', 'aj',
      'yoaj', 'oaj', 'akc. spol.', 'a.s.'
   ],
   'Joint Venture': ['esv', 'gie', 'kv.', 'qk'],
   'Limited': ['pty. ltd.', 'pty ltd', 'ltd', 'l.t.d.', 'bvba', 'd.o.o.', 'ltda', 'gmbh',
      'g.m.b.h', 'kft.', 'kht.', 'zrt.', 'ehf.', 's.a.r.l.', 'd.o.o.e.l.', 's. de r.l.',
      'b.v.', 'tapui', 'sp. z.o.o.', 's.r.l.', 's.l.', 's.l.n.e.', 'ood', 'oy', 'rt.',
      'teo', 'uab', 'scs', 'sprl', 'limited', 'bhd.', 'sdn. bhd.', 'sdn bhd', 'as',
      'lda.', 'tov', 'pp'
   ],
   'Limited Liability Company': ['pllc', 'llc', 'l.l.c.', 'plc.', 'plc', 'hf.', 'oyj',
      'a.e.', 'nyrt.', 'p.l.c.', 'sh.a.', 's.a.', 's.r.l.', 'srl.', 'aat', '3at', 'd.d.',
      's.r.o.', 'spol. s r.o.', 's.m.b.a.', 'smba', 'sarl', 'nv', 'sa', 'aps',
      'a/s', 'p/s', 'sae', 'sasu', 'eurl', 'ae', 'cpt', 'as', 'ab', 'asa', 'ooo', 'dat',
      'vat', 'zat', 'mchj', 'a.d.'
   ],
   'Limited Liability Limited Partnership': ['lllp', 'l.l.l.p.'],
   'Limited Liability Partnership': ['llp', 'l.l.p.', 'sp.p.', 's.c.a.', 's.c.s.'],
   'Limited Partnership': ['gmbh & co. kg', 'gmbh & co. kg', 'lp', 'l.p.', 's.c.s.',
      's.c.p.a', 'comm.v', 'k.d.', 'k.d.a.', 's. en c.', 'e.e.', 's.a.s.', 's. en c.',
      'c.v.', 's.k.a.', 'sp.k.', 's.cra.', 'ky', 'scs', 'kg', 'kd', 'k/s', 'ee', 'secs',
      'kda', 'ks', 'kb','kt'
   ],
   'Mutual Fund': ['sicav'],
   'No Liability': ['nl'],
   'Non-Profit': ['vzw', 'ses.', 'gte.'],
   'Private Company': ['private', 'pte', 'xk'],
   'Professional Corporation': ['p.c.', 'vof', 'snc'],
   'Professional Limited Liability Company': ['pllc', 'p.l.l.c.'],
   'Sole Proprietorship': ['e.u.', 's.p.', 't:mi', 'tmi', 'e.v.', 'e.c.', 'et', 'obrt',
      'fie', 'ij', 'fop', 'xt'
   ],
   'others': ['se','s.e.','s.e']
}

terms_by_country = {
   'Albania': ['sh.a.', 'sh.p.k.'],
   'Argentina': ['s.a.', 's.r.l.', 's.c.p.a', 'scpa', 's.c.e i.', 's.e.', 's.g.r',
      'soc.col.'
   ],
   'Australia': ['nl', 'pty. ltd.', 'pty ltd'],
   'Austria': ['e.u.', 'stg', 'gesbr', 'a.g.', 'ag', 'og', 'kg', 'aktiengesellschaft'],
   'Belarus': ['aat', '3at'],
   'Belgium': ['esv', 'vzw', 'vof', 'snc', 'comm.v', 'scs', 'bvba', 'sprl', 'cbva',
      'cvoa', 'sca', 'sep', 'gie'
   ],
   'Bosnia / Herzegovina': ['d.d.', 'a.d.', 'd.n.o.', 'd.o.o.', 'k.v.', 's.p.'],
   'Brazil': ['ltda', 's.a.', 'pllc', 'ad', 'adsitz', 'ead', 'et', 'kd', 'kda', 'sd'],
   'Bulgaria': ['ad', 'adsitz', 'ead', 'et', 'kd', 'kda', 'sd'],
   'Cambodia': ['gp', 'sm pte ltd.', 'pte ltd.', 'plc ltd.', 'peec', 'sp'],
   'Canada': ['gp', 'lp', 'sp'],
   'Chile': ['eirl', 's.a.', 'sgr', 's.g.r.', 'ltda', 's.p.a.', 'sa', 's. en c.',
      'ltda.'
   ],
   'Columbia': ['s.a.', 'e.u.', 's.a.s.', 'suc. de descendants', 'sca'],
   'Croatia': ['d.d.', 'd.o.o.', 'obrt'],
   'Czech Republic': ['a.s.', 'akc. spol.', 's.r.o.', 'spol. s r.o.', 'v.o.s.', u've\xc5\x99. obch. spol.', 'a spol.', 'k.s.', 'kom. spol.', 'kom. spol.'],
   'Denmark': ['i/s', 'a/s', 'k/s', 'p/s', 'amba', 'a.m.b.a.', 'fmba', 'f.m.b.a.', 'smba',
      's.m.b.a.', 'g/s'
   ],
   'Dominican Republic': ['c. por a.', 'cxa', 's.a.', 's.a.s.', 'srl.', 'eirl.', 'sa',
      'sas'
   ],
   'Ecuador': ['s.a.', 'c.a.', 'sa', 'ep'],
   'Egypt': ['sae'],
   'Estonia': ['fie'],
   'Finland': ['t:mi', 'tmi', 'as oy', 'as.oy', 'ay', 'ky', 'oy', 'oyj', 'ok'],
   'France': ['sicav', 'sarl', 'sogepa', 'ei', 'eurl', 'sasu', 'fcp', 'gie', 'sep', 'snc',
      'scs', 'sca', 'scop', 'sem', 'sas'
   ],
   'Germany': ['gmbh & co. kg', 'gmbh & co. kg', 'e.g.', 'e.v.', 'gbr', 'ohg', 'partg',
      'kgaa', 'gmbh', 'g.m.b.h.', 'ag', 'aktiengesellschaft'
   ],
   'Greece': ['a.e.', 'ae', 'e.e.', 'ee', 'epe', 'e.p.e.', 'mepe', 'm.e.p.e.', 'o.e.',
      'oe', 'ovee', 'o.v.e.e.'
   ],
   'Guatemala': ['s.a.', 'sa'],
   'Haiti': ['sa'],
   'Hong Kong': ['ltd', 'unltd', 'ultd', 'limited'],
   'Hungary': ['e.v.', 'e.c.', 'bt.', 'kft.', 'kht.', 'kkt.', 'k.v.', 'zrt.', 'nyrt',
      'ev', 'ec', 'rt.'
   ],
   'Iceland': ['ehf.', 'hf.', 'ohf.', 's.f.', 'ses.'],
   'India': ['pvt. ltd.', 'ltd.', 'psu', 'pse'],
   'Indonesia': ['ud', 'fa', 'pt'],
   'Ireland': ['cpt', 'teo'],
   'Israel': ['b.m.', 'bm', 'ltd', 'limited'],
   'Italy': ['s.n.c.', 's.a.s.', 's.p.a.', 's.a.p.a.', 's.r.l.', 's.c.r.l.', 's.s.'],
   'Latvia': ['as', 'sia', 'ik', 'ps', 'ks'],
   'Lebanon': ['sal'],
   'Lithuania': ['uab', 'ab', 'ij', 'mb'],
   'Luxemborg': ['s.a.', 's.a.r.l.', 'secs'],
   'Macedonia': ['d.o.o.', 'd.o.o.e.l', 'k.d.a.', 'j.t.d.', 'a.d.', 'k.d.'],
   'Malaysia': ['bhd.', 'sdn. bhd.'],
   'Mexico': ['s.a.', 's. de. r.l.', 's. en c.', 's.a.b.', 's.a.p.i.'],
   'Mongolia': ['xk', 'xxk'],
   'Netherlands': ['v.o.f.', 'c.v.', 'b.v.', 'n.v.'],
   'New Zealand': ['tapui', 'ltd', 'limited'],
   'Nigeria': ['gte.', 'plc', 'ltd.', 'ultd.'],
   'Norway': ['asa', 'as', 'ans', 'ba', 'bl', 'da', 'etat', 'fkf', 'hf', 'iks', 'kf',
      'ks', 'nuf', 'rhf', 'sf'
   ],
   'Oman': ['saog', 'saoc'],
   'Pakistan': ['ltd.', 'pvt. ltd.', 'ltd', 'limited'],
   'Peru': ['sa', 's.a.', 's.a.a.'],
   'Philippines': ['coop.', 'corp.', 'corp', 'ent.', 'inc.', 'inc', 'llc', 'l.l.c.',
      'ltd.'
   ],
   'Poland': ['p.p.', 's.k.a.', 'sp.j.', 'sp.k.', 'sp.p.', 'sp. z.o.o.', 's.c.', 's.a.'],
   'Portugal': ['lda.', 'crl', 's.a.', 's.f.', 'sgps'],
   'Romania': ['s.c.a.', 's.c.s.', 's.n.c.', 's.r.l.', 'o.n.g.', 's.a.'],
   'Russia': ['ooo', 'oao', 'zao', '3ao'],
   'Serbia': ['d.o.o.', 'a.d.', 'k.d.', 'o.d.'],
   'Singapore': ['bhd', 'pte ltd', 'sdn bhd', 'llp', 'l.l.p.', 'ltd.', 'pte'],
   'Slovenia': ['d.d.', 'd.o.o.', 'd.n.o.', 'k.d.', 's.p.'],
   'Slovakia': ['a.s.', 'akc. spol.', 's.r.o.', 'spol. s r.o.', 'k.s.', 'kom. spol.', 'v.o.s.', 'a spol.'],
   'Spain': ['s.a.', 's.a.d.', 's.l.', 's.l.l.', 's.l.n.e.', 's.c.', 's.cra', 's.coop',
      'sal', 'sccl'
   ],
   'Sweden': ['ab', 'hb', 'kb'],
   'Switzerland': ['ab', 'sa', 'gmbh', 'g.m.b.h.', 'sarl', 'sagl'],
   'Turkey': ['koop.'],
   'Ukraine': ['dat', 'fop', 'kt', 'pt', 'tdv', 'tov', 'pp', 'vat', 'zat', 'at'],
   'United Kingdom': ['plc.', 'plc', 'cic', 'cio', 'l.l.p.', 'llp', 'l.p.', 'lp', 'ltd.',
      'ltd', 'limited'
   ],
   'United States of America': ['llc', 'inc.', 'corporation', 'incorporated', 'company',
      'limited', 'corp.', 'inc.', 'inc', 'llp', 'l.l.p.', 'pllc', 'and company',
      '& company', 'inc', 'inc.', 'corp.', 'corp', 'ltd.', 'ltd', '& co.', '& co', 'co.',
      'co', 'lp'
   ],
   'Uzbekistan': ['mchj', 'qmj', 'aj', 'oaj', 'yoaj', 'xk', 'xt', 'ok', 'uk', 'qk'],
   'European': ['se','s.e.','s.e']
}

legal_suffixes = ['suc. de descendants', 'aktiengesellschaft', 'veÅ\x99. obch. spol.',
                  'gmbh & co. kg', 'incorporated', 'spol. s r.o.', 'and company', 'corporation',
                  's. de. r.l.', 'sm pte ltd.', 'akc. spol.', 'd.o.o.e.l.', 'kom. spol.',
                  's. de r.l.', 'sp. z.o.o.', '& company', 'c. por a.', 'd.o.o.e.l', 'pty. ltd.',
                  'pvt. ltd.', 'sdn. bhd.', 'unlimited', 'a.m.b.a.', 'f.m.b.a.', 'g.m.b.h.',
                  'l.l.l.p.', 'm.e.p.e.', 'o.v.e.e.', 'p.l.l.c.', 'plc ltd.', 'pte ltd.', 's. en c.',
                  's.a.p.a.', 's.a.p.i.', 's.a.r.l.', 's.c.e i.', 's.c.r.l.', 's.l.n.e.',
                  's.m.b.a.', 'soc.col.', 'and co.', 'a spol.', 'company', 'g.m.b.h', 'limited',
                  'private', 'pte ltd', 'pty ltd', 's.c.p.a', 'sdn bhd', 'sh.p.k.', 'adsitz',
                  'comm.v', 'd.n.o.', 'd.o.o.', 'e.p.e.', 'j.t.d.', 'k.d.a.', 'l.l.c.', 'l.l.p.',
                  'l.t.d.', 'o.n.g.', 'p.l.c.', 's.a.a.', 's.a.b.', 's.a.d.', 's.a.s.', 's.c.a.',
                  's.c.s.', 's.coop', 's.cra.', 's.g.r.', 's.k.a.', 's.l.l.', 's.n.c.', 's.p.a.',
                  's.r.l.', 's.r.o.', 'sogepa', 'v.o.f.', 'v.o.s.', '& co.', 'as oy', 'as.oy',
                  'coop.', 'corp.', 'eirl.', 'gesbr', 'koop.', 'ltda.', 'nyrt.', 'partg', 's.cra',
                  's.g.r', 'sh.a.', 'sicav', 'sp.j.', 'sp.k.', 'sp.p.', 'tapui', 'ultd.', 'unltd',
                  ' i/s', '& co', 'a.d.', 'a.e.', 'a.g.', 'a.s.', 'amba', 'b.m.', 'b.v.', 'bhd.',
                  'bvba', 'c.a.', 'c.v.', 'cbva', 'corp', 'cvoa', 'd.d.', 'e.c.', 'e.e.', 'e.g.',
                  'e.u.', 'e.v.', 'ehf.', 'eirl', 'ent.', 'etat', 'eurl', 'fmba', 'gmbh', 'gte.',
                  'inc.', 'k.d.', 'k.s.', 'k.v.', 'kft.', 'kgaa', 'kht.', 'kkt.', 'l.p.', 'lda.',
                  'lllp', 'ltd.', 'ltda', 'mchj', 'mepe', 'n.v.', 'nyrt', 'o.d.', 'o.e.', 'obrt',
                  'ohf.', 'ovee', 'p.c.', 'p.p.', 'peec', 'plc.', 'pllc', 's.a.', 's.c.', 's.e.',
                  's.f.', 's.l.', 's.p.', 's.s.', 'sagl', 'saoc', 'saog', 'sarl', 'sasu', 'sccl',
                  'scop', 'scpa', 'secs', 'ses.', 'sgps', 'smba', 'sprl', 'srl.', 't:mi', 'ultd',
                  'yoaj', 'zrt.', '3ao', '3at', 'a/s', 'aat', 'ans', 'aps', 'asa', 'bhd', 'bt.',
                  'cic', 'cio', 'co.', 'cpt', 'crl', 'cxa', 'dat', 'ead', 'epe', 'esv', 'fcp',
                  'fie', 'fkf', 'fop', 'g/s', 'gbr', 'gie', 'hf.', 'i/s', 'iks', 'inc', 'k/s',
                  'kda', 'kv.', 'llc', 'llp', 'ltd', 'nuf', 'oaj', 'oao', 'ohg', 'ood', 'ooo',
                  'oyj', 'p/s', 'plc', 'pse', 'psu', 'pte', 'qmj', 'rhf', 'rt.', 's.e', 'sae',
                  'sal', 'sas', 'sca', 'scs', 'sem', 'sep', 'sgr', 'sia', 'snc', 'stg', 'tdv',
                  'teo', 'tmi', 'tov', 'uab', 'vat', 'vof', 'vzw', 'xxk', 'zao', 'zat', 'ab',
                  'ad', 'ae', 'ag', 'aj', 'as', 'at', 'ay', 'ba', 'bl', 'bm', 'co', 'da', 'ec',
                  'ee', 'ei', 'ep', 'et', 'ev', 'fa', 'gp', 'hb', 'hf', 'ij', 'ik', 'kb', 'kd',
                  'kf', 'kg', 'ks', 'kt', 'ky', 'lp', 'mb', 'nl', 'nv', 'oe', 'og', 'ok', 'oy', 'pp',
                  'ps', 'pt', 'qk', 'sa', 'sd', 'se', 'sf', 'sp', 'ud', 'xk', 'xt']
