import pytest

if __name__ == '__main__':
   # 遇到错误重跑两次一共跑了三次
   pytest.main(['-vs', './1_Main_Notes/1_6_Chloe_Fail_test.py', '--reruns=2'])
