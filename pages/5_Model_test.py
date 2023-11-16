import streamlit as st
from utils import get_dataframe, bagging_model_load, evaluate
import pandas as pd

dataframe = get_dataframe() # получить данные

# загрузка данных для тестирования моделей
st.write("Введите тестовую выборку")
uploaded_file_test = st.file_uploader("Загрузите файл данных (CSV)", type=["csv"])
st.write("Введите файл, с которым сравниваем (y, outcome)")
uploaded_file_y = st.file_uploader("Загрузите файл данных (CSV)", type=["csv"])


if uploaded_file_test is not None and uploaded_file_y is not None:
    
    data_test = pd.read_csv(uploaded_file_test)
    st.table(data_test.head())
    #  model_choice = st.radio("Выберите модель для тестирования", ["Модель knn", "Модель knn"])
    data_y = pd.read_csv(uploaded_file_y)
    st.table(data_y.head())
    model = bagging_model_load()
    evaluate(model, data_test, data_y)