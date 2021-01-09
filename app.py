import json

import dash
import dash_cytoscape as cyto
import dash_html_components as html

from elements import elements

app = dash.Dash(__name__)

with open("stylesheet.json") as fp:
    stylesheet = json.load(fp)

app.layout = html.Div([
    cyto.Cytoscape(
        id="cytoscape-two-nodes",
        layout={"name": "preset"},
        stylesheet=stylesheet,
        elements=elements
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)