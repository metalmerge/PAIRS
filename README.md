# PULSAR - Pulsar Image Recognition System

## Introduction

PULSAR is an advanced Image Recognition System powered by Artificial Intelligence, designed for the detection and analysis of pulsar candidates. This project aims to add another filter to the identification of pulsars in astronomical data by leveraging machine learning models.

## Getting Started

To get started with PULSAR, follow these steps:

1. **API Key Setup:**
   - Export your Roboflow API key as an environment variable. Getting an API key is done by deploying this roboflow model: <https://app.roboflow.com/pulsarfinderthroughimageclassification/pulsarfinderimageclassification/deploy/2>

     ```bash
     export ROBOFLOW_API_KEY="YOUR_API_KEY"
     ```

2. **Installation:**
   - Clone this repository to your local machine:

     ```bash
     git clone https://github.com/metalmerge/PULSAR.git
     cd PULSAR
     ```

3. **Run the Code:**
   - Execute predict_unchecked_JSON.py to run the pulsar candiate model predictor. A JSON file will be returned with all the selected pulsar candidates.
  
    ```bash
     python3 predict_unchecked_JSON.py
     ```

## Usage

The JSON_to_images folder is used for converting checked JSON to images to use for training data.
JSON_input is for the unchecked or checked input JSON data
JSON_output is for the output of JSON files.
known_JSON_Pulsar_Data is for the two folders of known pulsar candidates and RFI

## Contributors

- Project Lead: Dimitry Ermakov
- Data Source: NANOstars (Wenke Xia)

## Acknowledgments

Special thanks to NANOstars for their willingness in providing the pulsar data and to Wenke Xia for the additional help with procuring the data.

![NANOstars](images/NANOstars.png)

## Contact

If you have any questions or suggestions, please feel free to contact me:

- [Email](ermakovd06@gmail.com)
- [GitHub](https://github.com/metalmerge)
