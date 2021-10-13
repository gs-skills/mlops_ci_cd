import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fixDtypeWarning import getColumns
from fixDtypeWarning import makeTypeDict
# Read data
DATA_FOLDER= "./data/"
stackoverflowData = DATA_FOLDER + "raw/stackoverflowPost.csv"
typeColumns = DATA_FOLDER + "typeColumList.csv"
keysList = getColumns(stackoverflowData)
valueList = getColumns(typeColumns)
dtypeDict = makeTypeDict(keysList , valueList)

def dataPipiline(dataset):
    df = (
        pd.read_csv(dataset, dtype=dtypeDict)
        .rename(columns=str.lower)
        .drop(['unnamed: 0' , 'parent_id' , 'community_owned_date'], axis=1)
        .assign(
            last_activity_date = lambda x: pd.to_datetime(x['last_activity_date']),
            last_edit_date = lambda x: pd.to_datetime(x['last_activity_date']),
                )
        )
    return df
(   
    dataPipiline(stackoverflowData)
    .sample(frac=0.50, replace=False, random_state=45)
    .to_csv('../data/process/stackoverflowSample.csv', index=False)
)