# README.md for "ICP NNS Governance System Explorer: Action NNS Function"

## Introduction

Welcome to the "Internet Computer Protocol (ICP) Network Nervous System (NNS) Governance System Explorer" GitHub repository. This project utilizes an interactive application built using Dash and Dashtools to explore governance data of the Internet Computer protocol. The dataset used for this application can be found on [Kaggle](https://www.kaggle.com/datasets/sunshineluyaozhang/icp-nns-proposals).

## How to Use This Repository

### Creating Dash Apps and Deploying to the Cloud Using Dashtools

This repository provides a framework for creating and deploying Dash applications. Here's a quick guide to get started:

1. **Setting Up the Environment**:
   - Create a virtual environment:
     ```
     python -m venv myenv
     ```
   - Activate the virtual environment:
     ```
     source myenv/bin/activate
     ```
   - Upgrade pip and install necessary packages:
     ```
     pip install --upgrade pip
     pip install dash plotly pandas
     ```

2. **Using Dash Tools**:
   - Install dash-tools and a compatible version of click:
     ```
     pip install dash-tools
     pip install "click<8.1.3"
     ```
   - Use dashtools to create the GUI:
     ```
     dashtools gui
     ```
   - Freeze the requirements for future deployments:
     ```
     pip freeze > requirements.txt
     ```
   - For more information on dashtools, visit the [PyPI dash-tools page](https://pypi.org/project/dash-tools/).

### Featured Dash Application: ICP NNS Governance System Dashboard

This repository focuses on a Dash application that visualizes the distribution of proposal NNS functions in the ICP NNS Governance System. The application is structured as follows:

- **Data Loading**: The dataset is loaded from a provided CSV URL.
- **Dash App Initialization**: A Dash app is initialized.
- **Plot Creation**: A bar plot is created using Plotly Express with a logarithmic scale on the y-axis.
- **App Layout**: The layout includes a header, a paragraph with notes, a dropdown for status selection, and a graph for data display.
- **Callback Function**: A callback function updates the bar plot based on the selected proposal status.
- **Running the App**: The application is executed with `app.run_server(debug=True)`.

The source code for this application is available in this repository. Users can explore and modify the code to suit their analytical needs.
# icp-nns-explorer-functions
# icp-nns-explorer-functions
