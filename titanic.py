import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title=" Titanic Dataset Explorer", layout="centered")
st.title(" Titanic Dataset Analysis & Insights")

# Upload section
uploaded_file = st.file_uploader(" Upload Titanic CSV", type=["csv"])

# Function to apply custom row styling for the gender table
def dark_row_style(df):
    styles = []
    for i in range(len(df)):
        bg_color = '#333333' if i % 2 == 0 else '#1e1e1e'  # alternate row dark shades
        styles.append([f'background-color: {bg_color}; color: #f5f5f5'] * len(df.columns))
    return pd.DataFrame(styles, index=df.index, columns=df.columns)

# When file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 1. Raw Data Preview
    st.subheader("🔍 Raw Data Preview")
    st.write(df.head())

    # 2. Gender-wise Analysis (Styled Table)
    if 'Sex' in df.columns and 'Age' in df.columns and 'Fare' in df.columns:
        st.subheader("👥 Gender-wise Average Age & Fare")
        result = df.groupby('Sex')[['Age', 'Fare']].mean().round(2).reset_index()
        styled_result = result.style.set_caption("💡 Average Age and Fare by Gender") \
                                     .format({'Age': '{:.2f}', 'Fare': '₹{:.2f}'}) \
                                     .apply(dark_row_style, axis=None)
        st.dataframe(styled_result, use_container_width=True)
    else:
        st.warning("⚠️ Gender table skipped. Columns 'Sex', 'Age', and 'Fare' not found.")

    # 3. Descriptive Statistics
    st.subheader(" Descriptive Statistics")
    numeric_stats = df.describe().round(2)
    st.dataframe(numeric_stats, use_container_width=True)

    # 4. Survival Distribution
    if 'Survived' in df.columns:
        st.subheader("🧍 Survival Distribution")
        survival_count = df['Survived'].value_counts().rename(index={0: 'Did Not Survive', 1: 'Survived'})
        st.bar_chart(survival_count)

    # 5. Passenger Class Distribution
    if 'Pclass' in df.columns:
        st.subheader("Passenger Class Distribution")
        class_count = df['Pclass'].value_counts().sort_index().rename(index={1: "1st Class", 2: "2nd Class", 3: "3rd Class"})
        st.bar_chart(class_count)

    # 6. Interpretation
    st.subheader(" Interpretation")
    st.markdown("""
    - The **descriptive statistics** summarize the spread and central tendencies of numeric variables like age and fare.
    - The **gender analysis** reveals differences in average age and ticket fare between males and females.
    - The **survival distribution** shows the number of passengers who survived and those who didn’t.
    - The **class breakdown** indicates most passengers traveled in 3rd class, historically linked to lower survival odds.
    """)

