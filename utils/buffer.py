import sys
import select

_poll = select.poll()
_poll.register(sys.stdin, select.POLLIN)


def read() -> str:
    poll_results = _poll.poll(1)
    if poll_results:
        data = sys.stdin.readline().strip()
        return data


