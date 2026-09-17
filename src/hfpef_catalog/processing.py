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
