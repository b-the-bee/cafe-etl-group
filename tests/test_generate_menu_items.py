from src.generate_menu_items import generate_menu

def test_generate_menu():
    dummy_data = [
        [1, "Chocolate", 2.30],
        [2, "Baked Beans", 1.85],
        [3, "Tea", 0.80],
        [4, "Tea", 0.80]
    ]
    
    expected = [
        ["P000", "Chocolate", 2.3],
        ["P001", "Baked Beans", 1.85],
        ["P002", "Tea", 0.8]
    ]
    
    result = generate_menu(dummy_data)[0]
    assert result == expected