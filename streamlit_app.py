from utils import load_data
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from PIL import Image

sns.set_palette("pastel")


with st.echo(code_location='below'):
    st.title("Titanic data exploration")

    data_load_state = st.text('Loading data...')

    df = load_data()

    data_load_state.text("Loaded data using @st.cache")

    st.subheader('Raw Titanic data')
    st.write(df)

    # Ages distrubution
    st.subheader('#of people by age')
    fig = plt.figure(1, figsize=(16, 9))
    sns.histplot(df["Age"], bins=75)
    plt.title("# of people by Age", fontsize=13)
    st.pyplot(fig)

    # Ages distribution between classes
    st.subheader('Age distribution between p_classes')
    fig = plt.figure(3, figsize=(16, 9))
    for pclass in [1, 2, 3]:  # for 3 classes
        df.query("Pclass == @pclass")["Age"].plot(kind="kde")
    plt.title("Age distribution between p_classes")
    plt.legend(("1st", "2nd", "3rd"), fontsize=13)
    st.pyplot(fig)

    # Classes distribution
    st.subheader('Barchart of classes distribution')
    fig = plt.figure(5, figsize=(16, 9))
    plt.title(
        "Barchart of classes distribution", fontsize=13)
    df.Embarked.value_counts(normalize=True).plot(kind="bar", alpha=0.67)
    st.pyplot(fig)

    # Survivals between Ages
    st.subheader('Survival distribution')
    plt.figure(2, figsize=(16, 9))
    plt.title(
        "Violinplot of survival distribution among different ages and sex", fontsize=13)
    ax = sns.violinplot(x="Sex", y="Age", hue="Survived", data=df, split=True)
    fig = ax.get_figure()
    st.pyplot(fig)

    # Heatmap of survivals between classes
    st.subheader('Heatmap of survivals between classes')
    st.write(
        """ **pclass: A proxy for socio-economic status (SES)**: \n
    1st = Upper, 
    2nd = Middle, 
    3rd = Lower, 
    """)
    fig = plt.figure(4, figsize=(16, 9))
    plt.title(
        "Heatmap of survivals between classes", fontsize=13)
    group = df.groupby(['Pclass', 'Survived'])
    pclass_survived = group.size().unstack()
    sns.heatmap(pclass_survived, annot=True, fmt="d")
    st.pyplot(fig)

    # Port of Embarkation
    st.subheader('Distributions of survivals dependent on port of Embarkation')
    st.write("""
    C = Cherbourg, Q = Queenstown, S = Southampton
    """)
    fig = sns.catplot(x='Embarked', hue='Survived',
                      kind='count', col='Pclass', data=df)
    st.pyplot(fig)

    #Passengers fares
    st.subheader('Passengers fares')
    fig = px.scatter(df, x='Fare', y='Age', color='Survived', size='Fare')
    st.plotly_chart(fig)

    #3D diagramm (Pclass, Age, Fare)
    st.subheader('3D diagramm (Pclass, Age, Fare)')
    fig = px.scatter_3d(df, x='Pclass', y='Fare', z='Age',
              color='Survived')
    fig.show()
    st.plotly_chart(fig)

    #Now lets do something intercative
    fig = plt.figure(7, figsize=(16, 9))
    COLUMNS_TO_CHOOSE = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    st.subheader("Ok, lets go interactive!")
    column = st.selectbox('Choose a column', COLUMNS_TO_CHOOSE)
    st.write('You selected:', column)
    sns.histplot(df[column], bins=75)
    st.pyplot(fig)

    #Dowmload a picture of titanic
    st.subheader("Download picture of titanic")
    with open("titanic.png", "rb") as file:
     btn = st.download_button(
             label="Download picture of titanic",
             data=file,
             file_name="titanic.png",
             mime="image/png"
           )
