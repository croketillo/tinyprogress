from tinyprogress import progress
import time

print('\n\nSIMPLE BAR:')
for i in progress(range(100)):
    time.sleep(0.05)  # Simulating work

print('\nMODIFY BAR LENGTH:')
for i in progress(range(100), bar_length=53):
    time.sleep(0.05)

print('\nNAMED TASK BAR:')
for i in progress(range(100), task_name="Downloading:"):
    time.sleep(0.05)

print('\nCUSTOM CHARS:')
for i in progress(range(100), fill_char='#', empty_char='-'):
    time.sleep(0.05)

for i in progress(range(100), fill_char='>', empty_char=' '):
    time.sleep(0.05)

for i in progress(range(100), fill_char='/', empty_char='-'):
    time.sleep(0.05)


print("\n\n")