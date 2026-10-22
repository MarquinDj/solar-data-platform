CREATE TABLE irradiance (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    date DATE NOT NULL,
    latitude NUMERIC(4,2) NOT NULL,
    longitude NUMERIC(5,2) NOT NULL,
    elevation NUMERIC(6,2) NOT NULL,
    ALLSKY_SFC_SW_DWN NUMERIC(6,2),
    T2M NUMERIC (5, 2),

    CONSTRAINT uq_data_coordenadas UNIQUE (date, latitude, longitude)
);