def bubble_sort(arr):
	"""In-place bubble sort; returns the sorted list."""
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True
		if not swapped:
			break
	return arr


def parse_input(s):
	"""Parse comma/space-separated tokens into numbers when possible."""
	import re
	parts = [p for p in re.split(r'[,\s]+', s.strip()) if p != '']
	out = []
	for p in parts:
		try:
			out.append(int(p))
		except ValueError:
			try:
				out.append(float(p))
			except ValueError:
				out.append(p)
	return out


if __name__ == '__main__':
	s = input('Enter numbers (space or comma separated): ')
	arr = parse_input(s)
	if not arr:
		print('No input received.')
	else:
		sorted_arr = bubble_sort(arr)
		print('Sorted:', ' '.join(map(str, sorted_arr)))