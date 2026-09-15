SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1YTe8AkWDHRS-WPOq0ZIrlfv2Q_bPDlUavvhNmwOCyuo/export?format=csv&gid="
SPREADSHEET_GID = {
    "homo_sapiens": 1105806498,
    "mus_musculus": 982375450,
    "felis_catus": 1317070655,
}


def build_sheet_url(spread_gid):
    species_url = f"{SPREADSHEET_URL}{spread_gid}"
    return species_url
