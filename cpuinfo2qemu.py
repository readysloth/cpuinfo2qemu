import sys
import argparse
import subprocess as sp


def get_flags_from_cpuinfo(lines):
    flags = []
    for line in lines:
        if 'flags' in line:
            flags_list = line.split(':')[-1]
            flags += flags_list.split()
    return flags


def read_cpuinfo():
    with open('/proc/cpuinfo', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        first_blank_line = lines.index('')
        return lines[:first_blank_line]


def get_flags_from_qemu(qemu):
    proc = sp.Popen([qemu, '-cpu', 'help'], stdout=sp.PIPE)
    lines = [l.decode().strip() for l in proc.stdout.readlines()]
    cpuid_line = lines.index('Recognized CPUID flags:')
    flags = []
    for line in lines[cpuid_line+1:]:
        flags += line.split()
    return flags


parser = argparse.ArgumentParser()
parser.add_argument('qemu',
                    nargs='?',
                    default='qemu-system-x86_64',
                    help='qemu executable, e.g. qemu-system-x86_64')
parser.add_argument('-d', '--debug', action='store_true', help='debug output')
args = parser.parse_args()

cpu_supported_flags = get_flags_from_cpuinfo(read_cpuinfo())
qemu_supported_flags = get_flags_from_qemu(args.qemu)

mutually_supported = set(qemu_supported_flags).intersection(cpu_supported_flags)

if args.debug:
    print('CPU supported:\n', ' '.join(cpu_supported_flags), file=sys.stderr)
    print('QEMU supported:\n', ' '.join(qemu_supported_flags), file=sys.stderr)
    print('Mutually supported:\n', ' '.join(mutually_supported), file=sys.stderr)
print('+' + ',+'.join(mutually_supported))
