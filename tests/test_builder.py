from jadncbor.builder import convert_cbor_to_json

def test_convert_cbor_hex_to_json():
    hex_data = "b900016361616163616161"
    data = convert_cbor_to_json(hex_data)
    assert data == {"aaa": "aaa"}

def test_convert_cbor_base64_to_json():
    base64_data = "uQABY2FhYWNhYWE="
    data = convert_cbor_to_json(base64_data, encoding='base64')
    assert data == {"aaa": "aaa"}

def test_convert_cbor_hex_to_invalid():
    hex_data = "b900016361616163616161"
    data = convert_cbor_to_json(hex_data, encoding='zzz')
    assert data != {"aaa": "aaa"}

def test_convert_invalid_cbor_hex_to_json():
    hex_data = "b900016361616163616161"
    data = convert_cbor_to_json(hex_data)
    assert data != {"aaa": "zzz"}
    
def test_convert_empty_cbor_hex_to_json():
    hex_data = ""
    data = convert_cbor_to_json(hex_data)
    assert data == {}    
    
def test_convert_none_cbor_hex_to_json():
    hex_data = None
    data = convert_cbor_to_json(hex_data)
    assert data == {}