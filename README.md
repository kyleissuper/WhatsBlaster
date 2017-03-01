# Automatically send WhatsApp messages

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

## Mass-messaging

I personally use `pandas` to iterate through a spreadsheet when notifying >60 club members about student events. But it's just as easy to accomplish a message blast like this:

```python
from WhatsBlaster import WhatsBlaster

names = [
    "Mickey Mouse",
    "Minnie Mouse",
    "Donald Duck",
    "Daisy Duck",
    "Goofy",
    "Pluto",
    "Boo Boo Chicken"
]

W = WhatsBlaster()
for name in names:
    print W.send_message(
        name,           # exact WhatsApp contact name
        "Hello!"        # message to send
        )               # returns success/failure message
W.close()
```

## Can I run this in the background?

Logging in requires you to manually scan the QR code with your WhatsApp mobile app, but after that, the script can be left to run on its own :)
