import streamlit as st

st.markdown(
        """
        Для того, чтобы тестировать модель машинного обучения, модель должна быть:
        
        1. Выгружена из jupiter notebook
        ```python
        
            from sklearn.neighbors import KNeighborsClassifier
            import joblib
            from google.colab import files
            
            n_neighbors=3

            model = KNeighborsClassifier(n_neighbors = n_neighbors)
            model.fit(X_train,y_train)

            score = model.score(X_test,y_test)
            print("The accuracy is ",score*100)
            
            # сохраним модель
            filename = 'knn_best_model.pkl'
            joblib.dump(model, filename)
            
            files.download('knn_best_model.pkl')
        ```
        
        2. Тренировать модель внутри веб-версии
        
        """
    )