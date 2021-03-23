import codecs,sys
import stop_words
import jieba
from jieba import analyse
#去除停用词
def stopWord(soureFile,targetFile,stopkey):
    sourcef =codecs.open(soureFile,'r',encoding='utf-8')
    targetf =codecs.open(targetFile,'w',encoding='utf-8')

    lines =sourcef.readlines()
    for line in lines:
        list = line.split('\t')
        comment = list[1]

        sentence = delstopword(comment ,stopkey)
        targetf.write(list[0]+','+sentence+','+list[2]+'\n')



    sourcef.close()
    targetf.close()
#删除停用词
def delstopword(comment,stopkey):
    wordList=jieba.cut(comment)
    sentence =''
    for word in wordList:
        word =word.strip()
        if word not in stopkey:
            if word != '\t':
                sentence +=word + " "
    return sentence.strip()

if __name__=='__main__':
    stopkey = [v.strip() for v in codecs.open("./stopWord.txt",'r',encoding='gbk').readlines()]

    soureFile ='sndn.csv'
    targetFile ='sn.csv'
    stopWord(soureFile,targetFile,stopkey)

    # soureFile='posiv'
    # targetFil='po'
    # stopWord(soureFile,targetFile,stopkey)