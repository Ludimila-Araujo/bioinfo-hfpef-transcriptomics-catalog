import pandas as pd


# Função para contar o número de espécies catalogadas
def count_all_species(df_species):
    return len(df_species)


# Função para contar o número total de respositórios catalogados
def sum_all_repositories(df_species):
    total_repo = 0
    for df in df_species.values():
        species_repositories = len(df)
        total_repo += species_repositories

    return total_repo


# Função para contar quantidade de datasets por espécie:
def dataset_count(df):
    return len(df["Dataset_ID"])


# Função para contar quantidade de tecidos estudados por repositório:
def tissue_count(df):
    return df["Sampled_Tissue"].nunique()


# Função para calcular o percentual de datasets segundo categoria de sexo registrada
def sex_distribution(df):

    sex_counts = df["Sex"].value_counts()

    total_datasets = len(df)

    return {
        "Female": (sex_counts.get("Female", 0) / total_datasets) * 100,
        "Male": (sex_counts.get("Male", 0) / total_datasets) * 100,
        "Male / female": (sex_counts.get("Male / female", 0) / total_datasets) * 100,
        "Not reported": (sex_counts.get("Not reported", 0) / total_datasets) * 100,
    }


# Função para calcular total de abordagens ômicas por repositório:
def omics_approach_count(df):
    return df["Omics_Approach"].nunique()


# Função para definir métricas iniciais das espécies:
def get_species_profile(df):

    return {
        "dataset_count": dataset_count(df),
        "Sampled tissue": tissue_count(df),
        "Sex distribution": sex_distribution(df),
        "Omics approach": omics_approach_count(df),
    }


# Função para normalização dos dados:
def normalize_data_types(df):
    df = df.copy()

    df["Biological_Individuals_Count"] = pd.to_numeric(
        df["Biological_Individuals_Count"], errors="coerce"
    ).astype("Int64")

    df["N_BioSamples"] = pd.to_numeric(df["N_BioSamples"], errors="coerce").astype(
        "Int64"
    )

    df["Local_Server_Path"] = df["Local_Server_Path"].astype("string")

    return df
