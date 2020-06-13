import pytest

from ..version import TestClass


@pytest.fixture(scope="module")
def test_class() -> TestClass:
    return TestClass()


class TestVersions:

    @pytest.mark.skip_if_dependency(version=1)
    def test_with_version_1(self, test_class):
        print(test_class.get_result())

    @pytest.mark.skip_if_dependency(version=2)
    def test_with_version_2(self, test_class):
        print(test_class.get_result())

    @pytest.mark.skip_if_dependency(version=3)
    def test_with_version_3(self, test_class):
        print(test_class.get_result())

    @pytest.mark.skip_if_dependency(version=4)
    def test_with_version_4(self, test_class):
        print(test_class.get_result())
