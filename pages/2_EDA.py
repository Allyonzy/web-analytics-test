from utils import get_dataframe
import streamlit as st
# importing libraries 
import altair as alt 
  
st.title('Исследовательский анализ данных')
st.write('Возьмем данные Титаника')
df = get_dataframe()

st.table(df.head(10))

st.write('Посмотрим сбалансированность данных')

plt_target = df[['survived']]
# making the simple histogram 
hist = alt.Chart(plt_target).mark_bar().encode(
    x = 'survived',
    y = 'count()'
    ).properties(
    height=350, 
    width=350,
    title="Количество выживших"
) 

st.altair_chart(hist, use_container_width=True)