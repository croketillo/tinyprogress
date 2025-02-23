from typing import Optional, Iterable, Any
import sys


def progress(
    iterable: Iterable[Any],
    total: Optional[int] = None,
    bar_length: int = 40,
    fill_char: str= '█',
    empty_char: str = ' ',
    task_name: Optional[str] = None
) -> None:
    """
    A lightweight progress bar for iterables.

    :param iterable: The iterable to wrap.
    :type iterable: Iterable[Any]
    :param total: Total number of iterations (optional, inferred from iterable if None).
    :type total: Optional[int]
    :param bar_length: Length of the progress bar in characters.
    :type bar_length: int
    :param fill_char: Character used to fill the progress bar.
    :type fill_char: str
    :param empty_char: Character used to represent remaining progress.
    :type empty_char: str
    :param task_name: Name of the task being executed (optional).
    :type task_name: Optional[str]
    :return: None
    :rtype: None
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
