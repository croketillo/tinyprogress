import sys


def progress(iterable, total=None, bar_length=40, fill_char='█', empty_char=' ', task_name=None):
    """
    A lightweight progress bar for iterables.
    
    :param iterable: The iterable to wrap.
    :param total: Total number of iterations (optional, inferred from iterable if None).
    :param bar_length: Length of the progress bar in characters.
    :param fill_char: Character used to fill the progress bar.
    :param empty_char: Character used to represent remaining progress.
    :param task_name: Name of the task being executed (optional, defaults to None).
    """
    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            raise ValueError("Total iterations must be specified for non-sized iterables.")
    
    for i, item in enumerate(iterable, 1):
        progress = i / total
        filled_length = int(bar_length * progress)
        bar = fill_char * filled_length + empty_char * (bar_length - filled_length)
        task_display = f"{task_name} " if task_name else ""
        sys.stdout.write(f'\r{task_display}[{bar}] {int(progress * 100)}%  {i}/{total}')
        sys.stdout.flush()
        yield item
    sys.stdout.write('\n')
    sys.stdout.flush()
