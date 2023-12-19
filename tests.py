from dataInputOutput import clearConsole

def test_clearConsole(mocker):
    # Create a fake system
    mocked_system = mocker.patch('os.system')

    clearConsole()

    # Check for execution of if/else 
    mocked_system.assert_called_once()
    mocked_system.assert_called_once_with(mocker.ANY)
    assert mocked_system.call_args[0][0] in {"clear", "clr"}