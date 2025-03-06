from tinyprogress import progress
import time
from colorama import Fore, Style

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
        return Fore.RED + Style.BRIGHT
    return Fore.GREEN + Style.BRIGHT

def text_color(progress: float) -> str:
    return Fore.BLUE


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
