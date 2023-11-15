# file-sharing
This is simple python-flask based web application for file sharing. Share files on the server via browser. 

# Preparation

## Environment

- Developer IDE
- Anaconda 
- Python 
- FLASK (rest api)

## Developer IDE

Visual Studio code is used as developer IDE and it comes with huge plugin ecosystem to work with various programming languages (is a personal choice for Python programming). A few to mention that are helpful in this solution context. 

- Python
- Python Extension Pack 
- Python Environment Manager 
- Jupyter 
- Intelli Code etc.

## Install Anaconda

1. Anaconda is a popular distribution of the Python programming language that provides a comprehensive ecosystem for data science, machine learning, and scientific computing, including a powerful package manager and extensive libraries.

2. Anaconda simplifies the process of setting up and managing Python environments, making it easier to work with different Python versions, manage dependencies, and create reproducible data analytics solutions, making it a preferred choice for many Python developers and data scientists.


[Download-Link](https://www.anaconda.com/products/distribution) 

## Check if installation is successful 

### From Terminal run below command 

```commandline
(base) naga ~ % conda -V
conda 22.11.1
```

## Install required libraries

Below also installs required python version and creates a python environment named `file-sharing` 

```commandline
cd <<project-home-director>>
```

```commandline
conda env create -f environment.yml
```

Switch to python environment `file-sharing`  

```commandline
conda activate file-sharing
```

# Run the application 

Since file-sharing environment is activated, the app can be run with below command.

```commandline
python ./app.py
```