import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash_table import DataTable
import pandas as pd

# Global variables
EXCEL_FILE_PATH = 'Your_data.xlsx'
TARGET_COLUMN = 'Column_Name'

# Function to read data from Excel
def read_excel_data(sheet_name):
    try:
        df = pd.read_excel(EXCEL_FILE_PATH, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Error reading data: {str(e)}")
        return pd.DataFrame()

# Function to update dropdown options based on column names
def get_column_options(sheet_name):
    df = read_excel_data(sheet_name)
    columns = [{'label': col, 'value': col} for col in df.columns]
    return columns

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Dashboard"),  # Adding a header

    html.Label("Select Sheet:"),
    dcc.Dropdown(
        id='sheet-dropdown',
        options=[
            {'label': sheet, 'value': sheet} for sheet in pd.ExcelFile(EXCEL_FILE_PATH).sheet_names
        ],
        value=pd.ExcelFile(EXCEL_FILE_PATH).sheet_names[0],
        multi=False,
        clearable=False,
        style={'width': '50%'}
    ),

    html.Label("Select Unique Values from Column B:"),
    dcc.Dropdown(
        id='unique-values-dropdown',
        multi=True,
        style={'width': '50%'}
    ),

    html.Label("Select Visualization Type:"),
    dcc.Dropdown(
        id='visualization-type-dropdown',
        options=[
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Heatmap', 'value': 'heatmap'},
            {'label': 'Pie Chart', 'value': 'pie'},
        ],
        value='line',
        multi=False,
        clearable=False,
        style={'width': '50%'}
    ),

    html.Label("Select X-axis:"),
    dcc.Dropdown(id='x-axis-dropdown', style={'width': '50%'}),

    html.Label("Select Y-axis:"),
    dcc.Dropdown(id='y-axis-dropdown', style={'width': '50%'}),

    # Visualization component (Plotly chart)
    dcc.Graph(id='plotly-chart'),

    # Data display component (data table)
    DataTable(
        id='data-table',
        columns=[],
        style_table={'overflowX': 'auto'},
    )
])

# Callback to update unique values dropdown based on selected sheet
@app.callback(
    Output('unique-values-dropdown', 'options'),
    [Input('sheet-dropdown', 'value')]
)
def update_unique_values_dropdown(sheet_name):
    df = read_excel_data(sheet_name)
    unique_values = df[TARGET_COLUMN].unique().tolist() if TARGET_COLUMN in df.columns else []
    options = [{'label': val, 'value': val} for val in unique_values]
    return options

# Callback to update dropdown options based on selected visualization type
@app.callback(
    [Output('x-axis-dropdown', 'options'),
     Output('y-axis-dropdown', 'options')],
    [Input('visualization-type-dropdown', 'value'),
     Input('sheet-dropdown', 'value')]
)
def update_axis_dropdowns(visualization_type, sheet_name):
    return get_column_options(sheet_name), get_column_options(sheet_name)

# Callback to update the Plotly chart based on user selections
@app.callback(
    Output('plotly-chart', 'figure'),
    [Input('sheet-dropdown', 'value'),
     Input('unique-values-dropdown', 'value'),
     Input('visualization-type-dropdown', 'value'),
     Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
def update_plotly_chart(sheet_name, unique_values, visualization_type, x_axis, y_axis):
    try:
        df = read_excel_data(sheet_name)

        # Filter data based on unique values
        if unique_values:
            df = df[df[TARGET_COLUMN].isin(unique_values)] if TARGET_COLUMN in df.columns else df

        # Create Plotly figure based on visualization type
        if visualization_type == 'line':
            figure = {'data': [dict(x=df[x_axis], y=df[y_axis], type='line')],
                      'layout': dict(title=f'{visualization_type} Chart')}
        elif visualization_type == 'scatter':
            figure = {'data': [dict(x=df[x_axis], y=df[y_axis], mode='markers', type='scatter')],
                      'layout': dict(title=f'{visualization_type} Plot')}
        elif visualization_type == 'heatmap':
            # Implement heatmap logic
            figure = {'data': [], 'layout': {}}
        elif visualization_type == 'pie':
            # Implement pie chart logic
            figure = {'data': [], 'layout': {}}
        else:
            figure = {'data': [], 'layout': {}}

        return figure

    except Exception as e:
        print(f"Error updating Plotly chart: {str(e)}")
        return {'data': [], 'layout': {}}

# Callback to update data table based on user selections
@app.callback(
    Output('data-table', 'columns'),
    [Input('sheet-dropdown', 'value')]
)
def update_data_table_columns(sheet_name):
    df = read_excel_data(sheet_name)
    columns = [{'name': str(col), 'id': str(col)} for col in df.columns]
    return columns

# Callback to update data table based on user selections
@app.callback(
    Output('data-table', 'data'),
    [Input('sheet-dropdown', 'value'),
     Input('unique-values-dropdown', 'value')]
)
def update_data_table(sheet_name, unique_values):
    try:
        df = read_excel_data(sheet_name)

        # Filter data based on unique values
        if unique_values and TARGET_COLUMN in df.columns:
            df = df[df[TARGET_COLUMN].isin(unique_values)]

        print("DataFrame:")
        print(df)

        return df.to_dict('records')

    except Exception as e:
        print(f"Error updating data table: {str(e)}")
        return []

if __name__ == '__main__':
    app.run_server(debug=True)
