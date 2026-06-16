import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from google import genai
from dotenv import load_dotenv
import os
import base64

# reading the data from excel file
df = pd.read_excel("Adidas.xlsx")
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
# Gemini Setup
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
st.set_page_config(layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown(
    "<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True
)
image = Image.open("adidas-logo.jpg")


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


logo_base64 = get_base64_image("adidas-logo.jpg")
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image(image, width=100)

html_title = """
    <style>
    .title-test {
    font-weight:bold;
    padding:5px;
    border-radius:6px;
    }
    </style>
    <center><h1 class="title-test">Adidas Interactive Sales Dashboard With AI Chatbot</h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html=True)

col3, col4, col5 = st.columns([0.1, 0.45, 0.45])
with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by:  \n {box_date}")

with col4:
    fig = px.bar(
        df,
        x="Retailer",
        y="TotalSales",
        labels={"TotalSales": "Total Sales {$}"},
        title="Total Sales by Retailer",
        hover_data=["TotalSales"],
        template="gridon",
        height=500,
    )
    st.plotly_chart(fig, use_container_width=True)

_, view1, dwn1, view2, dwn2 = st.columns([0.15, 0.20, 0.20, 0.20, 0.20])
with view1:
    expander = st.expander("Retailer wise Sales")
    data = df[["Retailer", "TotalSales"]].groupby(by="Retailer")["TotalSales"].sum()
    expander.write(data)
with dwn1:
    st.download_button(
        "Get Data",
        data=data.to_csv().encode("utf-8"),
        file_name="RetailerSales.csv",
        mime="text/csv",
    )

df["Month_Year"] = df["InvoiceDate"].dt.strftime("%b'%y")
result = df.groupby(by=df["Month_Year"])["TotalSales"].sum().reset_index()

with col5:
    fig1 = px.line(
        result,
        x="Month_Year",
        y="TotalSales",
        title="Total Sales Over Time",
        template="gridon",
    )
    st.plotly_chart(fig1, use_container_width=True)

with view2:
    expander = st.expander("Monthly Sales")
    data = result
    expander.write(data)
with dwn2:
    st.download_button(
        "Get Data",
        data=result.to_csv().encode("utf-8"),
        file_name="Monthly Sales.csv",
        mime="text/csv",
    )

st.divider()

result1 = df.groupby(by="State")[["TotalSales", "UnitsSold"]].sum().reset_index()

# add the units sold as a line chart on a secondary y-axis
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=result1["State"], y=result1["TotalSales"], name="Total Sales"))
fig3.add_trace(
    go.Scatter(
        x=result1["State"],
        y=result1["UnitsSold"],
        mode="lines",
        name="Units Sold",
        yaxis="y2",
    )
)
fig3.update_layout(
    title="Total Sales and Units Sold by State",
    xaxis=dict(title="State"),
    yaxis=dict(title="Total Sales", showgrid=False),
    yaxis2=dict(title="Units Sold", overlaying="y", side="right"),
    template="gridon",
    legend=dict(x=1, y=1.1),
)
_, col6 = st.columns([0.1, 1])
with col6:
    st.plotly_chart(fig3, use_container_width=True)

_, view3, dwn3 = st.columns([0.5, 0.45, 0.45])
with view3:
    expander = st.expander("View Data for Sales by Units Sold")
    expander.write(result1)
with dwn3:
    st.download_button(
        "Get Data",
        data=result1.to_csv().encode("utf-8"),
        file_name="Sales_by_UnitsSold.csv",
        mime="text/csv",
    )
st.divider()

_, col7 = st.columns([0.1, 1])
treemap = (
    df[["Region", "City", "TotalSales"]]
    .groupby(by=["Region", "City"])["TotalSales"]
    .sum()
    .reset_index()
)


def format_sales(value):
    if value >= 0:
        return "{:.2f} Lakh".format(value / 1_000_00)


treemap["TotalSales (Formatted)"] = treemap["TotalSales"].apply(format_sales)

fig4 = px.treemap(
    treemap,
    path=["Region", "City"],
    values="TotalSales",
    hover_name="TotalSales (Formatted)",
    hover_data=["TotalSales (Formatted)"],
    color="City",
    height=700,
    width=600,
)
fig4.update_traces(textinfo="label+value")

with col7:
    st.subheader(":point_right: Total Sales by Region and City in Treemap")
    st.plotly_chart(fig4, use_container_width=True)

_, view4, dwn4 = st.columns([0.5, 0.45, 0.45])
with view4:
    result2 = (
        df[["Region", "City", "TotalSales"]]
        .groupby(by=["Region", "City"])["TotalSales"]
        .sum()
    )
    expander = st.expander("View data for Total Sales by Region and City")
    expander.write(result2)
with dwn4:
    st.download_button(
        "Get Data",
        data=result2.to_csv().encode("utf-8"),
        file_name="Sales_by_Region.csv",
        mime="text.csv",
    )

_, view5, dwn5 = st.columns([0.5, 0.45, 0.45])
with view5:
    expander = st.expander("View Sales Raw Data")
    expander.write(df)
with dwn5:
    st.download_button(
        "Get Raw Data",
        data=df.to_csv().encode("utf-8"),
        file_name="SalesRawData.csv",
        mime="text/csv",
    )
st.divider()

# ==================================
# AI CHATBOT
# ==================================

# 1. Initialize session state for toggling the chatbot visibility
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False

# 2. Header Layout (Logo + Toggle Button)
col1, col2 = st.columns([1, 8])
with col1:
    st.image("adidas-logo.jpg", width=60)
with col2:
    if st.button("🤖 Adidas AI Assistant"):
        st.session_state.show_chat = not st.session_state.show_chat

# 3. Chatbot UI and Logic
if st.session_state.show_chat:
    st.header("🤖 Adidas AI Assistant")

    question = st.text_input("Ask about Adidas sales data", key="chat_question")

    if question:
        q = question.lower()

        # Keywords that route queries to the Gemini LLM instead of standard local filtering
        business_keywords = [
            "insight", "strategy", "marketing", "improve", "growth",
            "opportunity", "recommend", "recommendation", "executive summary",
            "future", "increase sales", "increase profit", "why are sales low",
            "business", "how can", "how to", "suggest", "advice",
            "improve profit", "improve sales"
        ]

        chart = None
        answer = ""

        try:
            # --- Retailer Analysis ---
            if "retailer" in q:
                result = (
                    df.groupby("Retailer")["TotalSales"]
                    .sum()
                    .sort_values(ascending=False)
                    .reset_index()
                )
                chart = px.bar(
                    result.head(10),
                    x="Retailer",
                    y="TotalSales",
                    title="Top Retailers by Sales",
                )
                answer = result.head(10).to_string(index=False)

            # --- State Analysis ---
            elif "state" in q:
                result = (
                    df.groupby("State")["TotalSales"]
                    .sum()
                    .sort_values(ascending=False)
                    .reset_index()
                )
                chart = px.bar(
                    result.head(10),
                    x="State",
                    y="TotalSales",
                    title="Top States by Sales",
                )
                answer = result.head(10).to_string(index=False)

            # --- Profit Analysis ---
            elif (
                q == "profit"
                or "profit analysis" in q
                or "top profit states" in q
                or "highest profit state" in q
            ):
                result = (
                    df.groupby("State")["OperatingProfit"]
                    .sum()
                    .sort_values(ascending=False)
                    .reset_index()
                )
                chart = px.bar(
                    result.head(10),
                    x="State",
                    y="OperatingProfit",
                    title="Top Profit States",
                )
                answer = result.head(10).to_string(index=False)

            # --- Monthly Trend ---
            elif "monthly" in q or "trend" in q:
                monthly = (
                    df.groupby(df["InvoiceDate"].dt.to_period("M"))["TotalSales"]
                    .sum()
                    .reset_index()
                )
                monthly["InvoiceDate"] = monthly["InvoiceDate"].astype(str)

                chart = px.line(
                    monthly,
                    x="InvoiceDate",
                    y="TotalSales",
                    title="Monthly Sales Trend",
                )
                answer = "Monthly Sales Trend Generated."

            # --- Product Analysis ---
            elif "product" in q:
                result = (
                    df.groupby("Product")["TotalSales"]
                    .sum()
                    .sort_values(ascending=False)
                    .reset_index()
                )
                chart = px.bar(
                    result, x="Product", y="TotalSales", title="Sales by Product"
                )
                answer = result.to_string(index=False)

            # --- Region Analysis ---
            elif "region" in q:
                result = (
                    df.groupby("Region")["TotalSales"]
                    .sum()
                    .sort_values(ascending=False)
                    .reset_index()
                )
                chart = px.bar(
                    result, x="Region", y="TotalSales", title="Sales by Region"
                )
                answer = result.to_string(index=False)

            # --- Business Strategy Questions (Routes to Gemini) ---
            elif any(word in q for word in business_keywords):
                # Dynamically construct a summary payload for the LLM context
                summary = f"""
                Total Sales: {df['TotalSales'].sum():,.2f}
                Total Profit: {df['OperatingProfit'].sum():,.2f}
                Total Units Sold: {df['UnitsSold'].sum():,.0f}

                Top Retailers:
                {df.groupby('Retailer')['TotalSales'].sum().sort_values(ascending=False).head(5).to_dict()}

                Top States:
                {df.groupby('State')['TotalSales'].sum().sort_values(ascending=False).head(5).to_dict()}

                Top Products:
                {df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False).head(5).to_dict()}

                Sales Method:
                {df.groupby('SalesMethod')['TotalSales'].sum().to_dict()}
                """

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"""
                    You are a Senior Business Analyst.

                    Dataset Summary:
                    {summary}

                    User Question:
                    {question}

                    Give actionable business recommendations.
                    """,
                )
                answer = response.text

            # --- Default Response for Unmatched Keywords ---
            else:
                answer = """
Try questions like:
• Top Retailers
• State Analysis
• Profit Analysis
• Product Analysis
• Region Analysis
• Monthly Sales Trend
• Business Insights
• Marketing Strategy
• Growth Opportunities
"""

            # Display text/data output from the query logic
            st.success(answer)

            # Display the chart dynamically if one was generated
            if chart is not None:
                st.plotly_chart(chart, use_container_width=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.markdown(
    f"""
    <style>

    .floating-logo {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 85px;
        height: 85px;
        border-radius: 50%;
        overflow: hidden;
        border: 4px solid #0066ff;
        box-shadow: 0px 0px 25px rgba(0,102,255,0.7);
        animation: float 3s ease-in-out infinite;
        z-index: 9999;
        background: white;
    }}

    .floating-logo img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}

    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
        100% {{ transform: translateY(0px); }}
    }}

    </style>

    <div class="floating-logo">
        <img src="data:image/jpeg;base64,{logo_base64}">
    </div>
    """,
    unsafe_allow_html=True,
)