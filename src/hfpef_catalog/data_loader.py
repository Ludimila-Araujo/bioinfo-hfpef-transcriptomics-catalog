import pandas as pd

from hfpef_catalog.config import SPREADSHEET_GID, build_sheet_url


def load_raw_sheet(url: str) -> pd.DataFrame:
    """
    Load a Google Sheet tab as a pandas DataFrame

    Parameters
    ----------
    url : str
        The CSV export URL of the target spreadsheet tab.

    Returns
    -------
    pd.DataFrame
        Data loaded from the spreadsheet, using the second row as the header.
    """
    df_species = pd.read_csv(url, header=1)
    return df_species


def load_all_species() -> dict[str, pd.DataFrame]:
    """
    Load the spreadsheet tabs configured for all cataloged species.

    Returns
    -------
    dict[str, pd.DataFrame]
        Dictionary mapping each species identifier to its DataFrame.
    """
    species_dictionary = {}
    df_species = {}

    for key, value in SPREADSHEET_GID.items():
        species_dictionary[key] = build_sheet_url(value)
        df_species[key] = load_raw_sheet(species_dictionary[key])

    return df_species


def consolidate_species(
    df_species: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    """
    Combine species-specific DataFrames into a single DataFrame.

    Parameters
    ----------
    df_species : dict[str, pd.DataFrame]
        Dictionary containing the DataFrame for each species.

    Returns
    -------
    pd.DataFrame
        Consolidated DataFrame with rows from all species, resetting the index.
    """
    return pd.concat(df_species.values(), ignore_index=True)
