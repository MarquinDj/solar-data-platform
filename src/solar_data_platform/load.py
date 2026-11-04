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


def insert_db_data(path: Path) -> int:
    cols = "date,allsky_sfc_sw_dwn,t2m,longitude,latitude,elevation"

    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                CREATE TEMP TABLE irradiance_stage ON COMMIT DROP AS
                SELECT {cols} FROM raw.irradiance WITH NO DATA
            """)
            with cur.copy(
                f"COPY irradiance_stage ({cols}) FROM STDIN (FORMAT CSV, HEADER)"
            ) as copy:
                with open(path, "rb") as f:
                    while bloco := f.read(65536):
                        copy.write(bloco)
            cur.execute(f"""
                INSERT INTO raw.irradiance AS ri ({cols})
                SELECT {cols} FROM irradiance_stage
                ON CONFLICT (date, latitude, longitude) DO UPDATE
                SET allsky_sfc_sw_dwn = EXCLUDED.allsky_sfc_sw_dwn,
                t2m = EXCLUDED.t2m,
                elevation = EXCLUDED.elevation
                WHERE (ri.allsky_sfc_sw_dwn, ri.t2m, ri.elevation) IS DISTINCT FROM
                      (EXCLUDED.allsky_sfc_sw_dwn, EXCLUDED.t2m, EXCLUDED.elevation)
            """)
            return cur.rowcount

