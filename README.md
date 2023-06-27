PyAutoIt
========

Python binding for AutoItX3.dll with native Autoit naming scheme

### Installing

If you have pip on your system, you can simply install or upgrade PyAutoIt:

```python
pip install -U git+https://github.com/Tophness/pyautoit
```

Alternately, you can download the source distribution from PyPI, unarchive it, and run:

```python
python setup.py install
```

### Example

- open notepad
- type some string into notepad, eg: **"hello world"**
- close notepad without saving

```python
import autoit

autoit.Run("notepad.exe")
autoit.WinWaitActive("[CLASS:Notepad]", "", 3)
autoit.ControlSend("[CLASS:Notepad]", "", "Edit1", "hello world{!}")
autoit.WinClose("[CLASS:Notepad]")
autoit.ControlClick("[Class:#32770]", "", "Button2")
```
