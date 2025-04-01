import os
import pandas as pd
from utils import compute_final_cpi, save_geojson_with_cpi, generate_cpi_map

# ================== CONFIG ==================
# Define paths
csv_path = "to request"
geojson_path = "to request"
out_csv = "to request"
out_geojson = "to request"
out_html = "to request"

# ============== PIPELINE ==============
print("📥 Loading CSV data...")
df = pd.read_csv(csv_path)

print("🧠 Computing CPI_final...")
df = compute_final_cpi(df)

print(f"💾 Saving final CPI to CSV → {out_csv}")
df.to_csv(out_csv, index=False)

print("🧩 Inserting CPI into GeoJSON...")
save_geojson_with_cpi(df, geojson_path, out_geojson)

print("🌍 Generating interactive map...")
generate_cpi_map(df, out_geojson, out_html)

print("✅ Pipeline completed.")
