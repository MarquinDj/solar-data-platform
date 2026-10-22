import psycopg
import os
from dotenv import load_dotenv
from pathlib import Path

from solar_data_platform.paths import ENV


def connect_db() -> psycopg.Connection:

    load_dotenv(dotenv_path=ENV)

    conn = psycopg.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=5432,
    )
    return conn


def insert_db_data(path: Path) -> None:
    query = (
        "COPY raw.irradiance (date,allsky_sfc_sw_dwn,t2m,longitude,latitude,elevation)"
        " FROM STDIN (FORMAT CSV, HEADER)"
    )
    with connect_db() as conn:
        with conn.cursor() as cur:
            with cur.copy(query) as copy:
                with open(path, "r", encoding="utf-8") as f:
                    while bloco := f.read(8192):
                        copy.write(bloco)
