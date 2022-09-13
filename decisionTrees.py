# pip install graphviz
# pip install pydotplus

# from os import sep
# import numpy as np



# from sklearn.model_selection import train_test_split 
# from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation



feature_cols = ['outlook','temperature','humidity','windy']

rows = [{'outlook':'sunny','temperature':'hot','humidity':'high','windy':'weak','playTennis':'no'},
        {'outlook':'sunny','temperature':'hot','humidity':'high','windy':'strong','playTennis':'no'},
        {'outlook':'overcast','temperature':'hot','humidity':'high','windy':'weak','playTennis':'yes'},
        {'outlook':'rainy','temperature':'mild','humidity':'high','windy':'weak','playTennis':'yes'},
        {'outlook':'rainy','temperature':'cool','humidity':'normal','windy':'weak','playTennis':'yes'},
        {'outlook':'rainy','temperature':'cool','humidity':'normal','windy':'strong','playTennis':'no'},
        {'outlook':'overcast','temperature':'cool','humidity':'normal','windy':'strong','playTennis':'yes'},
        {'outlook':'sunny','temperature':'mild','humidity':'high','windy':'weak','playTennis':'no'},
        {'outlook':'sunny','temperature':'cool','humidity':'normal','windy':'weak','playTennis':'yes'},
        {'outlook':'rainy','temperature':'mild','humidity':'normal','windy':'weak','playTennis':'yes'},
        {'outlook':'sunny','temperature':'mild','humidity':'normal','windy':'strong','playTennis':'yes'},
        {'outlook':'overcast','temperature':'mild','humidity':'high','windy':'strong','playTennis':'yes'},
        {'outlook':'overcast','temperature':'hot','humidity':'normal','windy':'weak','playTennis':'yes'},
        {'outlook':'rainy','temperature':'mild','humidity':'high','windy':'strong','playTennis':'no'},  
]

from os import pardir
import pandas as pd

df = pd.DataFrame(rows,index=None)
print(df)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
df['outlook'] = le.fit_transform(df['outlook'])
df['temperature'] = le.fit_transform(df['temperature'])
df['humidity'] = le.fit_transform(df['humidity'])
df['windy'] = le.fit_transform(df['windy'])

# df['outlook'].replace('sunny', 0,inplace=True)
# df['outlook'].replace('overcast', 1,inplace=True)
# df['outlook'].replace('rainy', 2,inplace=True)

# df['temperature'].replace('cool', 0,inplace=True)
# df['temperature'].replace('mild', 1,inplace=True)
# df['temperature'].replace('hot', 2,inplace=True)

# df['humidity'].replace('normal', 0,inplace=True)
# df['humidity'].replace('high', 1,inplace=True)

# df['windy'].replace('weak', 0,inplace=True)
# df['windy'].replace('strong', 1,inplace=True)

# df['playTennis'].replace('no', 0,inplace=True)
# df['playTennis'].replace('yes', 1,inplace=True)


print(df)

x = df[feature_cols]
y = df.playTennis
print(x,y,sep='\n')

from sklearn.tree import DecisionTreeClassifier 
# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(x,y)



from sklearn.tree import export_graphviz
from six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['no','yes'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('tree.png')
Image(graph.create_png())


test = [{'outlook':'sunny','temperature':'hot','humidity':'high','windy':'strong','playTennis':'no'},
          {'outlook':'overcast','temperature':'hot','humidity':'high','windy':'weak','playTennis':'no'}]


X_test = pd.DataFrame(test,index=None)
X_test['outlook'] = le.fit_transform(X_test['outlook'])
X_test['temperature'] = le.fit_transform(X_test['temperature'])
X_test['humidity'] = le.fit_transform(X_test['humidity'])
X_test['windy'] = le.fit_transform(X_test['windy'])
y_pred = clf.predict(X_test[feature_cols])
print(y_pred)
y_test = X_test['playTennis']
        
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
matrix = plot_confusion_matrix(clf,X_test[feature_cols],y_test,cmap=plt.cm.Reds)
matrix.ax_.set_title("confusion matrix",color ='white')
plt.xlabel('Predicted Label', color ='White')
plt.ylabel('True label', color ='white')
plt.show()
