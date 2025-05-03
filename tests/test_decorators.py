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


def test_log_success_message_logged(caplog):
    @log()
    def add(x, y):
        return x + y

    with caplog.at_level("INFO"):
        result = add(2, 3)

    assert result == 5
    assert "add ok" in caplog.text


def test_log_error_message_logged(caplog):
    @log()
    def divide(x, y):
        return x / y

    with caplog.at_level("ERROR"):
        try:
            divide(10, 0)
        except ZeroDivisionError:
            pass

    assert "divide error: ZeroDivisionError" in caplog.text
    assert "Inputs: (10, 0)" in caplog.text
