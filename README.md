## Automatically send WhatsApp messages

```python
from WhatsBlaster import WhatsBlaster

W = WhatsBlaster()
print W.send_message(
    "Mickey Mouse", # exact WhatsApp contact name
    "Hello!"        # message to send
    )               # returns success/failure message
W.close()
```

Requires selenium (`pip install selenium`), and driver may need some configuration. Tested and works on MacOS with Google Chrome.
