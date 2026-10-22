import requests
import json
from pathlib import Path
import pandas as pd
import numpy as np


def fetch_json(url: str, params: dict) -> dict:
    try:
        data = requests.get(url, params, timeout=5)
        return data.json()
    except requests.exceptions.Timeout:
        print("A requisição demorou muito e foi cancelada.")


def get_power_daily(
    lat: int, long: int, community: str, start: str, end: str, format: str, parameters: str
) -> dict:
    power_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    params = {
        "latitude": lat,
        "longitude": long,
        "community": community,
        "start": start,
        "end": end,
        "format": format,
        "parameters": parameters,
    }
    return fetch_json(power_url, params)


def valid_response(payload: dict, max_missing: float = 0.45) -> None:

    parameters = [key for key in payload["parameters"]]
    missing_value = payload["header"]["fill_value"]

    percentage_missing = {}
    high_missing = {}

    for parameter in parameters:
        total = sum(1 for value in payload["properties"]["parameter"][f"{parameter}"].values())
        percentage_missing[parameter] = (
            sum(
                1
                for value in payload["properties"]["parameter"][f"{parameter}"].values()
                if value == missing_value
            )
            / total
        )
        if percentage_missing[parameter] > max_missing:
            high_missing[parameter] = percentage_missing[parameter]

    if len(high_missing) > 0:
        raise Exception(f"High missing values in parameters {high_missing}")


def save_data(json_data: dict, path: str, name: str) -> Path:
    path = Path(path) / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(json_data, indent=4, ensure_ascii=False), encoding="utf-8")
    return path


def clean_series(payload: dict) -> pd.DataFrame:
    fill_value = payload["header"]["fill_value"]
    lon, lat, elevation = payload["geometry"]["coordinates"]
    return (
        pd.DataFrame(payload["properties"]["parameter"])
        .reset_index(names="date")
        .replace(fill_value, np.nan)
        .assign(lon=lon, lat=lat, elevation=elevation)
    )


def save_dataframe(df: pd.DataFrame, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path
