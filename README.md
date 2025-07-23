# 🪙 Live Coin Counter

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://your-app-url.streamlit.app/](https://live-coin-counter-app-unrqfwu6xyj6xezahn7kwt.streamlit.app/))

This repository contains the source code for a real-time coin detection and value calculation web application. It leverages a custom-trained Roboflow computer vision model to identify U.S. coins from a live camera feed and displays a running total of their value, all within a user-friendly Streamlit interface.

---

## Table of Contents
- [Demo](#demo)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation and Usage](#installation-and-usage)
- [Deployment](#deployment)
- [License](#license)

---

## Demo
A short GIF or screenshot showcasing the application in action.

*(Replace this text and the line below with a screenshot or GIF of your app)*
![App Demo](placeholder.gif)

---

## Key Features
- **Live Object Detection:** Employs a computer vision model to identify pennies, nickels, dimes, and quarters in real-time.
- **Dynamic Value Calculation:** Instantly computes and displays the total monetary value of the detected coins.
- **Interactive Web Interface:** Built with Streamlit for a responsive and intuitive user experience on both desktop and mobile.

---

## Tech Stack
- **Language:** Python 3.9+
- **Framework:** Streamlit
- **Computer Vision:** OpenCV, Roboflow
- **Core Libraries:** NumPy, Pydantic

---

## Installation and Usage
To set up and run this project locally, follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and Activate a Virtual Environment**
    This isolates the project's dependencies from your system's Python installation.
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Secrets**
    Create a `.streamlit` directory and a `secrets.toml` file within it.
    ```
    .
    ├── .streamlit/
    │   └── secrets.toml
    ├── app.py
    └── ...
    ```
    Add your Roboflow credentials to `secrets.toml`:
    ```toml
    ROBOFLOW_API_KEY = "YOUR_API_KEY_HERE"
    ROBOFLOW_PROJECT = "coin_recognition-0vii0"
    ROBOFLOW_VERSION = 1
    ```

5.  **Run the Application**
    ```bash
    streamlit run app.py
    ```
    Open your web browser and navigate to the local URL provided by Streamlit.

---

## Deployment
This application is configured for deployment on Streamlit Community Cloud. After pushing your code to a GitHub repository (ensuring `.streamlit/` is in your `.gitignore`), you can deploy by:
1.  Connecting your GitHub account to Streamlit Cloud.
2.  Selecting the repository and branch.
3.  Adding your project secrets to the Streamlit Cloud dashboard under the app's advanced settings.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
