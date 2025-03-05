![GitHub License](https://img.shields.io/github/license/croketillo/tinyprogress)
![GitHub file size in bytes](https://img.shields.io/github/size/croketillo/tinyprogress/tinyprogress/tinyprogress.py)
![PyPI - Version](https://img.shields.io/pypi/v/tinyprogress)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tinyprogress)
![Pepy Total Downloads](https://img.shields.io/pepy/dt/tinyprogress)

# TinyProgress

**TinyProgress** is a minimal and lightweight progress bar module for Python. It provides an easy way to track progress in loops and iterables without requiring external dependencies.

![Barra de progreso](images/barra.gif)

## 🚀 Features
- ✅ Simple and lightweight (no external dependencies)
- ✅ Customizable progress bar length and characters
- ✅ Supports named tasks
- ✅ Works with any iterable

## 📦 Installation
Since TinyProgress is a single-file module, you can simply copy `tinyprogress.py` into your project.

Alternatively, install it via pip (once published to PyPI):
```sh
pip install tinyprogress
```

## 🛠 Usage
### Basic Progress Bar
```python
from tinyprogress import progress
import time

for i in progress(range(100)):
    time.sleep(0.05)  # Simulating work
```

### Custom Progress Bar Length
```python
for i in progress(range(100), bar_length=50):
    time.sleep(0.05)
```

### Named Task Progress Bar
```python
for i in progress(range(100), task_name="Downloading"):
    time.sleep(0.05)
```

### Using Custom Characters
```python
for i in progress(range(100), fill_char='#', empty_char='-'):
    time.sleep(0.05)
```
### Using Custom Colors
```python
def bar_color(progress: float) -> str:
    if progress < 0.7:  # 70%
        return '\033[31m'
    return '\033[32m'

def text_color(progress: float) -> str:
    return '\033[35m'


for i in progress(
    range(100),
    task_name='Colored bar',
    fill_char='—',
    start_char=' ',
    end_char=' ',
    bar_color=bar_color,
    text_color=text_color
):
    time.sleep(0.05)
```

## 📜 License
GNU General Public License v3, see LICENSE file.