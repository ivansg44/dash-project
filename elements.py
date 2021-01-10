elements = [
    # x-axis
    {
        "data": {"id": "x-start"},
        "position": {"x": 0, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "x-end"},
        "position": {"x": 800, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"source": "x-start", "target": "x-end"},
        "classes": "axis-edge"
    },
    {
        "data": {"id": "oct-2011", "label": "Oct\n2011"},
        "position": {"x": 800/8 * 1, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "sep-2012", "label": "Sep\n2012"},
        "position": {"x": 800/8 * 2, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jun-2012", "label": "Jun\n2012"},
        "position": {"x": 800/8 * 3, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jul-2012", "label": "Jul\n2012"},
        "position": {"x": 800/8 * 4, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "nov-2014", "label": "Nov\n2014"},
        "position": {"x": 800/8 * 5, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "dec-2014", "label": "Dec\n2014"},
        "position": {"x": 800/8 * 6, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "jan-2015", "label": "Jan\n2015"},
        "position": {"x": 800/8 * 7, "y": 800},
        "classes": "x-axis-node"
    },
    # y-axis
    {
        "data": {"id": "y-start"},
        "position": {"x": 0, "y": 0},
        "classes": "x-axis-node"
    },
    {
        "data": {"id": "y-end"},
        "position": {"x": 0, "y": 800},
        "classes": "x-axis-node"
    },
    {
        "data": {"source": "y-start", "target": "y-end"},
        "classes": "axis-edge"
    },
    {
        "data": {"id": "tn4401a-1", "label": "Tn4401\nTn4401a-1\nIncFll(k)"},
        "position": {"x": 0, "y": 800/4 * 1},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "tn4401b-2", "label": "Tn4401\nTn4401b-2\nIncN"},
        "position": {"x": 0, "y": 800/4 * 2},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "tn4401b-1", "label": "Tn4401\nTn4401b-1\nIncP,L/M"},
        "position": {"x": 0, "y": 800/4 * 3},
        "classes": "y-axis-node"
    },
    # Divider lines
    {
        "data": {"id": "left-divider-1.5"},
        "position": {"x": 0, "y": 800 / 4 * 1.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "right-divider-1.5"},
        "position": {"x": 800, "y": 800 / 4 * 1.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "left-divider-2.5"},
        "position": {"x": 0, "y": 800 / 4 * 2.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"id": "right-divider-2.5"},
        "position": {"x": 800, "y": 800 / 4 * 2.5},
        "classes": "y-axis-node"
    },
    {
        "data": {"source": "left-divider-1.5", "target": "right-divider-1.5"}
    },
    {
        "data": {"source": "left-divider-2.5", "target": "right-divider-2.5"}
    },
]
