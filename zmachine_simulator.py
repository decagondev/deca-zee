import sys

class ZMachine:
  def __init__(self, story_file):
    self.memory = bytearray()
    self.pc = 0
    self.stack = []
    self.globals = [0] * 240
    self.locals = []
    self.load_story(story_file)

def load_story(self, story_file):
  pass

def read_byte(self, address):
  pass

def read_word(self, address):
  pass

def decode_zscii(self, text_address):
  pass

def run(self):
  pass

def execute_instruction(self, opcode):
  pass


def main():
  if len(sys.argv) != 2:
    print("Usage: python zmachine_simulator.py <zork1.z3>")
    sys.exit(1)

  simulator = ZMachine(sys.argv[1])
  simulatr.run()

if __name__ == "__main__":
  main()
