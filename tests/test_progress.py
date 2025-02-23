import unittest
from unittest.mock import patch
from io import StringIO
from typing import Generator
from tinyprogress import progress  # Ensure the module name is correct

class TestProgressFunction(unittest.TestCase):
    
    def test_progress_list(self):
        """Tests the progress bar with a list."""
        test_list = [1, 2, 3, 4, 5]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = list(progress(test_list, total=len(test_list)))
            self.assertEqual(result, test_list)
            output = mock_stdout.getvalue().splitlines()[-1]  # Get the last line
            self.assertIn("100%", output)
            self.assertEqual(output.count("█"), 40)
    
    def test_progress_range(self):
        """Tests with range, which has a defined length."""
        test_range = range(10)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = list(progress(test_range))
            self.assertEqual(result, list(test_range))
            output = mock_stdout.getvalue().splitlines()[-1]
            self.assertIn("100%", output)

    def test_progress_generator(self):
        """Tests with a generator, where `total` must be specified."""
        def gen():
            for i in range(5):
                yield i
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = list(progress(gen(), total=5))
            self.assertEqual(result, list(range(5)))
            output = mock_stdout.getvalue().splitlines()[-1]
            self.assertIn("100%", output)
            self.assertEqual(output.count("█"), 40)
    
    def test_progress_custom_chars(self):
        """Tests with custom characters for the progress bar."""
        test_list = [1, 2, 3]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            list(progress(test_list, total=3, fill_char='-', empty_char='.'))
            output_lines = mock_stdout.getvalue().splitlines()
            last_output = output_lines[-1]  # Get the last line
            self.assertIn("100%", last_output)
            self.assertIn("-", last_output)
            
            # Check if at least one of the intermediate progress updates contains the empty character
            intermediate_bars = [line.split("[")[1].split("]")[0] for line in output_lines if "[" in line and "]" in line]
            self.assertTrue(any("." in bar for bar in intermediate_bars), "Empty character '.' was not found in any intermediate progress bars")
    
    def test_progress_with_task_name(self):
        """Tests with a task name included."""
        test_list = [1, 2, 3, 4]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            list(progress(test_list, total=4, task_name="Loading"))
            output = mock_stdout.getvalue().splitlines()[-1]
            self.assertIn("Loading", output)
    
    def test_progress_large_input(self):
        """Tests progress bar with a large input to ensure performance and stability."""
        large_list = list(range(10000))
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = list(progress(large_list, total=len(large_list)))
            self.assertEqual(result, large_list)
            output = mock_stdout.getvalue().splitlines()[-1]
            self.assertIn("100%", output)
    
    def test_progress_small_bar_length(self):
        """Tests with a very short bar length."""
        test_list = [1, 2, 3, 4, 5]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            list(progress(test_list, total=len(test_list), bar_length=10))
            output = mock_stdout.getvalue().splitlines()[-1]
            self.assertIn("100%", output)
            self.assertLessEqual(output.count("█"), 10)
    
    def test_progress_error_no_total_for_generator(self):
        """Tests that an error is raised when `total` is not provided for a generator."""
        def gen():
            for i in range(3):
                yield i
        
        with self.assertRaises(ValueError) as context:
            list(progress(gen()))
        self.assertIn("Total iterations must be specified", str(context.exception))

if __name__ == '__main__':
    unittest.main()
