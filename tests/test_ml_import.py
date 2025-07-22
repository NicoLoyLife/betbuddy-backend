def test_ml_import():
    import numpy
    import sklearn

    assert numpy.__version__
    assert sklearn.__version__
