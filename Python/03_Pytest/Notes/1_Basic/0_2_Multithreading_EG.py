import pytest

if __name__ == '__main__':
    # 若没有-n则15秒多因为有time.sleep(3)
    # pytest.main(['-vs', './1_Main_Notes'])
    pytest.main(['-vs', './1_Main_Notes/1_2_Chloe_test.py::TestLogin', '-n=4'])
