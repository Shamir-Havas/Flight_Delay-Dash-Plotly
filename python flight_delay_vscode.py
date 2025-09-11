"""
Flight Delay Time Statistics Dashboard - VS Code Optimized
Author: Your Name
Date: 2025-09-09

Features:
- Compatible with Dash 2.15+ (uses app.run())
- Dark theme styling
- Hover tooltips on all charts
- Responsive layout
- Automatically opens browser
- Terminal prints progress
"""

# -----------------------------
# Step 0: Install Required Packages (run in terminal before executing script)
# -----------------------------
# pip install pandas dash plotly

# -----------------------------
# Step 1: Import Libraries
# -----------------------------
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import webbrowser

# -----------------------------
# Step 2: Load Airline Data
# -----------------------------
print("Loading airline data...")
airline_data = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
    encoding="ISO-8859-1",
    dtype={'Div1Airport': str, 'Div1TailNum': str, 'Div2Airport': str, 'Div2TailNum': str}
)
print("Data loaded successfully.")

# -----------------------------
# Step 3: Helper Function
# -----------------------------
def compute_info(df, year):
    """
    Computes monthly average delays per airline for a given year.
    Returns 5 DataFrames: Carrier, Weather, NAS, Security, Late Aircraft delays.
    """
    data = df[df['Year'] == int(year)]
    
    avg_carrier = data.groupby(['Month','Reporting_Airline'])['CarrierDelay'].mean().reset_index()
    avg_weather = data.groupby(['Month','Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    avg_NAS = data.groupby(['Month','Reporting_Airline'])['NASDelay'].mean().reset_index()
    avg_security = data.groupby(['Month','Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    avg_late = data.groupby(['Month','Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()
    
    return avg_carrier, avg_weather, avg_NAS, avg_security, avg_late

# -----------------------------
# Step 4: Initialize Dash App
# -----------------------------
app = Dash(__name__)
app.title = "Flight Delay Dashboard"

# -----------------------------
# Step 5: Layout
# -----------------------------
app.layout = html.Div([
    # Title
    html.H1(
        "Flight Delay Time Statistics",
        style={'textAlign':'center','color':'#F0F0F0','font-size':32,'margin-bottom':30,
               'background-color':'#2B2B2B','padding':20}
    ),
    
    # Year Input
    html.Div([
        html.Label("Select Year: ", style={'font-size':20,'margin-right':10,'color':'#F0F0F0'}),
        dcc.Input(
            id='input-year',
            type='number',
            value=2010,
            min=2010,
            max=2020,
            step=1,
            style={'height':35,'font-size':20,'width':100}
        )
    ], style={'textAlign':'center','margin-bottom':30,'background-color':'#2B2B2B','padding':10}),
    
    # Segment 1: Carrier & Weather Delays
    html.Div([
        html.Div(dcc.Graph(id='carrier-plot'), style={'width':'50%','padding':10}),
        html.Div(dcc.Graph(id='weather-plot'), style={'width':'50%','padding':10})
    ], style={'display':'flex'}),
    
    # Segment 2: NAS & Security Delays
    html.Div([
        html.Div(dcc.Graph(id='nas-plot'), style={'width':'50%','padding':10}),
        html.Div(dcc.Graph(id='security-plot'), style={'width':'50%','padding':10})
    ], style={'display':'flex'}),
    
    # Segment 3: Late Aircraft Delay
    html.Div(dcc.Graph(id='late-plot'), style={'width':'65%','margin':'auto','padding':20})
], style={'background-color':'#2B2B2B','font-family':'Arial, sans-serif'})

# -----------------------------
# Step 6: Callback
# -----------------------------
@app.callback(
    [
        Output('carrier-plot','figure'),
        Output('weather-plot','figure'),
        Output('nas-plot','figure'),
        Output('security-plot','figure'),
        Output('late-plot','figure')
    ],
    [Input('input-year','value')]
)
def update_graphs(year):
    print(f"Updating graphs for year: {year}...")
    avg_carrier, avg_weather, avg_NAS, avg_security, avg_late = compute_info(airline_data, year)
    
    template_style = 'plotly_dark'
    
    carrier_fig = px.line(avg_carrier, x='Month', y='CarrierDelay', color='Reporting_Airline',
                          title='Average Carrier Delay Time (minutes) by Airline', template=template_style,
                          hover_data={'Month':True, 'CarrierDelay':True, 'Reporting_Airline':True})
    
    weather_fig = px.line(avg_weather, x='Month', y='WeatherDelay', color='Reporting_Airline',
                          title='Average Weather Delay Time (minutes) by Airline', template=template_style,
                          hover_data={'Month':True, 'WeatherDelay':True, 'Reporting_Airline':True})
    
    nas_fig = px.line(avg_NAS, x='Month', y='NASDelay', color='Reporting_Airline',
                      title='Average NAS Delay (minutes) by Airline', template=template_style,
                      hover_data={'Month':True, 'NASDelay':True, 'Reporting_Airline':True})
    
    security_fig = px.line(avg_security, x='Month', y='SecurityDelay', color='Reporting_Airline',
                           title='Average Security Delay (minutes) by Airline', template=template_style,
                           hover_data={'Month':True, 'SecurityDelay':True, 'Reporting_Airline':True})
    
    late_fig = px.line(avg_late, x='Month', y='LateAircraftDelay', color='Reporting_Airline',
                       title='Average Late Aircraft Delay (minutes) by Airline', template=template_style,
                       hover_data={'Month':True, 'LateAircraftDelay':True, 'Reporting_Airline':True})
    
    return [carrier_fig, weather_fig, nas_fig, security_fig, late_fig]

# -----------------------------
# Step 7: Run the App
# -----------------------------
if __name__ == "__main__":
    print("Starting Flight Delay Dashboard...")
    webbrowser.open("http://127.0.0.1:8050/")  # open browser automatically
    app.run(debug=True, port=8050)
