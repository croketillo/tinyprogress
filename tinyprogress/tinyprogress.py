from typing import (
    Generator,
    Optional,
    Iterable,
    Union,
    TypeVar,
    Sized,
    Protocol,
    overload,
    Unpack,
    TypedDict,
    Callable
)
import sys

ColorCallable = Callable[[float], str]
reset_color = lambda _: '\033[0m'  # noqa: E731
default_color = lambda _: ''  # noqa: E731

T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)


class SizedIterable(Iterable[T_co], Sized, Protocol): ...


class Options(TypedDict, total=False):
    start_char: str
    end_char: str
    fill_char: str
    empty_char: str
    text_color: ColorCallable
    bar_color: ColorCallable


@overload
def progress(
    iterable: Iterable[T],
    total: int,
    bar_length: int = 40,
    task_name: Optional[str] = None,
    **options: Unpack[Options]
) -> Generator[T, None, None]: ...


@overload
def progress(
    iterable: SizedIterable[T],
    total: Optional[int] = None,
    bar_length: int = 40,
    task_name: Optional[str] = None,
    **options: Unpack[Options]
) -> Generator[T, None, None]: ...


def progress(
    iterable: Union[Iterable[T], SizedIterable[T]],
    total: Optional[int] = None,
    bar_length: int = 40,
    task_name: Optional[str] = None,
    **options: Unpack[Options]
) -> Generator[T, None, None]:
    """
    A lightweight progress bar for iterables.

    :param iterable: The iterable to wrap.
    :type iterable: Iterable[Any]
    :param total: Total number of iterations (optional, inferred from iterable if None).
    :type total: Optional[int]
    :param bar_length: Length of the progress bar in characters.
    :type bar_length: int
    :param task_name: Name of the task being executed (optional).
    :type task_name: Optional[str]
    :param fill_char: Character used to fill the progress bar.
    :type fill_char: str
    :param empty_char: Character used to represent remaining progress.
    :type empty_char: str
    :type start_char: str
    :param start_char: The start character (default: [)
    :type end_char: str
    :param end_char: The end character (default: ])
    :return: None
    :rtype: None
    """
    fill_char = options.get('fill_char', '█')
    empty_char = options.get('empty_char', ' ')
    start_char = options.get('start_char', '[')
    end_char = options.get('end_char', ']')
    text_color = options.get('text_color', default_color)
    bar_color = options.get('bar_color', default_color)
    if text_color is default_color:
        _reset = default_color
    else:
        _reset = reset_color

    if total is None:
        if isinstance(iterable, Sized):
            total = len(iterable)
        else:
            raise ValueError("Total iterations must be specified for non-sized iterables.")

    for i, item in enumerate(iterable, 1):
        progress = i / total
        filled_length = int(bar_length * progress)
        bar = fill_char * filled_length + empty_char * (bar_length - filled_length)
        task_display = f"{task_name} " if task_name else ""
        sys.stdout.write((
            f'\r{text_color(progress)}{task_display}{_reset(progress)}'
            f'{bar_color(progress)}{start_char}{bar}{end_char}{_reset(progress)}'
            f'{text_color(progress)}{int(progress * 100)}%  {i}/{total}{_reset(progress)}'
        ))
        sys.stdout.flush()
        yield item
    sys.stdout.write('\n')
    sys.stdout.flush()
