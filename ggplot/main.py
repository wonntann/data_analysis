import pandas as pd

# download dataset
download_url = (
    "https://www2.census.gov/programs-surveys/demo/tables/educational-attainment/2020/cps-detailed-tables/table-1-1.xlsx"
    "csv/datasets/educational-attainment"
)

df = pd.read_csv(download_url)
type(df)