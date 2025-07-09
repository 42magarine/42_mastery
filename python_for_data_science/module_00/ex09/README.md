# ft_package

This is a simple Python package that provides one function:
- `count_in_list(lst, item)` – counts how often `item` appears in `lst`.

## Example

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## Build & Install Instructions

1. **Install build tool:**

   ```bash
   pip install build
   ```

2. **Build the package:**

   From the project root (where `pyproject.toml` is located):

   ```bash
   python -m build
   ```

   This creates a `dist/` folder with `.whl` and `.tar.gz` files.

3. **Install the package locally:**

   ```bash
   pip install ./dist/ft_package-0.0.1.tar.gz
   pip install ./dist/ft_package-0.0.1-py3-none-any.whl
   ```

4. **Verify installation:**

   ```bash
   pip list
   pip show -v ft_package
   ```
