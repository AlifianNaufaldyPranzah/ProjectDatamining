import joblib
import pandas as pd

def normalisasi(x):
    # import data test
    # cols = ["Age","Sex","ALT","AST"]
    cols = ["Age","Gender","Polyuria","Polydipsia","sudden weight loss","Polyphagia","weakness","Genital thrush","visual blurring","Itching","Irritability","delayed healing","partial paresis","Alopecia","Obesity"]
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('Pendat/datatestfix.csv')
    data_test = data_test.drop(data_test.columns[0],axis=1)
    # data_test = data_test.drop(data_test.columns[7:13],axis=1)
    # memasukkan data kedalam data test
    data_test = data_test.append(df,ignore_index = True)
    # print(data_test.columns)
    # print(data_test)
    # return data_test yang sudah dinormalisasi
    return joblib.load('Pendat/norma.sav').fit_transform(data_test)

def knn(x):
    
    return joblib.load('Pendat/KNNmodel14.pkl').predict(x)

def nb(x):
    
    return joblib.load('Pendat/modelNB.pkl').predict(x)

def dt(x):
    
    return joblib.load('Pendat/DTmodel.pkl').predict(x)