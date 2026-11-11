# Shopping Cart – CI and Automated Testing

## Project Description

This project calculates and displays the total price of items in a shopping cart using Python.

## Continuous Integration

GitHub Actions is used to automatically check the code whenever changes are pushed to the repository.

The CI workflow includes:

- **Static Analysis:** Pylint checks the `shopping_cart.py` file for code quality and coding standard issues.
- **Automated Testing:** Python's built-in `unittest` framework runs the automated tests in `test_shopping_cart.py`.

## Running the Checks Locally

Install Pylint:

```bash
pip install pylint
```

Run static analysis:

```bash
pylint shopping_cart.py
```

Run automated tests:

```bash
python -m unittest discover -s . -p "test_*.py"
```

## Project Files

- `shopping_cart.py` – Shopping cart calculation and display functions.
- `test_shopping_cart.py` – Automated unit tests.
- `.github/workflows/ci.yml` – GitHub Actions CI configuration.

   
