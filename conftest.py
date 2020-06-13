import pytest

from .version import is_version_skipped


@pytest.fixture(autouse=True)
def skip_if_dependency(request):
    dependency_marker = request.node.get_closest_marker("skip_if_dependency")
    if dependency_marker:
        version = dependency_marker.kwargs.get("version", None)

        if is_version_skipped(version):
            pytest.skip(f"Test is run with version {version} which is not supported by test.")
