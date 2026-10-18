from solar_data_platform.aux_func import (
    get_power_daily, 
    valid_response, 
    save_data, 
    clean_series, 
    save_dataframe)
from solar_data_platform.paths import RAW, PROCESSED
import datetime


##Definição doa dados
parameters = "ALLSKY_SFC_SW_DWN,T2M"
lat = -3.73
long = -38.52
community = "RE"
start = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y%m%d")
end = datetime.datetime.now().strftime("%Y%m%d")
format = "json"

##Coleta e validação dos dados
json_return = get_power_daily(lat, long, community, start, end, format, parameters)
response_validate = valid_response(json_return)

##Registrar os dados brutos
file_name = f"Fortaleza - {parameters} - {start} to {end}"
save = save_data(json_return, RAW, file_name)

##Salvar dados tratados
clean_json = clean_series(json_return)
save_dataframe(clean_json, PROCESSED / "clean.csv")