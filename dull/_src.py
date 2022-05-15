import sys
from cProfile import Profile
from functools import wraps
from pstats import Stats
from pathlib import Path


def profile(
    to_file: bool = False,
    sort: str = "cumulative",
    name: str = None,
    folder: str = None,
):
    """Generate cProfile stats for wrapped function.

    If file is set to true, dumps stats to:
    `profile/<name>.dat`

    Check pstat values for sort:
    https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats

    :param to_file: dump stats to file instead of stderr
    :param sort: stat sorting
    :param name: profile name, defaults to wrapped function name
    :param folder: output folder, defaults to 'profile'
    """

    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            _name = fn.__name__
            if name:
                _name = name
            pr = Profile()
            try:
                return pr.runcall(fn, *args, **kwargs)
            finally:
                if to_file:
                    outputdir = Path(folder) if folder else Path("profile")
                    outputdir.mkdir(parents=True, exist_ok=True)
                    filename = outputdir / Path(_name + ".dat")
                    pr.dump_stats(filename)
                    print(
                        f"{fn.__name__}: profile saved to {filename}".center(89, "-"),
                        file=sys.stderr,
                    )
                else:
                    print(f"profile {_name}".center(89, "-"), file=sys.stderr)
                    Stats(pr, stream=sys.stderr).strip_dirs().sort_stats(
                        sort
                    ).print_stats()
                    print("-" * 89, file=sys.stderr)

        return wrapper

    return deco
