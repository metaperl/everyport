# every_port.py

Open up a small Flask program on every port.

# Why the hell would you want to do this?

What if you visited SomeDomainOfYours.com and it was not serving? Well, wouldnt it be nice to be able to say:

> I visited every port on my machine where a small flask program was running and never got a response.

Well now you can!!!

# Usage

Edit `min_port` and `max_port` in `build.py`.
Type `python build.py` to create `every_port.out`
Type `bash -x every_port.out` to run Flask on every port.
