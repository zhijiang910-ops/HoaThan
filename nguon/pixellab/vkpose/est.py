import json,base64,sys,importlib.util
spec=importlib.util.spec_from_file_location('pl','/home/user/HoaThan/cong_cu/claude/pl.py');pl=importlib.util.module_from_spec(spec);spec.loader.exec_module(pl)
out={}
for f in sys.argv[1:]:
    b=base64.b64encode(open('in/'+f+'.png','rb').read()).decode()
    j=pl.req('POST','/estimate-skeleton',{'image':{'type':'base64','base64':b}})
    out[f]=j;print(f,str(j)[:300])
json.dump(out,open('skel.json','w'))
