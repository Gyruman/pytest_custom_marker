class TestClass:

    @staticmethod
    def get_result():
        return "TestClass"


def is_version_skipped(version: int) -> bool:
    if version < 4:
        return True
    return False
