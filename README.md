# Contact Manager

## Project Description

This project is a simple command-line contact management application written in Python. It allows users to add, find, and delete contacts. Exception handling is used to prevent common errors from crashing the application.

## Project Files

* `buggy_contacts.py` — Original starter program.
* `contact_manager.py` — Corrected contact management application.
* `test_contact_manager.py` — Unit tests for the application.
* `README.md` — Project documentation.

## Bugs Fixed

1. Added input validation to handle letters or other invalid menu input.
2. Handled missing contacts when searching or deleting.
3. Created a custom `DuplicateContactError` exception.
4. Prevented duplicate contact names from being added.
5. Added unit tests using Python's `unittest` framework.

## Requirements

Python 3 is required. No external packages are needed.

## How to Run the Program

Open a terminal in the project directory and run:

```bash
python contact_manager.py
```

## How to Run the Tests

Run the following command:

```bash
python -m unittest test_contact_manager.py
```

The tests cover adding a contact, finding existing and missing contacts, deleting existing and missing contacts, and handling duplicate contacts.

## Screencast

Screencast video link: [Add your video link here after recording]

## Conclusion

This project demonstrates exception handling, custom exceptions, input validation, modular programming, and automated testing with Python.
