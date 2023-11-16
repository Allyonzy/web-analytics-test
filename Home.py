import streamlit as st
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Классификатор",
    )

    st.write("# Задача машинного обучения")

    st.sidebar.success("Выберите раздел")

    st.markdown(
        """
        Использование машинного обучения для классификации по признаку эндокринного заболевания
        **👈 Список разделов** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - EDA [Анализ датасета и его описание](./EDA)
        - Демонстрация датафрейма [здесь](./DataFrame_Demo)
        - Тестирование модели [здесь](./Work_with_model)
        
        ### See more complex demos
    """
    )


if __name__ == "__main__":
    run()
