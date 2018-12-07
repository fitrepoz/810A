import re

def main():
    filename = "hw5_text.txt"
    output = ''
    with open(filename) as f:
          for line in f:
                if line.rstrip().endswith('\\'):
                      next_line = next(f)
                      line = line.rstrip()[:-1] + next_line
                      output += line

if __name__ == "__main__":
    main()