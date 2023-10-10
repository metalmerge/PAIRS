# PULSAR - Pulsar Image Recognition System

## Introduction

PULSAR is an advanced Image Recognition System powered by Artificial Intelligence, designed for the detection and analysis of pulsar candidates. This project aims to add another filter to the identification of pulsars in astronomical data by leveraging machine learning models.

## Getting Started

To get started with PULSAR, follow these steps:

1. **API Key Setup:**
   - Export your Roboflow API key as an environment variable:

     ```bash
     export ROBOFLOW_API_KEY="YOUR_API_KEY"
     ```

2. **Data Credits:**
   - Special thanks to Wenke Xia and NANOstars for providing the pulsar data used in this project. You can access the roboflow model [here](https://universe.roboflow.com/feresearchproject/updated-pulsar-database).

3. **Installation:**
   - Clone this repository to your local machine:

     ```bash
     git clone https://github.com/your-username/pulsar-recognition.git
     cd pulsar-recognition
     ```

4. **Run the Code:**
   - Execute the Python script to perform pulsar candidate detection and analysis.

## Usage

The PULSAR project can be customized and extended for various use cases. Here are some common tasks you can perform:

- **Data Preparation:**
  - Ensure that your pulsar image data is organized in a folder structure that matches the expected format.
  - Prepare JSON files containing metadata and image URLs.

- **Configuration:**
  - Configure the ROBOFLOW_API_KEY environment variable with your Roboflow API key.

- **Training and Inference:**
  - Train and fine-tune the machine learning model using your own data if needed.
  - Perform inference on pulsar image candidates to classify and identify pulsars.

- **Data Analysis:**
  - Analyze the predictions and confidence scores to identify pulsars accurately.

- **Results:**
  - View and export the results, which include selected JSON objects with high-confidence pulsar predictions.

## Contributors

- Project Lead: Dimitry Ermakov
- Data Source: Wenke Xia/NANOstars

![NANOstars](NANOstars.png)

## Contact

If you have any questions or suggestions, please feel free to contact me:

- [Email](ermakovd06@gmail.com)
- [GitHub](https://github.com/metalmerge)
