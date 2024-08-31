import program_5
 
def test_app():
    input_values = [100, 50, 25, 0]
    output = []
 
    def mock_input(s):
        output.append(s)
        return input_values.pop(0)
    program_5.input = mock_input
    program_5.print = lambda s : output.append(s)
 
    program_5.main()
    print(output)
    correct_balance_found = False
    for item in output:
        if "25" in item:
            correct_balance_found = True

    assert correct_balance_found == True