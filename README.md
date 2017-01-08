# UPSILoN Extract
UPSILoN Extract is a Python script for extracting information from (time, magnitude, error) light curve data. It was created from the functionality built into the [UPSILoN](https://github.com/dwkim78/py3-UPSILoN) periodic variable star classifier ([Kim & Bailer-Jones 2015](https://arxiv.org/abs/1512.01611)).

All of the extraction functionality is directly from the UPSILoN classifier. UPSILoN Extract includes only the needed modules so that users do not have to download the Random Forest classifier included in the UPSILoN library. Additionally, UPSILoN Extract gives a command line tool `upsilon-extract` for batch processing light curve data files.

## Usage
```
$ upsilon-extract ~/Documents/smc/OGLE-SMC-RRLYR- ".dat" 4 1 2 > output.dat
0001
0002
$ cat output.dat
0001	0.222105266231	0.168940812264	2.35350124662	0.711495042227	-0.706604217476	654	0.558817465271	126.155970809	-72.6342860101	9.37487384865e-05	0.344141984626	0.430623638191	1.06856914681	2.28453779004	0.3225	0.456557492082	0.309140970985	0.984962463379	-0.149973531529	-0.0599727535122	0.0421956525987	0.773791293693	19.0023237696	0.205908079655
0002	0.137918745451	0.134565757297	2.3456030004	0.935545830991	-0.455123603177	645	0.594781360714	115.005462335	-64.2267065839	0.000106218547561	0.24627817273	0.683383802924	1.1766264556	-0.159475344256	0.215	0.474068384018	0.344516869683	0.990370690823	0.188820654255	-0.0653176913294	0.0570889600839	0.803583677383	19.0047431589	0.137336005957
```

### Command Structure
```
upsilon-extract FILE_PREFIX FILE_SUFFIX DIGIT_PADDING START END
```

### Installation
To install UPSILoN Extract from the GitHub repository, run the following commands:

```
$ git clone https://github.com/ExcaliburZero/upsilon-extract.git
$ cd upsilon-extract
$ python setup.py install
```

## Licensing
All of the code in the `extract_features` folder is from the UPSILoN library, licensed under the MIT License by Dae-Won Kim. See the [UPSILoN library history](https://github.com/dwkim78/py3-upsilon/commits/2c3e1da134014bf75fd672044f03f3b650045b10) for more attribution information.

The remainer of UPSILoN is also licensed under the MIT License.
