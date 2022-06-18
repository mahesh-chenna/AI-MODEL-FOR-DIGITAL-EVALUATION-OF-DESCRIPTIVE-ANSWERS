from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('finaldataset.csv')
xf = df[['keyword', 'grammar', 'qst']]
# intigrate keyword, grammar, qst :)
''''
keywords and qst:
e = 1
vg = 2
g = 3
o = 4
p = 5
vp = 6

Grammar:
y = 1
n = 0

class labels 0.1 to 0.9 simplifies to 0 to 9 for calculation purpose
'''

x = np.array(xf.values)
yf = df[['class']]
y = np.array(yf.values).ravel()
clf = GaussianNB()
clf.fit(x,y)

with open('nav_test.pickle','wb') as f:
    pickle.dump(clf, f)

pickle_in = open('nav_test.pickle', 'rb')
clf = pickle.load(pickle_in)


def predict(k, g, q):
    predicted = clf.predict([[k, g, q]])
    accuracy = clf.predict_proba([[k, g, q]])
    print("class[1-9] : " + str(predicted))
    print("accuracy=",np.max(accuracy))
    #print(np.max(accuracy))
    return predicted

