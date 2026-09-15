import pandas as pd

from hfpef_catalog.config import SPREADSHEET_GID, build_sheet_url


def load_raw_sheet(url: str) -> pd.DataFrame:
    """
    Load a Google Sheet tab as a pandas DataFaame

    Parameters
    ----------
    url : str
        The CSV export URL of the target Google Sheets tab.

    Returns
    -------
    pd.DataFrame
        The raw, unprocessed data exactly as it appears in the sheet.
    """
    df_species = pd.read_csv(url, header=1)
    return df_species


def load_all_species():

    species_dictionary = {}
    df_species = {}

    for key, value in SPREADSHEET_GID.items():
        species_dictionary[key] = build_sheet_url(value)
        df_species[key] = load_raw_sheet(species_dictionary[key])

    return df_species
