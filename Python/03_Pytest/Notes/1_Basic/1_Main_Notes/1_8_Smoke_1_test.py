import pytest


class TestLogin:

    def test_02(self):
        print('Test Chloe')

    def test_02_1(self):
        print('Test Chloe 1')

    @pytest.mark.usermanage
    def test_02_2(self):
        print('Test Chloe 2')

    @pytest.mark.smoke
    def test_02_3(self):
        print('Test Chloe 3')

    def test_02_4(self):
        print('Test Chloe 4')
