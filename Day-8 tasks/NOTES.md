# Day 8 Notes - pip vs uv

## What is pip?

pip is Python's default package manager.
It is used to install, update, and manage Python packages.

### Steps using pip

1. Create a virtual environment

```bash
python -m venv myenv
```

2. Activate the environment

```bash
myenv\Scripts\activate
```

3. Install a package

```bash
pip install requests
```

4. Generate requirements.txt

```bash
pip freeze > requirements.txt
```

---

## What is uv?

uv is a modern Python package manager and virtual environment tool.
It is designed to be much faster than pip.

### Steps using uv

1. Create a virtual environment

```bash
python -m uv venv
```

2. Activate the environment

```bash
.venv\Scripts\activate
```

3. Install a package

```bash
python -m uv pip install requests
```

4. Generate requirements.txt

```bash
python -m uv pip freeze > requirements.txt
```

---

## Comparison

| Feature              | pip      | uv       |
| -------------------- | -------- | -------- |
| Comes with Python    | Yes      | No       |
| Installation Speed   | Slower   | Faster   |
| Environment Creation | Standard | Faster   |
| Learning Curve       | Easy     | Easy     |
| Modern Tooling       | Basic    | Advanced |

---

## Conclusion

Both pip and uv can create isolated environments and install Python packages.
pip is the traditional and widely used tool,
while uv provides the same functionality with significantly better performance 
and faster package management.
