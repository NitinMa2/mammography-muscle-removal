# mammography-muscle-removal

Final Year Project aimed to detect and remove the pectoral muscle region from mammography images.

# Getting Started

## Prerequisites

-   [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (preferred) or [Anaconda](https://www.anaconda.com/products/individual)

## Setup

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

## Activating the Environment

You will always need to ensure you are working on the right environment. To activate the environment, run:

```bash
conda activate fyp_env
```

## Updating the Environment

If there are changes to the environment, you will need to update the YAML file. To update the contents of your `environment.yml` file, run the following command:

```bash
conda env update --name fyp_env --file environment.yml --prune
```

# Contributing Guidelines

All python code should exist in a Jupyter Notebook. When contributing to this repository, follow these practices:

1. Activate the environment.
2. Create your feature branch (`git checkout -b feature/your-amazing-feature`).
3. Commit your changes (`git commit -am 'adding my amazing feature'`).
4. Push to the branch (`git push origin feature/your-amazing-feature`).
5. Open a Pull Request on GitHub or merge your code into `main` and then push it.

_Note: Please do not work directly on the `main` branch._
