from solar_data_platform.load import connect_db, insert_db_data
import pytest
from pathlib import Path
import psycopg
from collections.abc import Iterator


caminho_arquivo = Path(__file__).resolve().parent / "fixtures" / "clean.csv"

TEST_DB = "solar_test"

@pytest.fixture
def conn() -> Iterator[psycopg.Connection]:
    with connect_db(TEST_DB) as conn:
        conn.autocommit = True
        yield conn

@pytest.fixture
def clear_table(conn) -> Iterator[None]:
    conn.execute("TRUNCATE TABLE raw.irradiance RESTART IDENTITY;")
    yield

def test_insert_data(clear_table) -> None:
    rows_affected = insert_db_data(caminho_arquivo, TEST_DB)
    assert rows_affected == 31

def test_duplicate_data(clear_table, conn) -> None:
    insert_db_data(caminho_arquivo, TEST_DB)
    rows_affected = insert_db_data(caminho_arquivo, TEST_DB)
    assert rows_affected == 0
    rows_count = conn.execute("select COUNT(*) from raw.irradiance;").fetchone()[0]
    assert rows_count == 31


