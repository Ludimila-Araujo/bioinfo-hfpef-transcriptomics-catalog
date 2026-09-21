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

    total_female = (sex_counts.get("Female", 0) / total_datasets) * 100
    total_male = (sex_counts.get("Male", 0) / total_datasets) * 100
    total_female_male = (sex_counts.get("Male / female", 0) / total_datasets) * 100

    return total_female, total_male, total_female_male


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
