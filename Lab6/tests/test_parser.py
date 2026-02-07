from parser import parse_product_basic, parse_availability



def test_parse_product_basic_extracts_id(valid_product):

    # Arrange - Set up test data
    # Act - Call the function
    id_extract = parse_product_basic(valid_product) 
    
    # Assert - Check the result
    assert "id" in id_extract




def test_parse_product_basic_extracts_name(valid_product):
    
    name_extract = parse_product_basic(valid_product)

    assert "name" in name_extract




def test_parse_product_basic_returns_only_id_and_name(valid_product):

    allowed_keys = {"id","name"}
    
    name_id_extract = parse_product_basic(valid_product) 

    assert set(name_id_extract.keys()) == allowed_keys







def test_parse_availability_when_in_stock(valid_product):

    result = parse_availability(valid_product)

    assert result is True




def test_parse_availability_when_out_of_stock(product_out_of_stock):

    result = parse_availability(product_out_of_stock)

    assert result is False


def test_parse_availability_when_field_missing(minimal_product):

    result = parse_availability(minimal_product)

    assert result is False

