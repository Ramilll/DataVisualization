import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

sns.set_palette("pastel")

from utils import load_data

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
    plt.show()

    #Survivals between Ages
    st.subheader('Survival distribution')
    plt.figure(figsize=(16, 9))
    ax = sns.violinplot(x ="Sex", y ="Age", hue ="Survived",data=df, split=True)
    fig = ax.get_figure()
    st.pyplot(fig)
    plt.show()


