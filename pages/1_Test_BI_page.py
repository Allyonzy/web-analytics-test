import streamlit as st
from utils import get_dataframe

import seaborn as sns
from matplotlib import pyplot as plt

from urllib.error import URLError

df = get_dataframe()
st.title('page1: heatmap')
st.write('Тепловая карта корреляций')
plt.figure(figsize=(15, 10), dpi=100)
sns.heatmap(df.corr(), cmap="viridis", annot=True, linewidth=0.5)
st.pyplot(plt)