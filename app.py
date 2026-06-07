import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Netflix Data Storytelling App")

df = pd.read_csv("netflix_titles.csv")

df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)

st.header("Dataset Introduction")

st.write("""
This dataset contains information about Netflix Movies and TV Shows.
""")

st.header("Dataset Preview")

st.dataframe(df.head())

st.header("Exploratory Data Analysis")

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

# Visualization 1
st.header("Movies vs TV Shows")

fig1 = px.pie(
    df,
    names="type",
    title="Movies vs TV Shows Distribution"
)

st.plotly_chart(fig1)

# Visualization 2
st.header("Netflix Content Growth Over Years")

year_count = df["release_year"].value_counts().sort_index()

fig2 = px.line(
    x=year_count.index,
    y=year_count.values,
    labels={"x":"Release Year","y":"Number of Titles"},
    title="Netflix Content Growth Over Years"
)

st.plotly_chart(fig2)

# Visualization 3
st.header("Top 10 Countries on Netflix")

top_countries = df["country"].value_counts().head(10)

fig3 = px.bar(
    x=top_countries.index,
    y=top_countries.values,
    labels={"x":"Country","y":"Content Count"},
    title="Top 10 Countries by Netflix Content"
)

st.plotly_chart(fig3)

st.header("Insights & Findings")

st.write("""
1. Netflix has significantly more Movies than TV Shows.

2. Content production increased rapidly after 2015.

3. The United States contributes the largest amount of Netflix content.

4. Netflix expanded aggressively during the last decade.
""")

st.header("Conclusion & Recommendations")

st.write("""
Netflix has experienced strong growth over the years.

Recommendations:

• Continue investing in international content.

• Expand successful TV Show productions.

• Focus on growing audiences in emerging markets.

• Maintain a balance between Movies and TV Shows.
""")