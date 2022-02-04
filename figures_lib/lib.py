import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go


def card(title, value):
    fig = go.Figure(go.Indicator(
        mode="number",
        value=value,
        title={"text": title},
        delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="lightgray")

    return fig