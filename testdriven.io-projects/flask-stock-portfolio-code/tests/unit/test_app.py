"""
This file contains unit tests for app.py file
"""
import pytest
from app import StockModel
from pydantic import ValidationError

def test_validate_stock_data_nominal():
    """
    GIVEN a helper class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    stock_data = StockModel(
        stock_symbol='SBUX',
        number_of_shares='100',
        purchase_price='45.67'
    )
    assert stock_data.stock_symbol == 'SBUX'
    assert stock_data.number_of_shares == 100
    assert stock_data.purchase_price == 45.67

def test_validate_stock_data_invalid_stock_symbol():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data(invalid stock symbol) is passed in
    THEN check that the validation raises a ValueError
    """
    with pytest.raises(ValueError):
        StockModel(
            stock_symbol='SBUX123', #invalid stock symbol
            number_of_shares='100',
            purchase_price='45.67'
        )

def test_validate_stock_data_invalid_number_of_shares():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data(invalid number of shares) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        StockModel(
            stock_symbol='SBUX',
            number_of_shares='100.1231', #invalid number of shares
            purchase_price='45.67'
        )

def test_validate_stock_data_invalid_purchase_price():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data(invalid purchase price) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        StockModel(
            stock_symbol='SBUX',
            number_of_shares='100',
            purchase_price='45,67' #invalid purchase price
        )

def test_validate_stock_data_invalid_stock_symbol_and_number_of_shares():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data(invalid stock symbol and number of shares) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        StockModel(
            stock_symbol='SBUX123', #invalid stock symbol
            number_of_shares='100.1231', #invalid number of shares
            purchase_price='45.67'
        )#This test cases was automatically created by the Github Copilot

def test_validate_stock_data_missing_inputs():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data(missing inputs) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        StockModel() #Missing Inputs

def test_validate_stock_data_missing_purchase_price():
    """
    GIVEN a helper class to validate the form data
    WHEN invalid data(missing purchase price) is passed in
    THEN check that the validation raises a ValidationError
    """
    with pytest.raises(ValidationError):
        StockModel(
            stock_symbol='SBUX',
            number_of_shares='100'
        ) #Missing purchase price