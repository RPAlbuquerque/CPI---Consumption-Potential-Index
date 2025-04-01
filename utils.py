import os
import pandas as pd
import numpy as np
import json
import plotly.express as px

def log(msg):
    from datetime import datetime
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def calculate_cpi(df):
    df["CPI_final"] = np.log1p(df["total_visitas"]) * np.log1p(df["tempo_medio"]) * df["sentimento_medio"]
    return df

def save_to_geojson(df, geojson_path, output_geojson_path):
    with open(geojson_path, "r", encoding="utf-8") as f:
        geo = json.load(f)

    cpi_dict = df.set_index("CD_SETOR")["CPI_final"].to_dict()

    for feature in geo["features"]:
        setor = feature["properties"]["CD_SETOR"]
        feature["properties"]["CPI_final"] = round(cpi_dict.get(setor, np.nan), 4)

    with open(output_geojson_path, "w", encoding="utf-8") as f:
        json.dump(geo, f)

    log(f"✅ GeoJSON saved to: {output_geojson_path}")

def generate_interactive_map(df, geo, output_html_path):
    df["CD_SETOR"] = df["CD_SETOR"].astype(str)

    fig = px.choropleth_mapbox(
        df,
        geojson=geo,
        locations="CD_SETOR",
        featureidkey="properties.CD_SETOR",
        color="CPI_final",
        color_continuous_scale="YlGnBu",
        mapbox_style="carto-positron",
        zoom=3.5,
        center={"lat": -14.235, "lon": -51.9253},
        opacity=0.7,
        title="CPI Final por Setor Censitário",
        height=800
    )

    fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})
    fig.write_html(output_html_path)
    log(f"✅ Interactive map saved to: {output_html_path}")
