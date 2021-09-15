from typing import Tuple, List

import dash_html_components as html
import dash_leaflet as dl
from dash import Dash
from dash.dependencies import Input, Output
from flask import Flask
from timezonefinder import TimezoneFinderL

server = Flask(__name__)
app = Dash(prevent_initial_callbacks=True, server=server)
tf = TimezoneFinderL(in_memory=True)

url = "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png"
attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a> '

app.title = "Timezone Finder"
app.layout = html.Div(
    [
        dl.Map(
            [
                dl.TileLayer(url=url, maxZoom=20, attribution=attribution),
                dl.LayerGroup(id="layer"),
            ],
            id="map",
            style={
                "width": "100%",
                "height": "98vh",
                "margin": "none",
                "display": "block",
            },
        ),
    ]
)


@app.callback(Output("layer", "children"), [Input("map", "click_lat_lng")])
def map_click(click_lat_lng: Tuple[float, float]) -> List[dl.Marker]:
    lat, lng = click_lat_lng
    tz = tf.timezone_at(lat=lat, lng=lng)
    return [
        dl.Marker(
            position=click_lat_lng,
            children=dl.Tooltip(
                f"Timezone: {tz} ({lat:.3f}, {lng:.3f})", permanent=True
            ),
        )
    ]


if __name__ == "__main__":
    app.run_server(port=8080)
