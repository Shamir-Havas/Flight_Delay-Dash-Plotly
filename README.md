#✈️ Flight Delay Time Statistics Dashboard

A modern interactive dashboard to explore flight delay trends across U.S. airlines.

📖 About the Project

This project is an interactive data visualization dashboard that analyzes airline delay patterns in the U.S. between 2010–2020.
Using Dash, Plotly, and Pandas, the dashboard enables users to:

Explore monthly average delays across airlines

Compare delay causes such as Carrier, Weather, NAS, Security, and Late Aircraft

Get insights into how delays vary by year and airline

This project demonstrates my data science & visualization skills through:

📊 Data preprocessing & aggregation in Pandas

🎨 Interactive, responsive charts in Plotly Dash

🖥️ Full-stack deployment of a dashboard

🔄 Clean modular code optimized for VS Code

📸 Demo / Screenshots
<p align="center"> <img src="assets/dashboard_home.png" alt="Dashboard Screenshot 1" width="700"/> </p> <p align="center"> <img src="assets/dashboard_charts.png" alt="Dashboard Screenshot 2" width="700"/> </p>
✨ Features

✅ Interactive year selection with real-time chart updates

✅ Five detailed delay categories: Carrier, Weather, NAS, Security, Late Aircraft

✅ Dark theme styling for professional look & readability

✅ Hover tooltips on all charts for better insights

✅ Responsive layout (works across screen sizes)

✅ Automatic browser launch when running the app

🛠 Tech Stack

Programming Language: Python 3.x

Libraries: Pandas, Plotly Express, Dash

Tools: Jupyter/VS Code, Git, Web Browser

Dataset: Airline Delay Data (2010–2020)

🔄 Workflow / Project Pipeline

Data Loading – Import flight delay dataset (CSV from IBM Skills Network)

Data Processing – Compute monthly averages of different delay categories

Dashboard Design – Layout built using Dash HTML & Core Components

Visualization – Line plots using Plotly Express with dark theme

Interactivity – Callback functions update charts dynamically based on year input

Execution – Run locally with automatic browser launch

📊 Results & Insights

Airlines experience different seasonal delay trends across categories.

Weather delays show higher peaks in winter months.

Carrier-related delays vary significantly among airlines.

The dashboard allows users (airlines, researchers, passengers) to identify root causes of delays.

⚡ How to Run Locally
# Clone this repository
git clone https://github.com/yourusername/flight-delay-dashboard.git  

# Navigate into the project folder
cd flight-delay-dashboard  

# Install dependencies
pip install pandas dash plotly  

# Run the app
python python_flight_delay_vscode.py  


Once running, the dashboard will open automatically in your browser:
👉 http://127.0.0.1:8050/

🚀 Future Improvements

🌍 Deploy on cloud (Heroku, AWS, or Streamlit Cloud)

📈 Add forecasting models (ARIMA / Prophet) for delay prediction

🧠 Integrate ML classification for predicting probability of delays

📊 Enhance visuals with airline ranking dashboards
