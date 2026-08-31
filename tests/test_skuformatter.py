import pytest
from sku_formatter import sku_formatter

def test_format_skus_strips_leading_zeros():
    assert sku_formatter.format_skus(["00123456","001234567"]) == ["123456","1234567"]

def test_format_skus_dedupes():
    pass