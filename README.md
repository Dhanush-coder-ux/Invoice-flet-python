![Screenshot 2024-12-08 115250](https://github.com/user-attachments/assets/6a08a03d-a0b0-4046-94a9-bd8678a296a0)

Invoice Generator Application

Project Description

The Invoice Generator Application is a Python-based tool that allows users to create professional invoices with ease. The application uses the Flet framework for its graphical user interface (GUI) and the ReportLab library to generate PDF invoices. This project is designed for small businesses and individuals who need a simple and efficient way to generate invoices.

Features

User-friendly graphical interface.

Ability to input billing information, including company name, address, state, and city.

Option to add multiple items with details such as name, quantity, and unit price.

Automatic calculation of total item prices.

PDF generation of invoices with professional formatting.

Dynamic and responsive UI with gradient backgrounds and easy navigation.

Technologies Used

Python: Core programming language.

Flet: Framework for building the graphical user interface.

ReportLab: Library for generating PDF files.

datetime: Python's built-in module for timestamping invoices.

Installation and Setup

Prerequisites

Python 3.8 or higher installed on your system.

Required Python packages:

flet

reportlab

Steps

Clone the repository or download the source code.

git clone <repository_url>
cd invoice-generator

Install the dependencies using pip:

pip install flet reportlab

Run the application:

python app.py

How to Use

Open the application by running python app.py.

Fill out the billing information:

Name

Company Name

Address

State

City

Add items by providing:

Item Name

Quantity

Unit Price

Click Submit to save billing details.

Click the + button to add items.

Once all details are entered, click Generate Invoice to create a PDF file.

The generated PDF file will be saved in the application’s directory with a timestamp in its filename.

Code Explanation

1. generate_pdf

Uses ReportLab to create a PDF document.

Takes the filename, billing information, and a list of items as input.

Formats the invoice with professional headers and calculates total prices.

2. main

Built using Flet to create an interactive GUI.

Includes fields for billing information and item details.

Provides buttons for submitting data and generating invoices.

Displays dynamic feedback with snack bars.

3. Event Handlers

add_to_form: Saves billing information and provides user feedback.

add_item: Adds item details to a list after validation.

generate_invoice: Validates inputs and calls generate_pdf to create the invoice.

Future Enhancements

Add support for multiple pages in PDF for large invoices.

Include tax calculations and discounts.

Allow saving invoices to a specified directory.

Implement a database to store and retrieve invoices.

Contributing

Feel free to fork the repository and submit pull requests for improvements or additional features.



