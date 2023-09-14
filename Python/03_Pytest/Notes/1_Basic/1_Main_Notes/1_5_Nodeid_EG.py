import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '1_2_Chloe_test.py::test_04'])
    # 需要加一个类名
    pytest.main(['-vs', '1_2_Chloe_test.py::TestLogin::test_02'])
