from src.decorators import log


def test_log_decorator_with_tmp_path(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3

    log_content = log_file.read_text(encoding='utf-8')

    assert "my_function ok" in log_content
