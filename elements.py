# TODO: could calculate graph_height based on longest label in graph
graph_height = 1200

padding = graph_height * 0.1

# Start and end coordinates for both axes
start_coord = 0 - padding
end_coord = graph_height + padding

# Node graph_heights
node_height = graph_height/5 * 0.5

elements = [
    # x-axis
    {
        "data": {"id": "x-start"},
        "position": {"x": start_coord, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "x-end"},
        "position": {"x": end_coord, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"source": "x-start", "target": "x-end"},
        "classes": "axis-edge"
    },
    {
        "data": {"id": "oct-2011", "label": "Oct\n2011"},
        "position": {"x": graph_height/6 * 0, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "sep-2012", "label": "Sep\n2012"},
        "position": {"x": graph_height/6 * 1, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jun-2012", "label": "Jun\n2012"},
        "position": {"x": graph_height/6 * 2, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jul-2012", "label": "Jul\n2012"},
        "position": {"x": graph_height/6 * 3, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "nov-2014", "label": "Nov\n2014"},
        "position": {"x": graph_height/6 * 4, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "dec-2014", "label": "Dec\n2014"},
        "position": {"x": graph_height/6 * 5, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jan-2015", "label": "Jan\n2015"},
        "position": {"x": graph_height/6 * 6, "y": end_coord},
        "classes": "x-axis-node"
    },
    # y-axis
    {
        "data": {"id": "y-start"},
        "position": {"x": start_coord, "y": start_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "y-end"},
        "position": {"x": start_coord, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"source": "y-start", "target": "y-end"},
        "classes": "axis-edge"
    },
    {
        "data": {"id": "tn4401a-1", "label": "Tn4401\nTn4401a-1\nIncFll(k)"},
        "position": {"x": start_coord, "y": graph_height/4 * 0},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "tn4401b-2", "label": "Tn4401\nTn4401b-2\nIncN"},
        "position": {"x": start_coord, "y": graph_height/4 * 2},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "tn4401b-1", "label": "Tn4401\nTn4401b-1\nIncP,L/M"},
        "position": {"x": start_coord, "y": graph_height/4 * 4},
        "classes": "y-axis-node"
    },
    # Divider lines
    {
        "data": {"id": "left-divider-1.5"},
        "position": {"x": start_coord, "y": graph_height/4 * 0.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "right-divider-1.5"},
        "position": {"x": end_coord, "y": graph_height/4 * 0.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "left-divider-2.5"},
        "position": {"x": start_coord, "y": graph_height/4 * 3.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "right-divider-2.5"},
        "position": {"x": end_coord, "y": graph_height/4 * 3.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"source": "left-divider-1.5", "target": "right-divider-1.5"}
    },
    {
        "data": {"source": "left-divider-2.5", "target": "right-divider-2.5"}
    },
    # ST512
    {
        "data": {"id": "st512-a", "label": "ST512\nA", "height": node_height},
        "position": {"x": graph_height/6 * 0, "y": graph_height/4 * 0},
        "classes": "square-node"
    },
    {
        "data": {"id": "st512-b", "label": "ST512\nB", "height": node_height},
        "position": {"x": graph_height/6 * 1, "y": graph_height/4 * 0},
        "classes": "square-node"
    },
    # ST252
    {
        "data": {"id": "st252-c", "label": "ST252\nC", "height": node_height},
        "position": {"x": graph_height/6 * 2, "y": graph_height/4 * 1},
        "classes": "square-node"
    },
    {
        "data": {"id": "st252-f", "label": "ST252\nF", "height": node_height},
        "position": {"x": graph_height/6 * 4, "y": graph_height/4 * 1},
        "classes": "square-node"
    },
    # ST354
    {
        "data": {"id": "st354-g", "label": "ST354\nG", "height": node_height},
        "position": {"x": graph_height/6 * 4, "y": graph_height/4 * 2},
        "classes": "circle-node"
    },
    {
        "data": {"id": "st354-h", "label": "ST354\nH", "height": node_height},
        "position": {"x": graph_height/6 * 5, "y": graph_height/4 * 2},
        "classes": "circle-node"
    },
    # ST1846
    {
        "data": {"id": "st1846-d-parent", "label": "Urine"},
        "classes": "parent-node"
    },
    {
        "data": {
            "id": "st1846-d",
            "label": "ST1846\nD",
            "height": node_height,
            "parent": "st1846-d-parent"
        },
        "position": {"x": graph_height/6 * 3, "y": graph_height / 4 * 3},
        "classes": "square-node"
    },
    {
        "data": {
            "id": "st1846-i",
            "label": "ST1846\nI",
            "height": node_height
        },
        "position": {"x": graph_height/6 * 6, "y": graph_height / 4 * 3},
        "classes": "square-node"
    },
    # Wound
    {
        "data": {"id": "wound-parent", "label": "Wound"},
        "classes": "parent-node"
    },
    {
        "data": {"id": "wound",
                 "label": "E",
                 "height": node_height,
                 "parent": "wound-parent"
                 },
        "position": {"x": graph_height/6 * 4, "y": graph_height/4 * 4},
        "classes": "triangle-node"
    },
    # Data edges
    {
        "data": {
            "source": "st512-a",
            "target": "st512-b",
            "label": "4 SNVs\n\u2800\n\u2800"
        },
        "classes": "data-edge"
    },
    {
        "data": {
            "source": "st252-c",
            "target": "st252-f",
            "label": "3 SNVs\n\u2800\n\u2800"
        },
        "classes": "data-edge"
    },
    {
        "data": {
            "source": "st252-c",
            "target": "st354-g",
            "label": "OR\n\u2800\n\u2800"
        },
        "classes": "data-edge dotted-edge"
    },
    {
        "data": {
            "source": "st252-c",
            "target": "st1846-d",
            "label": "\u2800\n\u2800\npRFLPA1"
        },
        "classes": "data-edge dotted-edge"
    },
    {
        "data": {
            "source": "st252-f",
            "target": "st354-g",
            "label": "\u2800\n\u2800\npRFLPA1"
        },
        "classes": "data-edge dotted-edge"
    },
    {
        "data": {
            "source": "st354-g",
            "target": "st354-h",
            "label": "38 SNVs\n\u2800\npRFLPA1"
        },
        "classes": "data-edge"
    },
    {
        "data": {
            "source": "st1846-d",
            "target": "st1846-i",
            "label": "6 SNVs\n\u2800\npRFLPA1"
        },
        "classes": "data-edge"
    }
]
