from src.db_connection import Engine


def test_engine_load_data(mocker):
    mocker.patch("src.db_connection.DBConnector.__init__", return_value=None)
    mocker.patch("src.db_connection.DBConnector.get", return_value="xyz")
    output = Engine().load_data()
    assert output == "xyzxxx"
