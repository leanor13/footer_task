HIDDEN_PAGES_SIGN = "..."
MAX_TOTAL_PAGES = 100000
MAX_BOUNDARIES_AROUND = 100

ERROR_MESSAGES = {
	"negative_value": "Invalid input: negative parameters are not allowed",
	"current_outside_range": "Invalid input: current page = {current_page} is not in range from 1 to {total_pages}",
	"maximum_total_exceeded": f"Invalid input: total pages cannot exceed {MAX_TOTAL_PAGES}",
	"boundaries_around_exceeded": f"Invalid input: boundaries and around cannot exceed {MAX_BOUNDARIES_AROUND}",
	"not_int": "Invalid input: only integer values allowed",
}

def print_pages(current_page, total_pages, boundaries, around):
	''' Validate input, form pages to print, print pages list '''
	
	try:
		_validate_input(current_page, total_pages, boundaries, around)
	except ValueError as e:
		print(f"Validation error: {e}")
		return
	
	pages = _form_pages_list(current_page, total_pages, boundaries, around)
	printable = _prepare_printable_output(pages, total_pages)
	print(printable)
	return printable

def _validate_input(current_page, total_pages, boundaries, around):
	''' Validations: parameter types and values, current page should belong to range '''
	
	if not all(isinstance(arg, int) for arg in [current_page, total_pages, boundaries, around]):
		raise ValueError(ERROR_MESSAGES["not_int"])
	
	if min(current_page, total_pages, boundaries, around) < 0:
		raise ValueError(ERROR_MESSAGES["negative_value"])
	
	if current_page not in range(1, total_pages + 1):
		raise ValueError(ERROR_MESSAGES["current_outside_range"].format(current_page=current_page, 
																		total_pages=total_pages))
	
	if total_pages > MAX_TOTAL_PAGES:
		raise ValueError(ERROR_MESSAGES["maximum_total_exceeded"])
	
	if max(boundaries, around) > MAX_BOUNDARIES_AROUND:
		raise ValueError(ERROR_MESSAGES["boundaries_around_exceeded"])

def _form_pages_list(current_page, total_pages, boundaries, around):
	''' Create sorted list of pages to display with no duplicates '''
	
	pages = set()
	# left part of the list starts from page 1 and ends at boundaries or total_pages - whatever is first
	start_left = 1
	end_left = min(boundaries, total_pages)
	pages.update(range(start_left, end_left + 1))
	
	# middle part of the list starts is between current_page -/+ around, but can't start before 1 or finish after total
	start_middle = max(1, current_page - around)
	end_middle = min(current_page + around, total_pages)
	pages.update(range(start_middle, end_middle + 1))
	
	# right side of the list ends at total_pages and starts at (total_pages - boundaries + 1) or 1 - whatever is first
	start_right = max(1, total_pages - boundaries + 1)
	end_right = total_pages
	pages.update(range(start_right, end_right + 1))
	
	return sorted(pages)

def _prepare_printable_output(pages_list, total_pages):
	''' Convert int values to str and fill page gaps with (...) '''
	
	output = []
	first_page = pages_list[0]
	last_page = pages_list[-1]
	
	# if page 1 is not printed, start output with (...)
	if first_page != 1:
		output.append(HIDDEN_PAGES_SIGN)
	
	output.append(str(first_page))
	
	# identify all gaps in page numbering and replace with (...)
	for current_index in range(1, len(pages_list)):
		previous_page = pages_list[current_index - 1]
		current_page = pages_list[current_index]
		
		if current_page != previous_page + 1:
			output.append(HIDDEN_PAGES_SIGN)
		
		output.append(str(current_page))
	
	# if last page is not printed, add final (...)
	if last_page != total_pages:
		output.append(HIDDEN_PAGES_SIGN)
	
	return " ".join(output)
