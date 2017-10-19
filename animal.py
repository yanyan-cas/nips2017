if __name__ == '__main__':
    import os

    from multiprocessing import cpu_count

    from src.animal.generate_dgm_provider import generate_dgm_provider
    from src.animal.experiments import experiment

    data_path = os.path.join(os.getcwd(), 'data/dgm_provider/npht_animal_corrected_32dirs.h5')
    if not os.path.isfile(data_path):
        print('Persistence diagram provider does not exists, creating ... (this may need some time)')
        n_cores = max(1, cpu_count() - 1)
        generate_dgm_provider('./data/raw_data/animal_corrected',
                              data_path,
                              32,
                              n_cores=n_cores)
    else:
        print('Found persistence diagram provider!')

    print('Starting experiment...')
    experiment(data_path)

