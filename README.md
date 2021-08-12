# mammography-muscle-removal

Final Year Project aimed to detect and remove the pectoral muscle region from mammography images.

# Getting Started

## Prerequisites

-   [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (preferred) or [Anaconda](https://www.anaconda.com/products/individual) (for MacOS)

## Setup

### For Windows Users

Follow these steps using the **Anaconda Prompt** to setup the project:

1. Clone this repository and cd into the project directory.
2. Create the project environment. To create an environment called `fyp_env` from `environment.yml`, you can run the command:

```bash
conda env create --file environment.yml --name fyp_env
```

The environment should now contain the following libraries:

-   Jupyter
-   Pandas
-   Numpy
-   Matplotlib
-   Seaborn
-   Scikit-image
-   OpenCV-Python

### For MacOS Users

Use conda through the **Terminal** and use the default Anaconda environment.

## Activating the Environment

You will always need to ensure you are working on the right environment. To activate the environment, run:

```bash
conda activate fyp_env
```

## Updating the Environment

To add/remove a library to the environment, refer to the following commands:

```bash
conda install package-name
conda remove package-name
```

Changes to the environment will need to be reflected in the YAML file. To update the contents of your `environment.yml` file, run the following command:

```bash
conda env export > environment.yml
```

If there are changes in the `environment.yml`, you will need to update your environment by running:

```bash
conda env update --name fyp_env --file environment.yml --prune
```

## Starting the Jupyter Notebook

To run the jupyter notebook on your localhost, run this command from the project folder after activating the environment:

```bash
jupyter notebook
```

# Contributing Guidelines

All python code should exist in a Jupyter Notebook. When contributing to this repository, follow these practices:

1. Activate the environment.
2. Update your local main.

```bash
git checkout main
git pull
```

3. Create your feature branch (`git checkout -b feature/your-amazing-feature`).
4. Add your changes (`git add .`).
5. Commit your changes (`git commit -m 'adding my amazing feature'`).
6. Push to the branch (`git push -u origin feature/your-amazing-feature`).
7. Request Nitin to merge your code. Please clearly specify the updates you have made.

_Note: Please do not work directly on the `main` branch._
