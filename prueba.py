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


for i in progress(range(100), fill_char='—', start_char='', end_char=''):
    time.sleep(0.05)
    
print('\nCUSTOM COLORS')
def bar_color(progress: float) -> str:
    if progress < 0.7:
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

print("\n\n")
