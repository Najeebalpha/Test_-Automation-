README


# Amazon E-commerce Checkout Test Automation

This repository contains an automated test script to verify the checkout functionality on an e-commerce website. The test navigates to Amazon, searches for a product, adds it to the cart, and proceeds to checkout. The script is built with Python, Selenium, Pytest, WebDriverManager, and includes Allure for test reporting.

## Folder Structure

amazon_test_automation/ │ ├── pages/ # Page Object Models for modular test structure │ ├── home_page.py │ ├── product_page.py │ └── cart_page.py │ ├── tests/ │ └── test_ecommerce_checkout.py # Main test script for checkout functionality │ ├── requirements.txt # Dependency file for installing all requirements └── README.md

bash


## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd amazon_test_automation
2. Set Up a Virtual Environment
It is recommended to install dependencies within a virtual environment to keep them isolated.


# Create a virtual environment
# On Windows
python -m venv test_automation

# On macOS/Linux
python3 -m venv test_automation
3. Activate the Virtual Environment

bash
# On Windows
test_automation\Scripts\activate

# On macOS/Linux
source venv/bin/activate
4. Install Dependencies


Once the virtual environment is active, install the dependencies listed in requirements.txt:
pip install -r requirements.txt
5. Ensure Java is Installed (for Allure)

Allure requires Java. You can check if Java is installed with the command:
java -version
If you get an error, download and install Java from Oracle's website, and set the JAVA_HOME environment variable if necessary.

6. Set Up Allure Command-Line Tool
Download the Allure Command-Line tool:
Go to Allure releases and download the latest zip file.
Extract the zip file and add the bin folder to your system’s PATH.


To verify Allure is set up correctly, run:
allure --version
Running the Tests


Activate the virtual environment if it’s not already activated:
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate


Run the tests with Pytest and generate Allure reports:

pytest tests/test_ecommerce_checkout.py --alluredir=reports/
Viewing Allure Reports
To generate and view Allure reports:


# Serve the Allure report on a local server
allure serve reports/
