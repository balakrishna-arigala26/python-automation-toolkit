from automation_toolkit.system_monitor import get_system_usage


def test_get_system_usage_keys():
    result = get_system_usage()

    assert "cpu_percent" in result
    assert "memory_percent" in result
    assert "disk_percent" in result


def test_get_system_usage_values_are_numbers():
    result = get_system_usage()

    assert isinstance(result["cpu_percent"], (int, float))
    assert isinstance(result["memory_percent"], (int, float))
    assert isinstance(result["disk_percent"], (int, float))
