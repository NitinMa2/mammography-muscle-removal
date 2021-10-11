# mammography-muscle-removal

Final Year Project aimed to detect and remove the pectoral muscle region from mammography images.

# Getting Started

## Prerequisites

-   [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (preferred) or [Anaconda](https://www.anaconda.com/products/individual) (for MacOS)
-   [Node.js](https://nodejs.org/en/download/)

## Jupyter Setup

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
-             Pydicom
-   Requests

### For MacOS Users

Use conda through the **Terminal** and use the default Anaconda environment.

## Activating the Python Environment

You will always need to ensure you are working on the right environment. To activate the environment, run:

```bash
conda activate fyp_env
```

## Updating the Python Environment

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

## Segmentation API Documentation

Only Valid API method is POST and only valid endpoint is Segment
This Post Method with segment endpoint takes in a base64 encoded image in string format and gives a json response with the segmented image in base64 encoded string.

A valid API call example will look like

```
{api_url}/segment/{base64_string}
```

with response

```
{"Segmented" : "base_64_image_string"}
```

## Web App Setup

The web app lives in the `web-app` directory. We need to first install the node dependencies.

```bash
cd web-app
npm install
```

In order to be able to connect with the MongoDB instance, you will need to add the uri to a `web-app/.env` file. Add the content of the `.env` file:

```
VUE_APP_MONGO_URI=<your_uri>
```

## Starting the Web App in localhost

To start the client and server in localhost from the `web-app` directory, run:

```bash
npm run dev
```

You can then access the app through http://localhost:8080 .

## REST API Setup

The REST API lives in the `rest-api` directory. We need to configure the python environment to run the API. There is a `rest-api/requirements.txt` file that contains all the dpenedencies exclusively for the API but using the `fyp_env` should also work (if not, please alert Nitin).

### Running the API Locally

Running `main.py` will allow access to the API at http://127.0.0.1:5000 . This can be achieved by executing:

```bash
python main.py
```

## REST API Usage

POST requests can made to the `/segment` endpoint. The API expects a JSON body containing the `base64Image` attribute which is used as the input to the region growing segmentation algorithm.

### Sample Request URL

```bash
http://127.0.0.1:5000/segment
```

### Sample Request Body

```bash
{
    "base64Image": "asdaGVsbG8="
}
```

### Sample Response

```bash
{
    "segmentedImage" : "asdaGVsbG8="
}
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
