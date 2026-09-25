# IT Operations Analysis Tool

## Overview

The IT Operations Analysis Tool is a Python-based project that analyzes basic IT spending and operational issues and converts the results into a structured management report. The project was created to apply basic-level Python programming in a practical business problem. The goal is to demonstrate how basic programming and data analysis can be used to organize operational information and identify areas that may require management attention.

## Business Problem

Small organizations may have IT spending and support information spread across different categories, making it difficult to quickly identify spending patterns and recurring operational issues.

This project takes a structured text file containing company details, IT spending, and IT issues data and automatically produces an analysis report containing:

- IT spending calculations
- Spending percentages
- Cost per employee
- Highest individual software and hardware expenses
- IT issues frequency
- Issue priority classifications
- Spending observations
- Management flags

## How It Works

The project follows a simple process:

1. Read the business data from a text file.
2. Organize the information into categories.
3. Calculate financial and operational metrics.
4. Compare spending categories and issue frequencies.
5. Apply predefined analytical rules.
6. Generate a text-based management report.

## Technologies Used

- Python
- File input/output
- Lists
- Loops
- Conditional statements
- Basic error handling
- String operations
- Arithmetic calculations

## Project Structure

```text
IT-Operations-Analysis-Tool/
│
├── README.md
├── main.py
├── business_data.txt
└── analysis_report.txt
