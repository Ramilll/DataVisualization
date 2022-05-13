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

    st.subheader('#of people by age')

    fig = plt.figure(figsize=(16, 9))
    sns.histplot(df["Age"], bins=75)
    plt.title("# of people by Age")
    st.pyplot(fig)


