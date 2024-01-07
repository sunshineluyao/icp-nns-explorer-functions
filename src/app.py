import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the CSV data from the provided link
url = "https://media.githubusercontent.com/media/sunshineluyao/icp-nns-db/main/data/proposals_no_empty.csv"
df = pd.read_csv(url)

# Prepare data for the line plot
action_nns_function_counts = df['action_nns_function'].value_counts().reset_index()
action_nns_function_counts.columns = ['Action NNS Function', 'Count']

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

# Create a line plot using Plotly Express with a log-scale y-axis
fig = px.line(action_nns_function_counts, x='Action NNS Function', y='Count', title='Distribution of Action NNS Functions', markers=True, line_shape='linear')
fig.update_traces(line_color='green')  # Set the line color to green
fig.update_yaxes(type="log")  # Set y-axis to logarithmic scale

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Internet Computer Protocol NNS Governance System Dashboard: Action NNS Function"),
    
    html.P([
        "Choose the proposal status to view the distributions of proposal action nns function. ",
        html.I("Notes: Action NNS Function is the specific NNS function targeted by the proposal; Status is the current standing of the proposal, be it pending, accepted, negated, or unsuccessful.")
    ]),

    dcc.Dropdown(
        id='status-dropdown',
        options=[
            {'label': status, 'value': status} for status in df['status'].unique()
        ],
        value=df['status'].unique()[0],
        multi=False
    ),
    dcc.Graph(id='bar-plot', figure=fig)  # Set the initial figure to the line plot
])

# Create a callback to update the plot based on the selected status
@app.callback(
    Output('bar-plot', 'figure'),
    Input('status-dropdown', 'value')
)
def update_bar_plot(selected_status):
    filtered_df = df[df['status'] == selected_status]
    action_nns_function_counts_filtered = filtered_df['action_nns_function'].value_counts().reset_index()
    action_nns_function_counts_filtered.columns = ['Action NNS Function', 'Count']

    fig = px.line(action_nns_function_counts_filtered, x='Action NNS Function', y='Count', title=f'Distribution of Action NNS Functions for {selected_status} Proposals', markers=True, line_shape='linear')
    fig.update_traces(line_color='green')  # Set the line color to green
    fig.update_yaxes(type="log")  # Set y-axis to logarithmic scale
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
