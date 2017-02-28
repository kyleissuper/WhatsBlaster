## Automatically send WhatsApp messages

```python
from WhatsBlaster import WhatsBlaster

W = WhatsBlaster()
print W.send_message("Mickey Mouse", "Hello!")
W.close()
```

Requires selenium (`pip install selenium`), and driver may need some configuration. Tested and works on MacOS with Google Chrome.
