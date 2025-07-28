import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def show_visuals(df):
    numeric_cols = df.select_dtypes(include='number').columns

    # if len(numeric_cols) >= 2:
    #     st.write("Correlation Heatmap")
    #     corr = df[numeric_cols].corr()
    #     fig, ax = plt.subplots()
    #     sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    #     st.pyplot(fig)

    st.write("Basic Distribution")
    for col in numeric_cols[:3]:  # Show first 3 numeric columns
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)
