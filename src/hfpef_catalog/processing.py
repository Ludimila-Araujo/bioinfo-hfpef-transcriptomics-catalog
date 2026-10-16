import pandas as pd


# Função para contar o número de espécies catalogadas
def count_all_species(df_species: dict[str, pd.DataFrame]) -> int:
    """
    Count the species represented in the loaded dataset collection.

    Parameters
    ----------
    df_species : dict[str, pd.DataFrame]
        Dictionary mapping species identifiers to their DataFrames.

    Returns
    -------
    int
        Number of species represented in the dictionary.
    """
    return len(df_species)


# Função para contar o número total de respositórios catalogados
def sum_all_repositories(
    df_species: dict[str, pd.DataFrame],
) -> int:
    """
    Count the total number of cataloged dataset records across
    all species DataFrames.

    Parameters
    ----------
    df_species : dict[str, pd.DataFrame]
        Dictionary mapping species identifiers to their DataFrames.

    Returns
    -------
    int
        Total number of rows across all species DataFrames.
    """

    total_repo = 0

    for df in df_species.values():
        species_repositories = len(df)
        total_repo += species_repositories

    return total_repo


# Função para contar quantidade de datasets por espécie:
def dataset_count(df: pd.DataFrame) -> int:
    """
    Count the dataset records represented in a species DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the cataloged datasets.

    Returns
    -------
    int
        Number of rows in the Dataset_ID column, including rows
        with missing identifiers.
    """

    return len(df["Dataset_ID"])


# Função para contar quantidade de tecidos estudados por repositório:
def tissue_count(df: pd.DataFrame) -> int:
    """
    Count the distinct sampled tissue categories in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the cataloged datasets.

    Returns
    -------
    int
        Number of unique values in the Sampled_Tissue column.
    """
    return df["Sampled_Tissue"].nunique()


# Função para calcular o percentual de datasets segundo categoria de sexo registrada
def sex_distribution(df: pd.DataFrame) -> dict[str, float]:
    """
    Calculate the percentage of dataset records in predefined
    recorded sex categories.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the cataloged datasets.

    Returns
    -------
    dict[str, float]
        Percentages for Female, Male, Male / female, and
        Not reported. Percentages use the total number of rows
        as the denominator. Actual missing values are not
        returned as a separate category.
    """

    sex_counts = df["Sex"].value_counts()
    total_datasets = len(df)

    return {
        "Female": (sex_counts.get("Female", 0) / total_datasets) * 100,
        "Male": (sex_counts.get("Male", 0) / total_datasets) * 100,
        "Male / female": (sex_counts.get("Male / female", 0) / total_datasets) * 100,
        "Not reported": (sex_counts.get("Not reported", 0) / total_datasets) * 100,
    }


# Função para calcular total de abordagens ômicas por repositório:
def omics_approach_count(df: pd.DataFrame) -> int:
    """
    Count the distinct omics approaches recorded in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the cataloged datasets.

    Returns
    -------
    int
        Number of unique values in the Omics_Approach column.
    """
    return df["Omics_Approach"].nunique()


# Função para definir métricas iniciais das espécies:
def get_species_profile(df: pd.DataFrame) -> dict:
    """
    Assemble the main summary metrics for a species.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the datasets cataloged for a species.

    Returns
    -------
    dict
        Dictionary containing the dataset count, distinct sampled tissues,
        sex distribution, and number of distinct omics approaches.
    """
    return {
        "dataset_count": dataset_count(df),
        "Sampled tissue": tissue_count(df),
        "Sex distribution": sex_distribution(df),
        "Omics approach": omics_approach_count(df),
    }


# Função para normalização dos dados:


def normalize_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize selected column types while preserving original values.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the cataloged datasets.

    Returns
    -------
    pd.DataFrame
        Copy of the input DataFrame with selected columns represented
        as pandas string types, preserving categories such as
        'Not reported' and numeric values stored as text.
    """
    df = df.copy()

    columns_to_preserve = [
        "Biological_Individuals_Count",
        "N_BioSamples",
        "Local_Server_Path",
    ]

    for column in columns_to_preserve:
        df[column] = df[column].astype("string")

    return df


def filter_datasets(df: pd.DataFrame, **filters) -> pd.DataFrame:
    """
    Filter datasets using one or more column criteria.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the datasets to filter.
    **filters
        Column names and filter values. A scalar value selects exact
        matches; a list, tuple, or set selects rows matching any of
        the provided values. Criteria with a value of None are ignored.

    Returns
    -------
    pd.DataFrame
        Copy of the input DataFrame containing rows that satisfy all
        active filter criteria.
    """
    filtered_df = df.copy()

    for column, value in filters.items():
        if value is None:
            continue

        if isinstance(value, (list, tuple, set)):
            filtered_df = filtered_df[filtered_df[column].isin(value)]
        else:
            filtered_df = filtered_df[filtered_df[column] == value]

    return filtered_df


def count_by_category(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Count records for each category in a selected column.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the records to analyze.
    column : str
        Name of the column to aggregate.

    Returns
    -------
    pd.DataFrame
        DataFrame containing each category and its record count.
        Actual missing values are excluded, while "Not reported"
        is preserved as a valid category.
    """
    counts = (
        df[column]
        .value_counts(dropna=True)
        .rename_axis(column)
        .reset_index(name="count")
    )

    return counts


def normalize_text_category(series: pd.Series) -> pd.Series:
    """
    Normalize whitespace in a categorical pandas Series.

    Converts values to pandas string dtype, removes leading and
    trailing whitespace, and replaces consecutive whitespace
    characters with a single space. Missing values remain missing.
    Strings containing only whitespace become empty strings.

    Parameters
    ----------
    series : pd.Series
        Series containing categorical text values.

    Returns
    -------
    pd.Series
        Series with normalized whitespace and pandas string dtype.
    """

    return series.astype("string").str.strip().str.replace(r"\s+", " ", regex=True)


def normalize_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize whitespace in selected categorical columns.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the cataloged datasets.

    Returns
    -------
    pd.DataFrame
        Copy of the input DataFrame with normalized categorical values.
        Missing values and explicit categories such as "Not reported"
        and "n/a" remain distinct.
    """
    normalized_df = df.copy()

    categorical_columns = [
        "Species",
        "Sampled_Tissue",
        "Sex",
        "Omics_Approach",
        "Platform",
        "Raw_Data_Availability",
        "Processed_Data_Availability",
        "Molecular_Biotype",
    ]

    for column in categorical_columns:
        if column in normalized_df.columns:
            normalized_df[column] = normalize_text_category(normalized_df[column])
            normalized_df[column] = normalized_df[column].replace("", pd.NA)

    return normalized_df
