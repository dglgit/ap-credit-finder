import pandas as pd
import os
prefix='data/'
#TODO: make multi index for more cool stuff like listing exactly which classesare equivalent to the ap credit
def getFname(fname):
    return prefix+fname

def readFile(fname):
    df=pd.read_csv(fname)
    school=fname.split('_')[-1][:-4]
    return df, school
def lazyRead():
    files=os.listdir(prefix)
    dfs={}
    for f in files:
        df, school=readFile(prefix+f)
        df=df.set_index('Exam Name')
        dfs[school]=df
        #returns {school name: raw pandas df }
    return dfs


def handle_multiple(df):
    #fixes dataframe having duplicate aps
    dupes=df.index.duplicated()
    count=0
    counts={}
    new_index=list(df.index)
    for i in range(len(dupes)):
        if dupes[i]:
            name=new_index[i]
            if new_index[i] in counts:
                counts[new_index[i]]+=1
            else:
                counts[new_index[i]]=2
            new_index[i]=str(new_index[i])+str(counts[name])
    if len(set(new_index))!=len(new_index):
        print(new_index)
    return df.set_index(pd.Index(new_index))

def makeAcronym(name):
    return ''.join([word[0] for word in name.split(' ')])

def makeBigDf():
    files=os.listdir(prefix)
    dfs=[]
    names=[]
    for f in files:
        df, school=readFile(prefix+f)
        #print(df.columns)
        school=school.lower()
        df=df[['Exam Name','Minimum Score Required']].set_index('Exam Name')
        df.index=df.index.str.lower()
        df=df.rename(columns={"Minimum Score Required":school})

        df=handle_multiple(df)
        dfs.append(df)
        names.append(school)
        #print(df)
    catted=pd.concat(dfs,axis=1, sort=True)
    catted.to_csv("catted.csv")
    print(catted)
    return catted


big_df=makeBigDf()
def byAp(key,df=big_df):
    return df[df.index.str.contains(key)]
def bySchool(key, df=big_df):
    cols=[]
    for i in df.columns:
        if key in i:
            cols.append(i)
    return df[cols].dropna()

