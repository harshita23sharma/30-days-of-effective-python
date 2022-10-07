from src.dataset import process_data


def test_process_data(mocker):
    # Mock where it ("load_data") is used, and not where it’s defined (source)
    mocker.patch("src.dataset.load_data", return_value={"key1": "valy", "key2": "val2"})
    assert process_data() == "valy"
