from solar_data_platform.aux_func import valid_response, save_data, clean_series, save_dataframe
import pytest
import json
from pathlib import Path


caminho_arquivo = Path(__file__).resolve().parent / "fixtures" / "nasa_power_fortaleza.json"

# Abre e lê o arquivo JSON
with open(caminho_arquivo, "r", encoding="utf-8") as f:
    test_dict = json.load(f)


def test_valid_response_accept() -> None:
    assert valid_response(test_dict) is None


def test_valid_response_refuse() -> None:
    with pytest.raises(Exception):
        valid_response(test_dict, 0.10)


def test_save_raw(tmp_path) -> None:
    file = save_data(test_dict, tmp_path, "test.json")
    assert file.exists()


def test_clear_data() -> None:
    fill_value = test_dict["header"]["fill_value"]
    clean_json = clean_series(test_dict)
    assert fill_value not in clean_json.values


def test_save_clear(tmp_path) -> None:
    clean_json = clean_series(test_dict)
    file = save_dataframe(clean_json, tmp_path / "test.csv")
    assert file.suffix == ".csv"
