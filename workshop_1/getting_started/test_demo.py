import pytest
from unittest.mock import Mock, patch
from calculator import Calculator

@pytest.fixture
def setup():
    cal_obj = Calculator()
    yield cal_obj # Could keep doing further, opposite to return; which's stop.
    

def test_add(setup):
    # Creating an object
    # Testing it
    assert setup.add(2, 5) == 7

def test_checkprint(capsys, setup):
    setup.use_capsys_fixture()
    stdout = capsys.readouterr()
    assert "hello world!" in stdout.out 


def test_mock_obj_in(setup):
    def special_method(value):
        return value * 2
     

    mock_obj = Mock()
    mock_obj.fetch.side_effect = special_method

    assert setup.use_object(2, mock_obj) == 4
    assert setup.use_object(5, mock_obj) == 10

# Noted: should review this again, we wanna change everything we wanted
@patch('calculator.AnotherClass')
def test_use_external(mock_anotherclass,setup):
    anotherclass_obj = mock_anotherclass.return_value # Specify mock must ne return obj
    anotherclass_obj.some_method.return_value = 5

    # Whatever be sent, all retrun 5
    assert setup.use_external(10) == 5


def test_divide(setup):
    assert setup.divide(2, 2) == 1
    with pytest.raises(ValueError) as exc:
        setup.divide(1, 0)
    assert str(exc.value) == "Can't Divide by Zero"
