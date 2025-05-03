import os
import json
import streamlit as st
import pandas as pd

st.set_page_config(page_title="COVID-19 Dashboard", layout="centered")

# --- Load Data ---
if not os.path.exists("covid_data.json"):
    st.error(" 'covid_data.json' not found. Please add the file to your project folder.")
    st.stop()

with open("covid_data.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# --- Convert to DataFrame ---
df = pd.DataFrame(raw_data)

# --- Dashboard Title ---
st.title("COVID-19 Data Dashboard")
st.markdown("Get insights on total cases, deaths, and recoveries by country.")

# --- Summary Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric(" Total Cases", f"{df['cases'].sum():,}")
col2.metric(" Total Deaths", f"{df['deaths'].sum():,}")
col3.metric(" Total Recovered", f"{df['recovered'].sum():,}")

st.markdown("---")

# --- Country Selector ---
selected_country = st.selectbox("Select a Country", df["country"].sort_values())
country_data = df[df["country"] == selected_country].iloc[0]

st.subheader(f" Stats for {selected_country}")
st.write(f"**Population:** {country_data['population']:,}")
st.write(f"**Cases:** {country_data['cases']:,}")
st.write(f"**Deaths:** {country_data['deaths']:,}")
st.write(f"**Recovered:** {country_data['recovered']:,}")

st.markdown("---")

# --- Bar Chart ---
st.subheader(" COVID-19 Comparison by Country")
chart_df = df.set_index("country")[["cases", "deaths", "recovered"]]
st.bar_chart(chart_df)

# --- Footer ---
st.markdown(" Data Source: `covid_data.json` (Offline Mode)")

