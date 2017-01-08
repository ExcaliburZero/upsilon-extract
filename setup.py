from setuptools import find_packages, setup

setup(
    name='upsilonextract',
    version='0.1',
    description='',
    platforms=['any'],
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=['numpy>=1.9', 'scikit-learn>=0.18.1', 'scipy>=0.15',
        #'pyfftw>=0.9.2',
    ],
    keywords=['astronomy', 'periodic variables', 'light curves',
        'variability features', 'time-series survey'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    entry_points={
        'console_scripts': [
            'upsilon-extract = upsilonextract:main'
        ]
    }
)
