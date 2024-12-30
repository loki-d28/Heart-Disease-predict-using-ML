import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('hearts.csv')
print(df)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df['Sex']=le.fit_transform(df['Sex'])
df['ChestPainType']=le.fit_transform(df['ChestPainType'])
df['RestingECG']=le.fit_transform(df['RestingECG'])
df['ExerciseAngina']=le.fit_transform(df['ExerciseAngina'])
df['ST_Slope']=le.fit_transform(df['ST_Slope'])

x=df.drop(columns=['HeartDisease'])
y=df['HeartDisease']
print("XXXX",x)
print("YYYY",y)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=12)

from sklearn.naive_bayes import GaussianNB
NB=GaussianNB()
NB.fit(x_train,y_train)

y_pred=NB.predict(x_test)
print("y_pred",y_pred)
print("y_test",y_test)

from sklearn.metrics import accuracy_score
print('ACCURACY IS',accuracy_score(y_test,y_pred))

#prediction
      
model_prediction=NB.predict([[70,0,3,339,121,1,0,138,1,1,2]]
                            )
if model_prediction==1:
      print("patient has heart disease")
else:
    print("gud...patient is normal")
