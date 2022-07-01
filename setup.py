from setuptools import setup

setup(
    name='MoleculeACE',
    version='2.0.0',
    packages=['MoleculeACE','MoleculeACE.benchmark',
                                'MoleculeACE.data_fetching',
                            'MoleculeACE.models',
                            'MoleculeACE.Data',
                                'MoleculeACE.Data.benchmark_data',
                                    'MoleculeACE.Data.benchmark_data.metadata',
                                    'MoleculeACE.Data.benchmark_data.raw',
                            'MoleculeACE.Data.configures',
                                'MoleculeACE.Data.configures.benchmark',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL4203_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL2034_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL233_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL4616_EC50',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL287_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL218_EC50',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL264_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL219_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL2835_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL2147_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL231_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL3979_EC50',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL237_EC50',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL244_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL4792_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL1871_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL237_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL262_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL2047_EC50',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL239_EC50',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL2971_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL204_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL214_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL1862_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL234_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL238_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL235_EC50',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL4005_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL236_Ki',
                                    'MoleculeACE.Data.configures.benchmark.CHEMBL228_Ki'
                                'MoleculeACE.Data.default',
                            'MoleculeACE.Data.results',
                            'MoleculeACE.Data.fetched_data',
                                'MoleculeACE.Data.fetched_data.data_curated',
                                'MoleculeACE.Data.fetched_data.data_final',
                                'MoleculeACE.Data.fetched_data.data_raw'
              ],
    url='https://github.com/molML/MoleculeACE',
    license='MIT',
    author='Derek van Tilborg',
    author_email='d.w.v.tilborg@tue.nl',
    description='MoleculeACE',
    install_requires=[
            'tqdm',
            'requests',
            'twine',
            'importlib-metadata',
            'pandas',
            'numpy',
            'chembl_webresource_client',
            'scikit-learn',
            'matplotlib',
            'python-Levenshtein',
            'rdkit-pypi',
            'transformers',
            'scikit-optimize'
        ],
    include_package_data=True,
    package_data={'': ['Data/*',
                       'Data/benchmark_data/*',
                       'Data/configures/*',
                       'Data/configures/default/*',
                       'Data/configures/benchmark/*',
                       'Data/configures/benchmark/CHEMBL4203_Ki/*',
                       'Data/configures/benchmark/CHEMBL2034_Ki/*',
                       'Data/configures/benchmark/CHEMBL233_Ki/*',
                       'Data/configures/benchmark/CHEMBL4616_EC50/*',
                       'Data/configures/benchmark/CHEMBL287_Ki/*',
                       'Data/configures/benchmark/CHEMBL218_EC50/*',
                       'Data/configures/benchmark/CHEMBL264_Ki/*',
                       'Data/configures/benchmark/CHEMBL219_Ki/*',
                       'Data/configures/benchmark/CHEMBL2835_Ki/*',
                       'Data/configures/benchmark/CHEMBL2147_Ki/*',
                       'Data/configures/benchmark/CHEMBL231_Ki/*',
                       'Data/configures/benchmark/CHEMBL3979_EC50/*',
                       'Data/configures/benchmark/CHEMBL237_EC50/*',
                       'Data/configures/benchmark/CHEMBL244_Ki/*',
                       'Data/configures/benchmark/CHEMBL4792_Ki/*',
                       'Data/configures/benchmark/CHEMBL1871_Ki/*',
                       'Data/configures/benchmark/CHEMBL237_Ki/*',
                       'Data/configures/benchmark/CHEMBL262_Ki/*',
                       'Data/configures/benchmark/CHEMBL2047_EC50/*',
                       'Data/configures/benchmark/CHEMBL239_EC50/*',
                       'Data/configures/benchmark/CHEMBL2971_Ki/*',
                       'Data/configures/benchmark/CHEMBL204_Ki/*',
                       'Data/configures/benchmark/CHEMBL214_Ki/*',
                       'Data/configures/benchmark/CHEMBL1862_Ki/*',
                       'Data/configures/benchmark/CHEMBL234_Ki/*',
                       'Data/configures/benchmark/CHEMBL238_Ki/*',
                       'Data/configures/benchmark/CHEMBL235_EC50/*',
                       'Data/configures/benchmark/CHEMBL4005_Ki/*',
                       'Data/configures/benchmark/CHEMBL236_Ki/*',
                       'Data/configures/benchmark/CHEMBL228_Ki/*'
                       ]}
)
