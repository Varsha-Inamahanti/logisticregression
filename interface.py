import streamlit as st
import pickle

pickle_in=open('classifier.pkl','rb')
clf=pickle.load(pickle_in)
a=st.number_input('sepal length')
b=st.number_input('sepal width')
c=st.number_input('petal length')
d=st.number_input('petal width')
if st.button('predict'):
    result=clf.predict([[a,b,c,d]]).squeeze()
    if result==0:
        st.success('SETOSA')
    if result==1:
        st.success('VERSI COLOR')
    if result==2:
        st.success('VERGINICA')
