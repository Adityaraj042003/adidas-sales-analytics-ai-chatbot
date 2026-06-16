# Adidas Sales Analytics Dashboard with AI Chatbot

An AI-powered sales analytics solution designed to help business users analyze sales performance, identify growth opportunities, and make data-driven decisions through interactive dashboards and intelligent business recommendations.

---

## 🛠 Tools & Technologies

### Python

Used as the primary programming language for building the complete analytics application, handling data processing, dashboard logic, and AI integration.

### Streamlit

Used to develop the interactive web-based dashboard and integrate analytics with AI capabilities in a single application.

### Pandas

Used for data cleaning, transformation, aggregation, and sales performance analysis across retailers, products, states, and regions.

### Plotly

Used to create interactive and dynamic visualizations that help users explore sales trends, profit analysis, and business performance.

### Google Gemini AI

Used to power the AI chatbot, enabling users to receive business insights, growth recommendations, marketing suggestions, and profit improvement strategies through natural language interaction.

### OpenPyXL

Used to read and process Excel-based sales datasets efficiently.

### Python Dotenv

Used to securely manage API keys and environment variables without exposing sensitive information in the source code.

### Pillow (PIL)

Used for image handling and customization within the dashboard interface.

### Excel

Used as the primary data source containing 9,649 Adidas sales records for analysis and visualization.

---

## 📌 Table of Contents

- [Overview](#overview)
* Business Problem
* Solution
* Dataset
* Project Structure
* Dashboard Features
* AI Chatbot Features
* Business Impact
* Why Streamlit Instead of Tableau?
* Future Enhancements
* How to Run This Project
* Author & Contact

---

## Overview

Organizations generate large amounts of sales data every day, but extracting meaningful insights from spreadsheets can be difficult and time-consuming.

This project was developed to simplify sales analysis by combining interactive data visualization with AI-powered business assistance.

The dashboard enables users to explore sales performance, profit trends, retailer performance, product insights, and regional sales distribution while interacting with an AI chatbot for business recommendations and decision support.

---

## Business Problem

Sales teams and business stakeholders often rely on spreadsheets and static reports to analyze performance.

This creates several challenges:

* Difficulty identifying top-performing retailers and regions
* Time-consuming manual analysis of sales data
* Limited visibility into profit and sales trends
* Challenges in identifying growth opportunities
* Non-technical users struggle to interpret large datasets

While traditional dashboards provide visualizations, they do not assist users in understanding what actions should be taken based on the data.

---

## Solution

To address these challenges, I developed an AI-powered Sales Analytics Dashboard that combines Business Intelligence with Generative AI.

The solution provides:

* Interactive sales analytics dashboard
* Retailer, state, region, and product analysis
* Profit performance tracking
* Monthly sales trend analysis
* Downloadable filtered data
* AI-powered chatbot for business queries
* Business recommendations and strategic insights

The goal is to transform raw sales data into actionable business intelligence that can support decision-making.

---

## Dataset

The project uses Adidas sales data containing:

### Dataset Details

**Records:** 9,649

### Variables

* Retailer ID
* Retailer
* Invoice Date
* Region
* State
* City
* Product
* Price Per Unit
* Units Sold
* Total Sales
* Operating Profit
* Sales Method

The dataset supports sales performance analysis across multiple business dimensions.

---

## Project Structure

```text
adidas-sales-analytics-ai-chatbot
│
├── app.py
├── Adidas.xlsx
├── adidas-logo.jpg
├── style.css
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dashboard Features

### Sales Analytics Dashboard

* Retailer Performance Analysis
* State-wise Sales Analysis
* Region-wise Sales Analysis
* Product Performance Analysis
* Profit Analysis
* Monthly Sales Trend Analysis
* Download Filtered Data
* Interactive Visualizations

### Business Analysis

The dashboard helps users identify:

* Top-performing retailers
* High-revenue regions
* Best-performing products
* Profit-generating states
* Monthly sales trends
* Sales method effectiveness

---

## AI Chatbot Features

The AI chatbot enables users to interact with the dashboard using natural language.

### Example Questions

* Top retailers by sales
* Which product performs best?
* Monthly sales trends
* How can Adidas improve profit?
* Suggest a marketing strategy
* What are the growth opportunities?

The chatbot combines dashboard analysis with Gemini AI-powered recommendations to provide actionable business insights.

---

## Business Impact

This solution helps organizations:

* Reduce manual reporting effort
* Improve decision-making speed
* Identify growth opportunities faster
* Understand sales performance more effectively
* Enable non-technical users to interact with business data

By integrating analytics with AI, the platform makes business intelligence more accessible and actionable.

---

## Why Streamlit Instead of Tableau?

While Tableau is a powerful Business Intelligence tool, this project required the integration of analytics and artificial intelligence within a single application.

Streamlit was chosen because it provides:

* Full Python integration
* Custom AI chatbot support
* Dynamic business logic implementation
* Flexible deployment options
* End-to-end analytics application development

This allowed the dashboard and AI assistant to work together within a unified platform.

---

## Future Enhancements

Future versions of the project may include:

* PandasAI Integration
* AI Agents for autonomous analysis
* RAG-based business intelligence
* Predictive sales forecasting
* Automated executive reporting
* Multi-dataset analytics support

---

## How to Run This Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Author & Contact

**Aditya Raj**

B.Tech Computer Science Engineering

Aspiring Data Analyst | Business Intelligence Enthusiast

📧 Email: [bhardwajaditya2536@gmail.com](mailto:bhardwajaditya2536@gmail.com)

💻 GitHub: https://github.com/Adityaraj042003

🔗 LinkedIn: https://www.linkedin.com/in/aditya-raj-a734b1279
