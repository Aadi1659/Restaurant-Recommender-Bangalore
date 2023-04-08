import streamlit as st
import pickle
import pandas as pd

restaurants_dict = pickle.load(open("restaurants_dict.pkl","rb"))
restaurants = pd.DataFrame(restaurants_dict)
similarity = pickle.load(open("similarity.pkl",'rb'))

# print(restaurants['Name'])

def recommend(restaurant):
    restaurant_names = []
    index = restaurants[restaurants['Name'] == restaurant].index[0]
    distances = similarity[index]
    ourlist = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:21]

    for i in ourlist:
        restaurant_names.append(restaurants.iloc[i[0]].Name)
        # st.write(restaurants.iloc[i[0]].Name)
        # print(i[0])

    return restaurant_names

st.title("Bangalore Restaurant Recommender System")

selected_rest = options = st.selectbox("Select Restaurant",restaurants['Name'].values)

if st.button('Recommend'):
    names = recommend(selected_rest)

    for i in names:
        st.subheader(i)


    

