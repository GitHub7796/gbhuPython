import pandas.io.clipboard as cb
import pandas as pd
import io
pasteContent=cb.paste()
df=pd.read_csv(io.StringIO(pasteContent),sep='\t',header=None)
res=[]
for pre in range(df.shape[0]):
    raw=df.iloc[pre]
    attrCol=str(raw.iloc[0])
    attrComment=str(raw.iloc[1])
    attrType=str(raw.iloc[2])
    attr=f'''
/**
* {attrComment}
*/
private {attrType} {attrCol} ;
'''
    res.append(attr)
res='\n'.join(res)
cb.copy(res)