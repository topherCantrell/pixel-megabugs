
def _conversion(s,color_ofs=1):
    ret = [] # List of images               
    rws = s.strip().split('\n')
    for i in range(len(rws)):
        cols = rws[i].strip().split(' ')
        for j in range(len(cols)-1,-1,-1):
            if not cols[j]:
                del cols[j]
        if i==0:
            for j in range(len(cols)):
                ret.append([])
        for j in range(len(cols)):
            col = cols[j]
            row = []
            for c in col:
                if c=='.':
                    c=0
                else:
                    c = int(c,16)-1+color_ofs
                row.append(c)
            ret[j].append(row)
    return ret

def _from_string_rec(data,color_ofs=1):    
    if isinstance(data,list):                
        ret = []
        for i in data:
            res,_typ,multi = _from_string_rec(i,color_ofs)      
            if multi:      
                for r in res:
                    ret.append(r)       
            else:
                ret.append(res)     
        return ret,'list',False
    elif isinstance(data,dict):
        ret = {}
        for i in data:
            res,typ,multi = _from_string_rec(data[i],color_ofs)
            if '`' in i:
                ks = i.split('`')
                for j in range(len(ks)):
                    ret[ks[j]] = res[j]                
            else:
                ret[i] = res
                
        return ret,'dict',False
    elif isinstance(data,str):
        res = _conversion(data,color_ofs)
        if len(res)>1:
            return res,'string',True
        else:
            return res[0],'string',False        
    else:
        raise Exception('Must be list or dictionary')
    
def from_string(data,col_ofs=1):
    r = data
    res,_type,_multi = _from_string_rec(r,col_ofs)    
    return res

