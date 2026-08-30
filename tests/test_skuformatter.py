import pytest
from sku_formatter import sku_formatter

def test_format_skus():
    with pytest.raises(ValueError):
        sku_formatter.format_skus({"001123123", "132231", "abc"})