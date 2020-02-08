from expressionCalculator import parser, calculate
from emojiAndNormalConverter import myToEmojiConverter

# from __future__ import print_function

import argparse
import sys


def fmt_err(fmt, *args):
  """Prints a formatted message to STDERR"""
  print(fmt % args, file=sys.stderr)


def main():
  # Parse arguments - not sure why it gives 'ArgumentParser' object is not callable when the input is correct
  # TODO: check why

  # parser = argparse.ArgumentParser(
  #     description="An example application for flags and I/O on STDIN and STDOUT")
  # parser.add_argument("-human",
  #                     help="Print in human readable format as well (ASCII)",
  #                     action='store_true')
  # args = parser.parse_args()
  try:
    std = sys.stdin.read()
  except IOError as ioe:
    fmt_err("Error: Unable to read from STDIN: %s\n", ioe)
    return
  print(std)
  try:
    expression = myToEmojiConverter.convertEmojiStringToNormalOutput(std)
    eq, status = parser(expression)
    if status > 0:
    # Some error during the parsing
      print("🤷")
      return
    output = int(calculate(eq))
    print(myToEmojiConverter.convertNumberToEmoji(output))
    # print(output)
  except Exception as e:
    print("🤷")
    # Also print why we had issues
    print(e)


if __name__ == '__main__':
  main()