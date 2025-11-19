def linear_search(lst, target):
	"""
	Return the index of the first occurrence of `target` in `lst`.
	If not found, return -1.
	"""
	for i, v in enumerate(lst):
		if v == target:
			return i
	return -1


def _parse_list_input(s):
	"""Parse a user input string into a list of values.

	Splits on commas or whitespace. Each token is converted to int if
	possible, otherwise to float if possible, otherwise left as string.
	"""
	import re
	parts = re.split(r"[,\s]+", s.strip())
	parts = [p for p in parts if p != ""]
	out = []
	for p in parts:
		try:
			out.append(int(p))
			continue
		except ValueError:
			pass
		try:
			out.append(float(p))
			continue
		except ValueError:
			out.append(p)
	return out


def _parse_single(s):
	s = s.strip()
	try:
		return int(s)
	except ValueError:
		pass
	try:
		return float(s)
	except ValueError:
		return s


def _interactive():
	s = input("Enter list elements (space or comma separated): ")
	lst = _parse_list_input(s)
	t = _parse_single(input("Enter target value: "))
	idx = linear_search(lst, t)
	if idx >= 0:
		print(f"Found at index: {idx}")
	else:
		print("Not found")


if __name__ == "__main__":
	_interactive()

