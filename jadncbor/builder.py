import base64
import cbor2


def convert_cbor_to_json(data, encoding='hex'):
    """P
    Convert CBOR data to JSON format.
    
    Args:
        data (bytes): The CBOR data to convert.
        
    Returns:
        dict: The converted JSON data.
    """
    if data is None or data == "":
        return {}
    
    try:
        cbor_data = None
        if encoding == 'hex':
            cbor_data = bytes.fromhex(data)
        elif encoding == 'base64':
            cbor_data = base64.b64decode(data)
        else:
            raise ValueError("Unsupported encoding type. Use 'hex' or 'base64'.")

        return cbor2.loads(cbor_data)
    except Exception as e:
        return f"Invalid Data: {e}"
