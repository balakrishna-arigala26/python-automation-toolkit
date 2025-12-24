from automation_toolkit.log_parser import parse_logs


def test_parse_logs_finds_matches(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("INFO started\nERROR failed\nINFO running\nERROR crashed")

    result = parse_logs(log_file, "ERROR")

    assert len(result) == 2
    assert "ERROR failed" in result
    assert "ERROR crashed" in result


def test_parse_logs_no_matches(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("INFO started\nINFO running")

    result = parse_logs(log_file, "ERROR")

    assert result == []


def test_parse_logs_empty_file(tmp_path):
    log_file = tmp_path / "empty.log"
    log_file.write_text("")

    result = parse_logs(log_file, "ERROR")

    assert result == []
