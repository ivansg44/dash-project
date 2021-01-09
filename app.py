import dash
import dash_cytoscape as cyto
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    cyto.Cytoscape(
        id="cytoscape-two-nodes",
        layout={"name": "preset"},
        stylesheet=[
            {
                "selector": ".data-edge",
                "style": {
                    "curve-style": "bezier",
                    "line-color": "black",
                    "target-arrow-color": "black",
                    "target-arrow-shape": "triangle"
                }
            },
            {
                "selector": ".data-node",
                "style": {
                    "background-color": "lightgrey",
                    "content": "data(label)",
                    "shape": "rectangle",
                    "padding": "100%",
                    "text-valign": "center",
                    "text-wrap": "wrap",
                    "width": "label"
                }
            },
            {
                "selector": ".x-axis-edge",
                "style": {
                    "line-color": "black"
                }
            },
            {
                "selector": ".x-axis-node",
                "style": {
                    "background-opacity": "0",
                    "content": "data(label)",
                    "text-valign": "bottom"
                }
            },            {
                "selector": ".y-axis-edge",
                "style": {
                    "line-color": "black"
                }
            },
            {
                "selector": ".y-axis-node",
                "style": {
                    "background-opacity": "0",
                    "content": "data(label)",
                    "text-halign": "left",
                    "text-valign": "center"
                }
            }
        ],
        elements=[
            # Data
            {
                "data": {"id": "one", "label": "ST512\nA"},
                "position": {"x": 50, "y": 10},
                "classes": "data-node"
            },
            {
                "data": {"id": "two", "label": "ST512\nB"},
                "position": {"x": 150, "y": 10},
                "classes": "data-node"
            },
            {
                "data": {"source": "one", "target": "two"},
                "classes": "data-edge"
            },
            # X-axis
            {
                "data": {"id": "x-0", "label": "0"},
                "position": {"x": 0, "y": 200},
                "classes": "x-axis-node"
            },
            {
                "data": {"id": "x-1", "label": "100"},
                "position": {"x": 100, "y": 200},
                "classes": "x-axis-node"
            },
            {
                "data": {"id": "x-2", "label": "200"},
                "position": {"x": 200, "y": 200},
                "classes": "x-axis-node"
            },
            {
                "data": {"source": "x-0", "target": "x-1"},
                "classes": "x-axis-edge"
            },
            {
                "data": {"source": "x-1", "target": "x-2"},
                "classes": "x-axis-edge"
            },
            # Y-axis
            {
                "data": {"id": "y-0", "label": "0"},
                "position": {"x": 0, "y": 200},
                "classes": "y-axis-node"
            },
            {
                "data": {"id": "y-1", "label": "100"},
                "position": {"x": 0, "y": 100},
                "classes": "y-axis-node"
            },
            {
                "data": {"id": "y-2", "label": "200"},
                "position": {"x": 0, "y": 0},
                "classes": "y-axis-node"
            },
            {
                "data": {"source": "y-0", "target": "y-1"},
                "classes": "y-axis-edge"
            },
            {
                "data": {"source": "y-1", "target": "y-2"},
                "classes": "y-axis-edge"
            }
        ]
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
