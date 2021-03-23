import pandas as pd
from snownlp import SnowNLP
pd.set_option('display.max_columns',5)

def convert(comment):
    snow=SnowNLP(str(comment))
    sentiments = snow.sentiments
    return sentiments
if __name__=='__main__':
    data=pd.read_csv('./sn.csv',',')
    data['snownlp']=data.comment.apply(convert)
    data.sort_values(by='snownlp',ascending=False,inplace=True)
    #保持数据
    data_pos = data[data['snownlp']>0.8]
    data_neg = data[data['snownlp']<=0.3]

    data_pos.to_csv('./sndn_pos.csv',sep='\t',index=False,encoding='utf-8')
    data_neg.to_csv('./sndn_neg.csv',sep='\t',index=False,encoding='utf-8')
    data.to_csv('./sndn_snownlp.csv', sep='\t', index=False, encoding='utf-8')

    #print(data[:10])
    # print(data[-10:])