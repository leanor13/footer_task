import pytest
from ex01 import print_pages, _validate_input, ERROR_MESSAGES, MAX_BOUNDARIES_AROUND, MAX_TOTAL_PAGES

class TestFooter:
	@staticmethod
	def assert_print_pages_output(current_page, total_pages, boundaries, around, expected_output, capsys):
		print_pages(current_page, total_pages, boundaries, around)
		captured = capsys.readouterr()
		actual_output = captured.out.strip()

		assert actual_output == expected_output
	
	@pytest.mark.happy_flow
	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, expected_output",
		[
			(4, 5, 1, 0, "1 ... 4 5"),
			(1, 5, 1, 0, "1 ... 5"),
			(2, 5, 1, 0, "1 2 ... 5"),
			(4, 10, 2, 2, "1 2 3 4 5 6 ... 9 10"),
			(5, 10, 1, 1, "1 ... 4 5 6 ... 10"),
			(1, 10, 10, 10, "1 2 3 4 5 6 7 8 9 10"),
			(5, 6, 2, 2, "1 2 3 4 5 6"),
		]
	)
	def test_print_pages_default_tests(self, current_page, total_pages, boundaries, around, expected_output, capsys):
		self.assert_print_pages_output(current_page, total_pages, boundaries, around, expected_output, capsys)

	@pytest.mark.happy_flow
	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, expected_output",
		[
			(5, 10, 100, 1, "1 2 3 4 5 6 7 8 9 10"),
			(5, 10, 0, 4, "1 2 3 4 5 6 7 8 9 ..."),
			(6, 10, 0, 4, "... 2 3 4 5 6 7 8 9 10"),
			(5, 10, 0, 0, "... 5 ..."),
			(1, 1, 0, 0, "1"),
            (1, 1, 1, 1, "1"),
            (1, 100, 1, 0, "1 ... 100"),
            (50, 100, 1, 1, "1 ... 49 50 51 ... 100"),
            (50, 100, 2, 2, "1 2 ... 48 49 50 51 52 ... 99 100"),
		]
	)
	def test_print_pages_corner_cases(self, current_page, total_pages, boundaries, around, expected_output, capsys):
		self.assert_print_pages_output(current_page, total_pages, boundaries, around, expected_output, capsys)

	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, expected_output",
		[
			(5, MAX_TOTAL_PAGES, 1, 2, f"1 ... 3 4 5 6 7 ... {MAX_TOTAL_PAGES}"),
			(5, 10, MAX_BOUNDARIES_AROUND, 2, "1 2 3 4 5 6 7 8 9 10"),
			(5, 10, 1, MAX_BOUNDARIES_AROUND, "1 2 3 4 5 6 7 8 9 10"),
		]
	)
	def test_print_pages_border_values(self, current_page, total_pages, boundaries, around, expected_output, capsys):
		self.assert_print_pages_output(current_page, total_pages, boundaries, around, expected_output, capsys)  

	@pytest.mark.error_handling
	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, error_message",
		[
			(1.4, 10, 1, 2, ERROR_MESSAGES["not_int"]),
			(5, "ten", 1, 2, ERROR_MESSAGES["not_int"]),
			(5, 10, "", 2, ERROR_MESSAGES["not_int"]),
			(5, 10, 1, None, ERROR_MESSAGES["not_int"]),
		]
	)
	def test_print_pages_not_int_values(self, current_page, total_pages, boundaries, around, error_message):
		with pytest.raises(ValueError, match=error_message):
			_validate_input(current_page, total_pages, boundaries, around)

	@pytest.mark.error_handling
	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, error_message",
		[
			(-1, 10, 1, 2, ERROR_MESSAGES["negative_value"]),
			(5, -10, 1, 2, ERROR_MESSAGES["negative_value"]),
			(5, 10, -1, 2, ERROR_MESSAGES["negative_value"]),
			(5, 10, 1, -2, ERROR_MESSAGES["negative_value"]),
		]
	)
	def test_print_pages_negative_values(self, current_page, total_pages, boundaries, around, error_message):
		with pytest.raises(ValueError, match=error_message):
			_validate_input(current_page, total_pages, boundaries, around)
	
	@pytest.mark.error_handling
	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, error_message",
		[
			(10, 9, 1, 2, ERROR_MESSAGES["current_outside_range"]),
			(10, 0, 1, 2, ERROR_MESSAGES["current_outside_range"]),
			(0, 10, 1, 2, ERROR_MESSAGES["current_outside_range"]),
   		]
	)
	def test_print_pages_outside_of_total(self, current_page, total_pages, boundaries, around, error_message):
		with pytest.raises(ValueError, match=error_message):
			_validate_input(current_page, total_pages, boundaries, around)

	@pytest.mark.error_handling
	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, error_message",
		[
			(5, MAX_TOTAL_PAGES + 1, 1, 2, ERROR_MESSAGES["maximum_total_exceeded"]),
			(5, 10, MAX_BOUNDARIES_AROUND + 1, 2, ERROR_MESSAGES["boundaries_around_exceeded"]),
			(5, 10, 1, MAX_BOUNDARIES_AROUND + 1, ERROR_MESSAGES["boundaries_around_exceeded"]),
   		]
	)
	def test_print_pages_outside_of_total(self, current_page, total_pages, boundaries, around, error_message):
		with pytest.raises(ValueError, match=error_message):
			_validate_input(current_page, total_pages, boundaries, around)
	
	# we test different cases for validation in tests above, this test is just to validate final exception output
	@pytest.mark.error_handling
	@pytest.mark.parametrize(
		"current_page, total_pages, boundaries, around, error_message",
		[
			(0, 0, -1, 0, "Validation error: " + ERROR_MESSAGES["negative_value"]),
			(10, 0, 1, 2, "Validation error: " + ERROR_MESSAGES["current_outside_range"].format(current_page = 10, total_pages = 0)),
			(5, MAX_TOTAL_PAGES + 1, 1, 2, "Validation error: " + ERROR_MESSAGES["maximum_total_exceeded"]),
			(5, 10, MAX_BOUNDARIES_AROUND + 1, 2, "Validation error: " + ERROR_MESSAGES["boundaries_around_exceeded"]),
			(5.5, 10, 6, 2, "Validation error: " + ERROR_MESSAGES["not_int"]),
		]
	)
	def test_print_pages_validation_errors(self, current_page, total_pages, boundaries, around, error_message, capsys):
		print_pages(current_page, total_pages, boundaries, around)
		captured = capsys.readouterr()
		assert captured.out.strip() == error_message