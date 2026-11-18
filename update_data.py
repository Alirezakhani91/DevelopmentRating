#!/usr/bin/env python3
"""Read the published sheet CSV and atomically update the dashboard JSON."""
import csv, io, json, urllib.request, datetime, pathlib, sys
URL='https://docs.google.com/spreadsheets/d/e/2PACX-1vQb-14w0moHzpHPQfsrZ8doUrIfJMmw2019w6YSLvGOaJjQYxxHW7xG5U-HMQHEu6J-elWNNoVu14Fp/pub?gid=980860521&single=true&output=csv'
def num(x):
 try: return int(str(x).strip().replace(',','').translate(str.maketrans('۰۱۲۳۴۵۶۷۸۹','0123456789')) or 0)
 except: return 0
def transform(rows):
 data=[]
 for r in rows[1:]:
  r=list(r)+['']*max(0,18-len(r));name=r[0].strip();target=num(r[2]);
  if not name or target<=0:continue
  data.append({'name':name,'exec':r[1].strip() or 'تعیین نشده','target':target,'hq':num(r[3]),'fr':num(r[4]),'contracts':num(r[5]),'newHQ':num(r[7]),'newFr':num(r[8]),'completing':num(r[9]),'negotiating':num(r[11]),'properties':[s.strip() for s in r[12:] if s.strip()]})
 return data
req=urllib.request.Request(URL,headers={'User-Agent':'Mozilla/5.0 (DailyMarket-Dashboard/1.0)'})
with urllib.request.urlopen(req,timeout=35) as response: csv_text=response.read().decode('utf-8-sig')
rows=list(csv.reader(io.StringIO(csv_text)))
if not rows or rows[0][0].strip()!='مدیر منطقه':raise RuntimeError('Unexpected CSV headers')
data=transform(rows)
if not 20<=len(data)<=100:raise RuntimeError('Unexpected number of regions: '+str(len(data)))
if sum(x['contracts'] for x in data)<=0:raise RuntimeError('Invalid contract totals')
output={'success':True,'source':'Google Sheets published CSV','updatedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'data':data}
path=pathlib.Path(__file__).with_name('data.json')
tmp=path.with_suffix('.json.tmp');tmp.write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8');tmp.replace(path)
print('Updated:',len(data),'regions;',sum(x['contracts'] for x in data),'contracts')
