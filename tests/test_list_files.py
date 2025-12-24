from automation_toolkit.list_files import list_files


def test_list_files_returns_files(tmp_path):
    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"

    file1.write_text("1")
    file2.write_text("2")

    result = list_files(tmp_path)

    assert len(result) == 2
    assert file1 in result
    assert file2 in result


def test_list_files_empty_dir(tmp_path):
    result = list_files(tmp_path)
    assert result == []


def test_list_files_extension_filter(tmp_path):
    txt_file = tmp_path / "a.txt"
    log_file = tmp_path / "b.log"

    txt_file.write_text("1")
    log_file.write_text("2")

    result = list_files(tmp_path, extension=".txt")

    assert result == [txt_file]
