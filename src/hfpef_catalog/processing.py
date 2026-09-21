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


# Função para definir métricas iniciais das espécies:
def get_species_overview(df):

    overview_columns = df[
        [
            "Dataset_ID",
            "Sampled_Tissue",
            "Strain / Ethnicity",
            "Sex",
            "N_BioSamples",
            "Condition: {n}",
        ]
    ]

    overview_dict = overview_columns.loc[0].to_dict()

    return {
        "Dataset ID": overview_dict["Dataset_ID"],
        "Sampled tissue": overview_dict["Sampled_Tissue"],
        "Strain / ethnicity": overview_dict["Strain / Ethnicity"],
        "Sex": overview_dict["Sex"],
        "Biosamples": overview_dict["N_BioSamples"],
        "Conditions": overview_dict["Condition: {n}"],
    }
