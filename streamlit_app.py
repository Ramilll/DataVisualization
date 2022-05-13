from utils import load_data
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

sns.set_palette("pastel")


with st.echo(code_location='below'):
    st.title("Titanic data exploration")

    data_load_state = st.text('Loading data...')

    df = load_data()

    data_load_state.text("Done! (using st.cache)")

    st.subheader('Raw Titanic data')
    st.write(df)

    # Ages distrubution
    st.subheader('#of people by age')
    fig = plt.figure(figsize=(16, 9))
    sns.histplot(df["Age"], bins=75)
    plt.title("# of people by Age", fontsize=13)
    st.pyplot(fig)

    # Survivals between Ages
    st.subheader('Survival distribution')
    plt.figure(figsize=(16, 9))
    plt.title(
        "Violinplot of survival distribution among different ages and sex", fontsize=13)
    ax = sns.violinplot(x="Sex", y="Age", hue="Survived", data=df, split=True)
    fig = ax.get_figure()
    st.pyplot(fig)

    # Heatmap of survivals between classes
    st.subheader('Heatmap of survivals between classes')
    plt.title(
        "Heatmap of survivals between classes", fontsize=13)
    fig = plt.figure(figsize=(16, 9))
    group = df.groupby(['Pclass', 'Survived'])
    pclass_survived = group.size().unstack()
    sns.heatmap(pclass_survived, annot=True, fmt="d")
    st.pyplot(fig)

    # Port of Embarkation
    st.subheader('Distributions of survivals dependent on port of Embarkation')
    fig = plt.figure(figsize=(16, 9))
    plt.title("Distributions of survivals dependent on port of Embarkation", fontsize=13)
    sns.catplot(x='Embarked', hue='Survived',
                kind='count', col='Pclass', data=df)
    st.pyplot(fig)
