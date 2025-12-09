import pytest

#lista de archivos de prueba
test_files = [
    "test/test_login.py", "test/test-navigate.py", "test/test-cart.py", "test/test_inventory.py"
]

pytest_args = test_files + ["--html=report.html","-v"]

pytest.main(pytest_args)
