# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 05:24:41 2018

@author: paipradeep
"""

import pandas as pd
from sklearn.utils import shuffle
import ipaddress
from os.path import splitext
from urllib.parse import urlparse
import tldextract

def filetoDF(file):
    file = "dataset2.csv"
    df = pd.read_csv(file)
    print(df.head())
    return df

def countDots(url):
    return url.count('.')

def countDelimiter(url):
    delim = ['&','?','=',';','_']
    count = 0
    for ch in url:
        if ch in delim:
            count += 1
    return count

def hyphenCount(url):
    return url.count('-')

def isIPaddress(domain):
    try:
        if ipaddress.ip_address(domain):
            return 1
    except:
        return 0
def atCount(url):
    return url.count('@')

def doubleSlashCount(url):
    return url.count('//')

def subDirCount(url):
    return url.count('/')

def fileExt(url):
    rest,extension = splitext(url)
    return extension

def subDomainCount(subdomain):
    if not subdomain:
        return 0
    else:
        return len(subdomain.split('.'))

def queryCount(query):
    if  not query:
        return 0
    return len(query.split('&'))

def suspiciousTLD(suffix):
    TLD = ['zip','cricket','link','work','party','gq','kim','country','science','tk']
    if suffix in TLD:
        return 1
    return 0

def extractFeatures(url,label):
    row = []
    print(url)
    parse = urlparse(url)
    extract = tldextract.extract(url)
    url = str(url)
    row.append(url)

    row.append(countDots(extract.subdomain))
    row.append(hyphenCount(parse.netloc))
    row.append(len(url))
    row.append(atCount(parse.netloc))
    row.append(doubleSlashCount(parse.path))
    row.append(subDirCount(parse.path))
    row.append(subDomainCount(extract.subdomain))
    row.append(len(parse.netloc))
    row.append(queryCount(parse.query))
    row.append(isIPaddress(extract.domain))
    row.append(suspiciousTLD(extract.suffix))
    row.append(label)
    return row

def makeDataset(file):
    featureSet = pd.DataFrame(columns=('url','no of dots','no of hyphen','len of url','presence of @',\
    'presence of //','no of subdir','no of subdomain','len of domain','no of queries','is IP','Suspicious_TLD',\
    'label'))
    df = filetoDF(file)
    for i in range(len(df)):
        features = extractFeatures(df["URL"].loc[i],df["Label"].loc[i])
        featureSet.loc[i] = features


#makeDataset(df)
