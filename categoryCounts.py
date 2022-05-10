#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:36:23 2021
@author: lexipfalzgraf
"""

import pandas as pd
import nltk 
import jsonlines
from nltk.util import bigrams, trigrams
import collections

#create dataframe from dataset
df= pd.DataFrame(columns=["creator","datePublished","docType","fullText","id","identifier","isPartOf","issueNumber","language","outputFormat","pageCount","pageEnd","pageStart","pagination","provider","publicationYear","publisher","sourceCategory","tdmCategory","title","url","volumeNumber","wordCount"])
i=0  
with jsonlines.open('spirit.jsonl') as f:
    for line in f.iter():
        df.loc[i]=(line)
        i+=1

#dropping all entries that occur after 2015, not substantial      
df.drop(df[df['publicationYear']>2015].index, inplace=True)
remove_title=['Back Matter','Front Matter','Volume Information','Personal and Bibliographical','Personal and Miscellaneous''In Memoriam','Other Publications Received','Other Books Received','Selected Bibliography','Minor Notices','[Miscellaneous]','Books and Periodicals','Economic and Financial Questions','Other Activities','Notes from the Editor','Administrative and Budgetary Questions','Minor Notices','Economic and Financial Questions','Editorial Note','Briefer Notices']
df = df[~df['title'].isin(remove_title)]
df=df.reset_index()
df=df.drop('index',1)

#changing fullText to type string for easier manipulation
df = df.astype({"fullText": str}, errors='raise')

#function to clean the text (lowercase, remove puncuation, remove stopwords)
stopword=nltk.corpus.stopwords.words('english')

def clean(txt):
    txt=txt.lower().split()
    txt_np=[l for l in txt if l.isalpha()]
    textClean=[w for w in txt_np if w not in stopword]
    return textClean
        
#function to add to dictionaries based on phrase
def dictAdd(author, nList, aList):
    for i in range(len(nList)):
        for j in aList:
            if pubYear[i] not in author:
                author[pubYear[i]]=nList[i][j[0],j[1]]
            else:
                author[pubYear[i]]+=nList[i][j[0],j[1]]

def dictAddUni(author, nList, aList):
    for i in range(len(nList)):
        for j in aList:
            if pubYear[i] not in author:
                author[pubYear[i]]=nList[i][j[0]]
            else:
                author[pubYear[i]]+=nList[i][j[0]]

def dictAddTri(author, nList, aList):
    for i in range(len(nList)):
        for j in aList:
            if pubYear[i] not in author:
                author[pubYear[i]]=nList[i][j[0],j[1],j[2]]
            else:
                author[pubYear[i]]+=nList[i][j[0],j[1],j[2]]
                
            
#list to hold fullText from df, to hold pub year from df, cleaned text, bi, tri 
rawText=df['fullText']
pubYear=df['publicationYear']
cleanText=[]
uniList=[]
biList=[]
triList=[]

#loop to clean all full text and store in list
for i in range(len(rawText)):
    cleanText.append(clean(rawText[i]))
    
#generate bigrams, trigrams
for i in range(len(cleanText)):
    uniList.append(collections.Counter(cleanText[i]))
    
for i in range(len(rawText)):
    biList.append(collections.Counter(list(bigrams(cleanText[i]))))

for i in range(len(rawText)):
    triList.append(collections.Counter(list(trigrams(cleanText[i]))))


#create author dictionaries
Spirit={}
Weber={}
Mont={}
Hegel={}
Diamond={}
Beard={}
Macy={}
Rugg={}
Pye={}
Misc={}
Wilson={}
Ari={}
Religion={}
Aquinas={}
Voe={}
#
Vatican={}
#Christianity={}
#Islam={}
#Christian={}
#Ecu={}
#Holy={}
#Relig={}
#Spirituality={}
#Spiritual={}

#create author phrase lists
WeberList=[['spirit','weber'],['weber','spirit'],['work','spirit'],['spirit','work'],['spirit','capitalism'],['capitalism','spirit'],['ethic','spirit'],['spirit','ethic'],['ethics','spirit'],['spirit','ethics'],['protestant','spirit'],['spirit','protestant'],['entrepreneurial','spirit'],['spirit','entrepreneurial'],['entrepreneur','spirit'],['spirit','entrepreneur'],['enterprise','spirit'],['spirit','enterprise'],['spirit','capitalism'],['isolation','spiritual'],['spiritual','isolation'],['spiritual','energies'],['energies','spiritual'],['talcott','spirit'],['spirit','talcott'],['parsons','spirit'],['spirit','parsons']]
MontList=[['spirit','constitutional'],['constitutional','spirit'],['spirit','article'],['article','spirit'],['spirit','montesquieu'],['montesquieu','spirit'],['spirit','allen'],['allen','spirit'],['constitutional','spirit'],['spirit','constitutional'],['charter','spirit'],['spirit','charter'],['book','spirit'],['spirit','book'],['written','spirit'],['spirit','written'],['spirit','political'],['political','spirit'],['spirit','law'],['law','spirit'],['spirit','laws'],['laws','spirit'],['spirit','constitution'],['constitution','spirit'],['spirit','letter'],['letter','spirit'],['spirit','letters'],['letters','spirit'],['republican','spirit'],['spirit','republican'],['spirit','government'],['government','spirit'],['spirit','constitutionalism'],['constitutionalism','spirit'],['spirit','republicanism'],['republicanism','spirit'],['spirit','community'],['community','spirit'],['anne','spirit'],['spirit','anne'],['spirit','purpose'],['purpose','spirit'],['spirit','violation'],['violation','spirit']]
HegelList=[['hegel','spirit'],['spirit','hegel'],['spirit','nationality'],['nationality','spirit'],['nationalist','spirit'],['spirit','nationalist'],['nationalism','spirit'],['spirit','nationalism'],['guiding','spirit'],['spirit','guiding'],['spirit','guide'],['guide','spirit'],['phenomenology','spirit'],['spirit','phenomenology'],['world','spirit'],['spirit',' world'],['national','spirit'],['spirit','national'],['spirit','times'],['times','spirit'],['spirit','age'],['age','spirit'],['popular','spirit'],['spirit','popular'],['people','spirit'],['spirit','people'],['guild','spirit'],['spirit','guild'],['chirstianity','spirit'],['spirit','christianity'],['christian','spirit'],['spirit','christian'],['human','spirit'],['spirit','human'],['century','spirit'],['spirit', 'century'],['common','spirit'],['spirit','common'],['nationalist','spirit'],['spirit','nationalist']]
DiamondList=[['diamond','spirit'],['spirit','diamond'],['spirit','democratic'],['spirit','democracy'],['democracy','spirit'],['democratic','spirit']]
BeardList=[['beard','spirit'],['spirit','beard'],['spirit','civic'],['civic','spirit'],['spirit','man'],['man','spirit'],['spirit','american'],['american','spirit'],['spirit','mankind'],['mankind','spirit'],['creative','spirit'],['spirit','creative'],['alien','spirit'],['spirit','alien'],['america','spirit'],['spirit','america'],['founding','spirit'],['spirit','founding']]
MacyList=[['macy','spirit'],['spirit','macy'],['science','spirit'],['spirit','science'],['spirit','new'],['new','spirit'],['true','spirit'],['spirit','true'],['scientific','spirit'],['spirit','scientific'],['method','spirit'],['spirit','method'],['spirit','truth'],['truth','spirit'],['spirit','progressive'],['progressive','spirit'],['modern','spirit'],['spirit','modern'],['social','spirit'],['spirit','social'],['rationalism','spirit'],['spirit','rationalism']]
RuggList=[['ruggiero','spirit'],['spirit','ruggiero'],['de','spirit'],['spirit','de'],['free','spirit'],['spirit','free'],['liberty','spirit'],['spirit','liberty'],['freedom','spirit'],['spirit','freedom'],['liberal','spirit'],['spirit','liberal']]
PyeList=[['pye','spirit'],['spirit','pye'],['spirit','chinese'],['chinese','spirit'],['spirit','china'],['china','spirit'],['lucian','spirit'],['spirit','lucian'],['psychocultural','spirit'],['spirit','psychocultural']]
MiscList=[['form','spirit'],['spirit','form'],['spirit','private'],['private','spirit'],['team','spirit'],['spirit','team'],['well','spirit'],['spirit','well'],['party','spirit'],['spirit','party'],['university','spirit'],['spirit','university'],['spirit','rather'],['rather','spirit'],['review','spirit'],['spirit','review'],['spirit','life'],['life','spirit'],['spirit','politic'],['politic','spirit'],['spirit','politics'],['politics','spirit'],['spirit','cooperative'],['cooperative','spirit'],['spirit','within'],['within','spirit'],['spirit','also'],['also','spirit'],['spirit','imbued'],['imbued','spirit'],['spirit','violate'],['violate','spirit'],['spirit','book'],['book','spirit'],['spirit','fighting'],['fighting','spirit'],['spirit','different'],['different','spirit'],['violated','spirit'],['spirit','violated'],['spirit','mind'],['mind','spirit'],['might','spirit'],['spirit','might'],['must','spirit'],['spirit','must'],['among','spirit'],['spirit','among'],['spirit','keeping'],['keeping','spirit'],['spirit','would'],['would','spirit'],['spirit','consistent'],['consistent','spirit'],['spirit','mutual'],['mutual','spirit'],['spirit','one'],['one','spirit'],['spirit','thomas'],['thomas','spirit'],['spirit','even'],['even','spirit'],['might','spirit'],['spirit','might'],['among','spirit'],['spirit','among'],['article','spirit'],['spirit','article'],['spirit','keeping'],['keeping','spirit'],['well','spirit'],['spirit','well'],['may','spirit'],['spirit','may'],['spirit','party'],['party','spirit'],['general','spirit'],['spirit','general'],['one','spirit'],['spirit','one'],['similar','spirit'],['spirit','similar'],['much','spirit'],['spirit','much'],['military','spirit'],['spirit','military'],['contrary','spirit'],['spirit','contrary'],['spirited','discussion'],['discussion','spirited'],['spirited','debate'],['debate','spirited'],['kindred','spirit'],['spirit','kindred'],['kindrid','spirit'],['spirit','kindrid'],['spiritual','crisis'],['crisis','spiritual'],['revolutionary','spirit'],['spirit','revolutionary'],['spirit','rebellion'],['rebellion','spirit'],['conquest','spirit'],['spirit','conquest'],['machiavelli','spirit'],['spirit','machiavelli']]
WilsonList=[['wilson','spirit'],['spirit','wilson'],['union','spirit'],['spirit','union'],['hope','spirit'],['spirit','hope'],['renewed','spirit'],['spirit','renewed'],['sinew','spirit'],['spirit','sinew'],['public','spirit'],['spirit','public'],['spirit','crusading'],['crusading','spirit'],['international','spirit'],['spirit','international'],['spirit','independence'],['independence','spirit'],['spirit','united'],['united','spirit'],['moral','spirit'],['spirit','moral'],['spirit','cooperation'],['cooperation','spirit'],['compromise','spirit'],['spirit','compromise']]
AriList=[['aristotle','spirit'],['spirit','aristotle'],['citizen','spirited'],['spirited','citizen'],['men','spirited'],['spirited','men'],['spiritedness','thumos'],['thumos','spiritedness'],['manly','spirit'],['male','spirit'],['spirit','manly'],['spirit','male']]
MacyThree=[['truth','telling','spirit'],['spirit','truth','telling']]
WilsonThree=[['united','nations','spirit'],['spirit','united','nations']]
MiscOne=[['spiritless']]
AriOne=[['spirtedness']]
ReligionList=[['spirit','vatican'],['vatican','spirit'],['spirit','christianity'],['christianity','spirit'],['islam','spirit'],['spirit','islam'],['spirit','christian'],['christian','spirit'],['ecumenical','spirit'],['spirit','ecumenical'],['holy','spirit'],['spirit','holy'],['religion','spirit'],['spirit','religion']]
ReligionUni=[['spirituality'],['spiritual']]
AquinasList=[['thomas','spirit'],['spirit','thomas'],['gifts','spirit'],['spirit','gifts'],['gift','spirit'],['spirit','gift']]
VoeList=[['spiritual','realism'],['realism','spiritual'],['voegelin','spirituality'],['spirituality','voegelin'],['voegelin','spirit'],['spirit','voegelin'],['voegelin','spiritual'],['spiritual','voegelin']]
VaticanList=[['spirit','vatican'],['vatican','spirit']]
#ChristianityList=[['spirit','christianity'],['christianity','spirit']]
#IslamList=[['islam','spirit'],['spirit','islam']]
#ChristianList=[['spirit','christian'],['christian','spirit']]
#EcuList=[['ecumenical','spirit'],['spirit','ecumenical']]
#HolyList=[['holy','spirit'],['spirit','holy']]
#ReligList=[['religion','spirit'],['spirit','religion']]
#SpiritualityList=[['spirituality']]
#SpiritualList=[['spiritual']]



#consolidated list of bigrams
allCountedBi=[['spiritual','realism'],['realism','spiritual'],['voegelin','spirituality'],['spirituality','voegelin'],['voegelin','spirit'],['spirit','voegelin'],['voegelin','spiritual'],['spiritual','voegelin'],['thomas','spirit'],['spirit','thomas'],['gifts','spirit'],['spirit','gifts'],['gift','spirit'],['spirit','gift'],['spirit','vatican'],['vatican','spirit'],['spirit','christianity'],['christianity','spirit'],['islam','spirit'],['spirit','islam'],['spirit','christian'],['christian','spirit'],['ecumenical','spirit'],['spirit','ecumenical'],['holy','spirit'],['spirit','holy'],['religion','spirit'],['spirit','religion'],['aristotle','spirit'],['spirit','aristotle'],['citizen','spirited'],['spirited','citizen'],['men','spirited'],['spirited','men'],['spiritedness','thumos'],['thumos','spiritedness'],['manly','spirit'],['male','spirit'],['spirit','manly'],['spirit','male'],['wilson','spirit'],['spirit','wilson'],['union','spirit'],['spirit','union'],['hope','spirit'],['spirit','hope'],['renewed','spirit'],['spirit','renewed'],['sinew','spirit'],['spirit','sinew'],['public','spirit'],['spirit','public'],['spirit','crusading'],['crusading','spirit'],['form','spirit'],['spirit','form'],['spirit','private'],['private','spirit'],['spirit','purpose'],['purpose','spirit'],['international','spirit'],['spirit','international'],['spirit','independence'],['independence','spirit'],['team','spirit'],['spirit','team'],['well','spirit'],['spirit','well'],['party','spirit'],['spirit','party'],['university','spirit'],['spirit','university'],['spirit','violation'],['violation','spirit'],['spirit','community'],['community','spirit'],['spirit','rather'],['rather','spirit'],['review','spirit'],['spirit','review'],['spirit','life'],['life','spirit'],['spirit','politic'],['politic','spirit'],['spirit','politics'],['politics','spirit'],['spirit','cooperative'],['cooperative','spirit'],['spirit','within'],['within','spirit'],['spirit','also'],['also','spirit'],['spirit','imbued'],['imbued','spirit'],['spirit','violate'],['violate','spirit'],['spirit','book'],['book','spirit'],['spirit','fighting'],['fighting','spirit'],['anne','spirit'],['spirit','anne'],['spirit','different'],['different','spirit'],['violated','spirit'],['spirit','violated'],['spirit','mind'],['mind','spirit'],['might','spirit'],['spirit','might'],['must','spirit'],['spirit','must'],['among','spirit'],['spirit','among'],['spirit','keeping'],['keeping','spirit'],['spirit','would'],['would','spirit'],['spirit','consistent'],['consistent','spirit'],['spirit','mutual'],['mutual','spirit'],['spirit','one'],['one','spirit'],['spirit','thomas'],['thomas','spirit'],['spirit','even'],['even','spirit'],['might','spirit'],['spirit','might'],['spirit','united'],['united','spirit'],['among','spirit'],['spirit','among'],['article','spirit'],['spirit','article'],['spirit','keeping'],['keeping','spirit'],['well','spirit'],['spirit','well'],['may','spirit'],['spirit','may'],['social','spirit'],['spirit','social'],['spirit','party'],['party','spirit'],['general','spirit'],['spirit','general'],['one','spirit'],['spirit','one'],['similar','spirit'],['spirit','similar'],['much','spirit'],['spirit','much'],['military','spirit'],['spirit','military'],['contrary','spirit'],['spirit','contrary'],['moral','spirit'],['spirit','moral'],['spirited','discussion'],['discussion','spirited'],['spirited','debate'],['debate','spirited'],['kindred','spirit'],['spirit','kindred'],['kindrid','spirit'],['spirit','kindrid'],['spiritual','crisis'],['crisis','spiritual'],['revolutionary','spirit'],['spirit','revolutionary'],['spirit','rebellion'],['rebellion','spirit'],['rationalism','spirit'],['spirit','rationalism'],['spirit','cooperation'],['cooperation','spirit'],['conquest','spirit'],['spirit','conquest'],['machiavelli','spirit'],['spirit','machiavelli'],['compromise','spirit'],['spirit','compromise'],['pye','spirit'],['spirit','pye'],['spirit','chinese'],['chinese','spirit'],['spirit','china'],['china','spirit'],['lucian','spirit'],['spirit','lucian'],['psychocultural','spirit'],['spirit','psychocultural'],['ruggiero','spirit'],['spirit','ruggiero'],['de','spirit'],['spirit','de'],['free','spirit'],['spirit','free'],['liberty','spirit'],['spirit','liberty'],['freedom','spirit'],['spirit','freedom'],['liberal','spirit'],['spirit','liberal'],['macy','spirit'],['spirit','macy'],['science','spirit'],['spirit','science'],['spirit','new'],['new','spirit'],['true','spirit'],['spirit','true'],['scientific','spirit'],['spirit','scientific'],['method','spirit'],['spirit','method'],['spirit','truth'],['truth','spirit'],['spirit','progressive'],['progressive','spirit'],['modern','spirit'],['spirit','modern'],['beard','spirit'],['spirit','beard'],['spirit','civic'],['civic','spirit'],['spirit','man'],['man','spirit'],['spirit','american'],['american','spirit'],['spirit','mankind'],['mankind','spirit'],['creative','spirit'],['spirit','creative'],['alien','spirit'],['spirit','alien'],['america','spirit'],['spirit','america'],['founding','spirit'],['spirit','founding'],['diamond','spirit'],['spirit','diamond'],['spirit','democratic'],['spirit','democracy'],['democracy','spirit'],['democratic','spirit'],['hegel','spirit'],['spirit','hegel'],['spirit','nationality'],['nationality','spirit'],['nationalist','spirit'],['spirit','nationalist'],['nationalism','spirit'],['spirit','nationalism'],['guiding','spirit'],['spirit','guiding'],['spirit','guide'],['guide','spirit'],['phenomenology','spirit'],['spirit','phenomenology'],['world','spirit'],['spirit',' world'],['national','spirit'],['spirit','national'],['spirit','times'],['times','spirit'],['spirit','age'],['age','spirit'],['popular','spirit'],['spirit','popular'],['people','spirit'],['spirit','people'],['guild','spirit'],['spirit','guild'],['chirstianity','spirit'],['spirit','christianity'],['christian','spirit'],['spirit','christian'],['human','spirit'],['spirit','human'],['century','spirit'],['spirit', 'century'],['common','spirit'],['spirit','common'],['nationalist','spirit'],['spirit','nationalist'],['spirit','constitutional'],['constitutional','spirit'],['spirit','article'],['article','spirit'],['spirit','montesquieu'],['montesquieu','spirit'],['spirit','allen'],['allen','spirit'],['constitutional','spirit'],['spirit','constitutional'],['charter','spirit'],['spirit','charter'],['book','spirit'],['spirit','book'],['written','spirit'],['spirit','written'],['spirit','political'],['political','spirit'],['spirit','law'],['law','spirit'],['spirit','laws'],['laws','spirit'],['spirit','constitution'],['constitution','spirit'],['spirit','letter'],['letter','spirit'],['spirit','letters'],['letters','spirit'],['republican','spirit'],['spirit','republican'],['spirit','government'],['government','spirit'],['spirit','constitutionalism'],['constitutionalism','spirit'],['spirit','republicanism'],['republicanism','spirit'],['spirit','weber'],['weber','spirit'],['work','spirit'],['spirit','work'],['spirit','capitalism'],['capitalism','spirit'],['ethic','spirit'],['spirit','ethic'],['ethics','spirit'],['spirit','ethics'],['protestant','spirit'],['spirit','protestant'],['entrepreneurial','spirit'],['spirit','entrepreneurial'],['entrepreneur','spirit'],['spirit','entrepreneur'],['enterprise','spirit'],['spirit','enterprise'],['spirit','capitalism'],['isolation','spiritual'],['spiritual','isolation'],['spiritual','energies'],['energies','spiritual'],['talcott','spirit'],['spirit','talcott'],['parsons','spirit'],['spirit','parsons']]

#go through each entry in bi, check through each entry in allBi, if !=, add to notCounted

#count of spirit per year

for i in range(len(uniList)):
    if pubYear[i] not in Spirit:
        Spirit[pubYear[i]]=uniList[i]['spirit']
    else:
        Spirit[pubYear[i]]+=uniList[i]['spirit']
        

#run functions to create each author dict
dictAdd(Weber, biList, WeberList)
dictAdd(Mont, biList, MontList)
dictAdd(Hegel, biList, HegelList)
dictAdd(Diamond, biList, DiamondList)
dictAdd(Beard, biList, BeardList)
dictAdd(Macy, biList, MacyList)
dictAddTri(Macy, triList, MacyThree)
dictAdd(Rugg, biList, RuggList)
dictAdd(Pye, biList, PyeList)
dictAdd(Misc, biList, MiscList)
dictAddUni(Misc, uniList, MiscOne)
dictAddTri(Wilson, triList, WilsonThree)
dictAdd(Wilson, biList, WilsonList)
dictAdd(Ari, biList, AriList)
dictAddUni(Ari, uniList, AriOne)
dictAdd(Religion, biList, ReligionList)
dictAddUni(Religion, uniList, ReligionUni)   
dictAdd(Aquinas, biList, AquinasList)
dictAdd(Voe, biList, VoeList)
dictAdd(Vatican, biList, VaticanList)

#dictAdd(Christianity, biList, ChristianityList)
#dictAdd(Islam, biList, IslamList)
#dictAdd(Christian, biList, ChristianList)
#dictAdd(Ecu, biList, EcuList)
#dictAdd(Holy, biList, HolyList)
#dictAdd(Relig, biList, ReligList)
#dictAddUni(Spirituality, uniList, SpiritualityList)
#dictAddUni(Spiritual, uniList, SpiritualList)
  
SpiritP=pd.Series(Spirit).sort_index()
WeberP=pd.Series(Weber).sort_index()
MontP=pd.Series(Mont).sort_index()
HegelP=pd.Series(Hegel).sort_index()
DiamondP=pd.Series(Diamond).sort_index()
BeardP=pd.Series(Beard).sort_index()
MacyP=pd.Series(Macy).sort_index()
RuggP=pd.Series(Rugg).sort_index()
PyeP=pd.Series(Pye).sort_index()
MiscP=pd.Series(Misc).sort_index()
WilsonP=pd.Series(Wilson).sort_index()
AriP=pd.Series(Ari).sort_index()
ReligionP=pd.Series(Religion).sort_index()
AquinasP=pd.Series(Aquinas).sort_index()
VoeP=pd.Series(Voe).sort_index()
VaticanP=pd.Series(Vatican).sort_index()
#ChristianityP=pd.Series(Christianity).sort_index()
#IslamP=pd.Series(Islam).sort_index()
#ChristianP=pd.Series(Christian).sort_index()
#EcuP=pd.Series(Ecu).sort_index()
#HolyP=pd.Series(Holy).sort_index()
#ReligP=pd.Series(Relig).sort_index()
#SpiritualityP=pd.Series(Spirituality).sort_index()
#SpiritualP=pd.Series(Spiritual).sort_index()




"""to get series into .csv, uncomment line and fill in with wanted file. Freq was calcualted in spreadsheets
then converted from spreadsheet to csv for later plots"""
WeberP.to_csv("weberS.csv")
WilsonP.to_csv("wilsonS.csv")
MontP.to_csv("MontS.csv")
HegelP.to_csv("HegelS.csv")
DiamondP.to_csv("DiamondS.csv")
MontP.to_csv("MontS.csv")
MacyP.to_csv("MacyS.csv")
MiscP.to_csv("MiscS.csv")
ReligionP.to_csv("ReligionS.csv")
BeardP.to_csv("BeardS.csv")