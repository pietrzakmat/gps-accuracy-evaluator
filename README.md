# GPS Accuracy Evaluator

It is a software which helps to evaluate and present the data for accuracy of the GPS sensor.

## Description

The example analyis is based on blog article: [rtklibexplorer](https://rtklibexplorer.wordpress.com/2016/12/29/exploring-moving-base-solutions/)

It shows a use case two receivers (Rx1 and Rx2) fixed on the moving platform, later called rovers. In this scenario they are placed 15cm apart on a straight rail. The idea is to find the difference between calclualted rovers positions and verify how much it differs from 15cm fixed distance. In this way we can define accuracy of GPS receivers.

The data are a prori aquired as described in aformentioned blog [rtklibexplorer](https://rtklibexplorer.wordpress.com/2016/12/29/exploring-moving-base-solutions/) and extracted from receivers cards using [rtklib](https://rtklib.com/).
Instead relying on rktlib plotting software the Python script is proposed in this repository. Additionally it runs some statistics to evaluate error from desired 15cm distance between sensors. It cleans the output from rtklib and loads pythons pandas dataframes and produces plots out of them.


## Getting Started

### Dependencies

1. Python 3 or higher
2. pip install pandas
3. Required numpy 1.24 >= <= 2.0, i.e. 
   pip install --force-reinstall numpy==1.24
4. python3 -m pip install -U matplotlib
5. pip install colored
6. pip install pyproj
 
### Installing

git clone https://github.com/pietrzakmat/gps-accuracy-evaluator
or 
git clone git@github.com:pietrzakmat/gps-accuracy-evaluator.git

### Executing program

* Navigate to cloned directory
* Run
```
./src/test.py
```

## Authors

Contributors names and contact info

Mateusz Pietrzak [@mail](mat.pietrzak@gmail.com)


## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* [gps_utils](https://gist.github.com/MikeK4y/1d99b93f806e7d535021b15afd5bb04f)
Copyright (c) 2019 Michail Kalaitzakis
