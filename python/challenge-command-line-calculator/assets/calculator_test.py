import subprocess
import sys

sys.path.append('/home/labex/project')

def test_addition():
    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '-a', '1', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '1 + 2 = 3'

    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '--add', '10', '20'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '10 + 20 = 30'

def test_subtraction():
    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '-s', '10', '5'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '10 - 5 = 5'

    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '--subtract', '20', '10'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '20 - 10 = 10'

def test_multiplication():
    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '-m', '10', '5'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '10 * 5 = 50'

    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '--multiply', '20', '10'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '20 * 10 = 200'

def test_division():
    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '-d', '10', '5'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '10 / 5 = 2.0'

    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '--divide', '20', '10'], stdout=subprocess.PIPE)
    assert result.stdout.decode().strip() == '20 / 10 = 2.0'

def test_invalid_option():
    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '--invalid'], stderr=subprocess.PIPE)
    assert 'unrecognized arguments: --invalid' in result.stderr.decode().strip()

def test_insufficient_arguments():
    result = subprocess.run(['python3', '/home/labex/project/calculator.py', '-a'], stderr=subprocess.PIPE)
    assert 'argument -a/--add: expected 2 arguments' in result.stderr.decode().strip()

if __name__ == '__main__':
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_invalid_option()
    test_insufficient_arguments()
    print('All tests passed!')