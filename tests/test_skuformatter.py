import pytest
from sku_formatter import sku_formatter

def test_format_skus_strips_leading_zeros():
    assert sku_formatter.format_skus(["00123456","001234567"]) == ["123456","1234567"]

def test_format_skus_dedupes():
    assert sku_formatter.format_skus(["987654321", "123456789", "987654321", "1234567891"]) == ["987654321", "123456789", "1234567891"]

def test_format_skus_avoids_all_zero_input():
    assert sku_formatter.format_skus(["000000","00000000000"]) == []

def test_format_skus_avoids_empty_input():
    assert sku_formatter.format_skus([]) == []

@pytest.fixture(scope="session")
def input_file(tmp_path_factory):
    directory = tmp_path_factory.mktemp("directory")
    file = directory / "input.txt"
    file.write_text("21341234 040124109491 000102341234 asdfsf241234   !!! 2134234 21341234")
    return file

def test_extract_skus(input_file):
    assert sku_formatter.extract_skus(input_file) == ["21341234", "040124109491", "000102341234", "241234", "2134234", "21341234"]

@pytest.fixture(scope="session")
def write_skus_input_file(tmp_path_factory):
    directory = tmp_path_factory.mktemp("directory")
    write_skus_input = directory / "write_skus_input.txt"
    return write_skus_input

def test_write_skus(write_skus_input_file):
    sku_formatter.write_skus(["21341234", "40124109491", "102341234", "241234", "2134234"], write_skus_input_file) 
    assert write_skus_input_file.read_text() == f"'21341234',\n'40124109491',\n'102341234',\n'241234',\n'2134234'"