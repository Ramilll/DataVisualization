import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

from utils import load_data

with st.echo(code_location='below'):
    st.title("Titanic data exploration")

    data_load_state = st.text('Loading data...')

    df = load_data()

    data_load_state.text("Done! (using st.cache)")

    st.subheader('Raw Titanic data')
    st.write(df)

    st.subheader("# of people on Titanic by Age")

    hist_values = np.histogram(df["Age"], bins=24, range=(0,24))[0]

    st.bar_chart(hist_values)


