def read_file(filename: str) -> str:
    """Read and return the contents of `filename`.

    Uses `with open(...)` for safe file handling and explicit try/except
    to provide clearer error messages.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")
    except PermissionError:
        raise PermissionError(f"Permission denied when opening: {filename}")
    except Exception as e:
        raise RuntimeError(f"Error reading file {filename}: {e}") from e


if __name__ == '__main__':
    import sys
    # Choose filename from argv if provided, otherwise try a sensible default
    filename = sys.argv[1] if len(sys.argv) > 1 else 'Text 2.txt'
    try:
        content = read_file(filename)
        print(f"Read {len(content)} bytes from '{filename}':\n")
        print(content)
    except Exception as err:
        print(f"Failed to read '{filename}': {err}")
