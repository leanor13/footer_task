# Pagination Footer Generator

This Python module provides a simple and efficient way to generate pagination footers for websites or applications.

## Table of Contents

- [Preconditions](#preconditions)
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Tests](#tests)
- [Contributing](#contributing)

## Preconditions

Before running the code or tests, ensure you have the following installed:

- Python 3
- pytest

## Introduction

The Pagination Footer Generator allows you to create pagination footers for navigating through multiple pages of content. It takes into account the current page, the total number of pages, and the desired boundaries and around parameters to determine which pages to display and where to place ellipses (...) for hidden pages.

Assumptions made: only non-negative integer values are allowed as input, current page should be within range between 1 and total pages (inclusive), 
maximum number of total pages and boundaries is limited, limiting constants can be modified if required.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/pagination-footer.git
    ```

2. Navigate to the directory:

    ```bash
    cd pagination-footer
    ```

3. Use the `print_pages` function in your Python scripts or applications.

## Usage

Import the `print_pages` function into your Python script or module where you want to use it:

```python
from ex01 import print_pages
```

Generate a pagination footer by calling the print_pages function:

for example:
```python
print_pages(current_page=4, total_pages=10, boundaries=2, around=2)
```

This will output: 
```python
1 2 3 4 5 6 ... 9 10
```

## Error Handling

Ensure that you handle any `ValueError` exceptions that may be raised if the input parameters are invalid. These exceptions will contain descriptive error messages to guide you in correcting the input.

## Tests

To run the unit tests, use the following command:

```bash
pytest test_ex01.py
```

You can run specific test scenarios using pytest markers. Here are the available markers:

- `happy_flow`: Tests that verify the main happy path scenarios
- `error_handling`: Tests that verify error handling scenarios

To run tests with a specific marker, use the following command:

```bash
pytest -m <marker_name>
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.