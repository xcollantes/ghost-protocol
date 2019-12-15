"""Start file for Ghost Protocol."""

from ghost_protocol import GhostProtocol


def main():
  import argparse

  parser = argparse.ArgumentParser(description='Simulate user at computer.')

  parser.add_argument('--windows', dest='window_shift_flag', default=False,
                      type=bool, metavar='',
                      help='Add flag to switch between windows.')

  parser.add_argument('--pause', dest='pause', default=1,
                      metavar='',
                      type=int,
                      help='Seconds to wait between actions. (default: 1 sec.)')

  parser.add_argument('--timer', dest='timer',
                      metavar='',
                      type=int, help='Specify seconds for runtime.')

  args = parser.parse_args()

  GhostProtocol(windows, pause, timer)


if __name__ == '__main__':
  main()
