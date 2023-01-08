# cpuinfo2qemu

Small script that transforms `/proc/cpuinfo` output to qemu `-cpu` flags

```
usage: cpuinfo2qemu.py [-h] [-f FILE] [-d] [qemu]

positional arguments:
  qemu                  qemu executable, e.g. qemu-system-x86_64

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  use file instead of /proc/cpuinfo
  -d, --debug           debug output
```
