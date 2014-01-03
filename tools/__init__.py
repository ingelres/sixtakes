import sys


def progressbar(done, total, length):
    """ Draw a progress bar showing the current progress (done / total) over length+2 characters """
    done = done * length / total

    sys.stdout.write('\r[' + '=' * done + ' ' * (length - done) + ']')
    sys.stdout.flush()
