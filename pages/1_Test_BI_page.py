import streamlit as st
from utils import get_dataframe

import seaborn as sns
from matplotlib import pyplot as plt
# importing libraries 
import altair as alt 

from urllib.error import URLError

df = get_dataframe()
st.title('page1: heatmap')
st.write('Тепловая карта корреляций')
sns.heatmap(df.corr(), cmap="viridis", annot=True, linewidth=0.5)

st.table(df.corr())

st.pyplot(plt)
