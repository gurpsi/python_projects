# app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

# Read Excel file and get sheet names
excel_file = 'YOYR-EXCEL-FILE.xlsx'
excel_data = pd.ExcelFile(excel_file)
sheet_names = excel_data.sheet_names

# App layout
app.layout = html.Div([
    html.H1("Dynamic Visualization App"),
    
    # Dropdowns
    html.Div([
        html.Label("Select Sheet:"),
        dcc.Dropdown(id='sheet-dropdown', options=[{'label': sheet, 'value': sheet} for sheet in sheet_names], value=sheet_names[0]),
        
        html.Label("Select Visualization Type:"),
        dcc.Dropdown(
            id='visualization-type-dropdown',
            options=[
                {'label': 'Line Chart', 'value': 'line'},
                {'label': 'Scatter Plot', 'value': 'scatter'},
                {'label': 'Heatmap', 'value': 'heatmap'}
            ],
            value='line'
        ),
        
        html.Label("Select X-axis:"),
        dcc.Dropdown(id='x-axis-dropdown'),

        html.Label("Select Y-axis:"),
        dcc.Dropdown(id='y-axis-dropdown'),
    ], style={'width': '50%', 'display': 'inline-block'}),

    # Visualization Output
    dcc.Graph(id='visualization-output', style={'width': '70%', 'display': 'inline-block', 'padding': '0 20'}),

    # Data Table
    html.Div([
        html.Hr(),
        html.Label("Data Table:"),
        html.Div(id='data-table')
    ], style={'width': '70%', 'display': 'inline-block', 'padding': '0 20'})
])

# Callback to update X-axis and Y-axis dropdown options based on selected sheet
@app.callback(
    [Output('x-axis-dropdown', 'options'),
     Output('y-axis-dropdown', 'options')],
    [Input('sheet-dropdown', 'value')]
)
def update_dropdown_options(selected_sheet):
    df = pd.read_excel(excel_file, sheet_name=selected_sheet)
    columns = [{'label': col, 'value': col} for col in df.columns]
    return columns, columns

# Callback to update visualization based on user choices
@app.callback(
    Output('visualization-output', 'figure'),
    [Input('sheet-dropdown', 'value'),
     Input('visualization-type-dropdown', 'value'),
     Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)

# Heat map still not working
def update_visualization(selected_sheet, selected_type, x_axis, y_axis):
    try:
        df = pd.read_excel(excel_file, sheet_name=selected_sheet)

        if selected_type == 'line':
            figure = {
                'data': [{'x': df[x_axis], 'y': df[y_axis], 'type': 'line', 'mode': 'lines+markers'}],
                'layout': {'title': f'Line Chart - {selected_sheet}'}
            }
        elif selected_type == 'scatter':
            figure = {
                'data': [{'x': df[x_axis], 'y': df[y_axis], 'type': 'scatter', 'mode': 'markers'}],
                'layout': {'title': f'Scatter Plot - {selected_sheet}'}
            }
        elif selected_type == 'heatmap':
            # Use plotly express to create heatmap
            figure = px.imshow(df.pivot(index=x_axis, columns=y_axis, values=df.columns[2]))
            figure.update_layout(title=f'Heatmap - {selected_sheet}')
        else:
            figure = {'data': [], 'layout': {}}

        return figure
    except Exception as e:
        return {'data': [], 'layout': {}}


# Callback to update data table based on selected sheet or selected portion of the visualization
@app.callback(
    Output('data-table', 'children'),
    [Input('sheet-dropdown', 'value'),
     Input('visualization-output', 'selectedData')]
)
def update_data_table_combined(selected_sheet, selected_data):
    try:
        df = pd.read_excel(excel_file, sheet_name=selected_sheet)

        if selected_data is not None:
            selected_indices = [point['pointIndex'] for point in selected_data['points']]
            df = df.iloc[selected_indices]

        table = html.Table(
            [html.Tr([html.Th(col) for col in df.columns])] +
            [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))]
        )
        return table
    except Exception as e:
        return html.P(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run_server(debug=True)
