# Expense Manager

A simple Python based Expense Manager designed to help users record, manage, and analyse their expenses.

The application provides basic expense tracking and summary features. It was developed as a practical Python project to apply fundamental programming concepts such as functions, lists, loops, conditional statements, user input, and data processing.

## Features

The Expense Manager allows users to:

* Add new expenses
* Enter the date of the expense
* Assign a category to each expense
* Enter the expense amount in USD
* View recorded expenses
* Calculate total expenses
* Identify the minimum expense
* Identify the maximum expense
* Calculate the average expense
* Delete expenses
* Display an expense summary

## Expense Information

Each expense contains the following information:

| Field      | Description                        |
| ---------- | ---------------------------------- |
| Expense ID | Unique identifier for the expense  |
| Date       | Date on which the expense was made |
| Category   | Category assigned to the expense   |
| Amount     | Expense amount in USD              |

### Date Format

The application expects the date to be entered in the following format:

```text
DD/MM/YY
```

Example:

```text
22/09/26
```

## Technologies Used

* Python
* Functions
* Lists
* Loops
* Conditional statements
* User input
* Built in Python functions
* Basic data processing

## How to Run

### Run the Python File

Make sure Python is installed on your computer.

Run the following command from the project directory:

```bash
python expense_manager.py
```

### Run the Windows Executable

A Windows executable version is also provided.

Open:

```text
expense_manager.exe
```

The executable can be run without having Python installed.

## Example

The application can display an expense summary such as:

```text
Here is the summary of the expenses:

Exp_ID     Date       Category       Expense
---------------------------------------------
1          01/09/26   Rent           $1250
2          02/09/26   Insurance      $30
3          03/09/26   Transport      $65
4          05/09/26   Leisure        $30
5          07/09/26   Grocery        $75
6          15/09/26   Leisure        $44
```

The application can then calculate:

* Total expenses
* Highest expense
* Lowest expense
* Average expense

## Current Limitations

The current version has the following known limitations.

### 1. Duplicate Minimum and Maximum Expenses

If two or more expenses have the same minimum or maximum amount, the current version does not display all matching expenses correctly.

For example:

```text
Insurance    $30
Leisure      $30
```

Both expenses have the same minimum amount.

However, the current version displays only the **first matching expense in the list** instead of displaying all expenses with the minimum amount.

The same limitation applies when multiple expenses have the same maximum amount.

This functionality is planned for a future version.

### 2. Date Format Validation

The application expects the date to be entered in `DD/MM/YY` format.

If the user enters an incorrect date format, the current version may result in a program error.

For example, entering an invalid format instead of:

```text
22/09/26
```

may cause the program to terminate unexpectedly.

Improved date validation and user friendly error handling will be added in a future version.

## Future Improvements

The following improvements are planned for future versions:

* Correctly display all expenses with the same minimum amount
* Correctly display all expenses with the same maximum amount
* Add date format validation
* Handle invalid user input without terminating the program
* Add the ability to edit expenses
* Add expense search and filtering
* Add expense sorting
* Add permanent data storage
* Add monthly expense analysis
* Add category based spending analysis
* Add budget tracking
* Improve the overall user interface

## Project Purpose

This project was created as a practical Python learning project.

It focuses on applying Python fundamentals to a real world expense tracking application while gradually introducing more advanced concepts and functionality.

The project will be improved progressively as new Python concepts are learned.

## Author

**Kalpesh Baviskar**

Python learning project focused on developing practical programming and data processing skills.
