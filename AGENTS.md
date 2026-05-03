## Cursor Cloud specific instructions

This is a minimal Python repository with two standalone CLI scripts and no external dependencies beyond the Python standard library.

### Services

| Script | Description | Run command |
|--------|-------------|-------------|
| `main.py` | Interactive calculator (add, subtract, multiply, custom op) | `python3 main.py` |
| `salary.py` | Salary/payroll calculator | `python3 salary.py` |

Both scripts are interactive (read from stdin). For non-interactive testing, pipe input:
```
printf '5\n3\n1\n5\n3\n0\n' | python3 main.py
printf 'Alice\n40\n25\n' | python3 salary.py
```

### Lint / Check

- **Lint:** `ruff check .`
- **Compile check:** `python3 -m py_compile main.py && python3 -m py_compile salary.py`

### Testing

No test suite exists yet. Use `pytest` if tests are added. For now, validate scripts via piped stdin as shown above.

### Notes

- No `requirements.txt` — there are zero third-party dependencies.
- The update script installs `ruff` (linter) and `pytest` (test runner) as dev tools.
- Scripts use Korean-language prompts/output (UTF-8).
