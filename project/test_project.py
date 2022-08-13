from project import check_name, check_num, search_food
from unittest.mock import patch




def main():
    test_check_name()
    test_check_num()
    test_search_food()
   



def test_check_name():
    with patch('builtins.input', lambda *args: 'apple'):
         assert check_name() == 'Apple'
    with patch('builtins.input', lambda *args: 'APPLE'):
        assert check_name() == 'Apple'
 
def test_check_num():
    with patch('builtins.input', lambda *args: '50'):
         assert check_num() == 50
    with patch('builtins.input', lambda *args: '100'):
        assert check_num() == 100  




def test_search_food():
    assert search_food("apple") == {'calories' : 53.0, 'protein' : 0.3, 'fat': 0.2}
    assert search_food("ple") == None
    assert search_food("") == None


    

if __name__ == "__main__":
    main()