padding = 800 * 0.1
# Start and end coordinates for both axes
start_coord = 0 - padding
end_coord = 800 + padding

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
        "position": {"x": 800/6 * 0, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "sep-2012", "label": "Sep\n2012"},
        "position": {"x": 800/6 * 1, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jun-2012", "label": "Jun\n2012"},
        "position": {"x": 800/6 * 2, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jul-2012", "label": "Jul\n2012"},
        "position": {"x": 800/6 * 3, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "nov-2014", "label": "Nov\n2014"},
        "position": {"x": 800/6 * 4, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "dec-2014", "label": "Dec\n2014"},
        "position": {"x": 800/6 * 5, "y": end_coord},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jan-2015", "label": "Jan\n2015"},
        "position": {"x": 800/6 * 6, "y": end_coord},
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
        "position": {"x": start_coord, "y": 800 / 4 * 0},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "tn4401b-2", "label": "Tn4401\nTn4401b-2\nIncN"},
        "position": {"x": start_coord, "y": 800 / 4 * 2},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "tn4401b-1", "label": "Tn4401\nTn4401b-1\nIncP,L/M"},
        "position": {"x": start_coord, "y": 800 / 4 * 4},
        "classes": "y-axis-node"
    },
    # Divider lines
    {
        "data": {"id": "left-divider-1.5"},
        "position": {"x": start_coord, "y": 800 / 4 * 0.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "right-divider-1.5"},
        "position": {"x": end_coord, "y": 800 / 4 * 0.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "left-divider-2.5"},
        "position": {"x": start_coord, "y": 800 / 4 * 3.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "right-divider-2.5"},
        "position": {"x": end_coord, "y": 800 / 4 * 3.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"source": "left-divider-1.5", "target": "right-divider-1.5"}
    },
    {
        "data": {"source": "left-divider-2.5", "target": "right-divider-2.5"}
    },
]
