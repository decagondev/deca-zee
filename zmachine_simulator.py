import sys
import struct

class ZMachine:
  def __init__(self, story_file):
    self.memory = bytearray()
    self.pc = 0
    self.stack = []
    self.globals = [0] * 240
    self.locals = []
    self.load_story(story_file)

  def load_story(self, story_file):
    """Load and validate the .z3 story file."""
    try:
      with open(story_file, 'rb') as f:
        self.memory = bytearray(f.read())
    except:
      print(f"Error: Story file '{story_file}' not found.")
      sys.exit(1)
  
    self.version = self.memory[0]
    
    if self.version != 3:
      print(f"Error: Only Z-Machine version 3 is supported, found version {self.version}.")
      sys.exit(1)
  
    self.pc = self.read_word(0x06)
  
  def read_byte(self, address):
    """Read a byte from memory."""
    return self.memory[address]
  
  def read_word(self, address):
    """Read a 16-bit word from memory."""
    return (self.memory[address] << 8) | self.memory[address + 1]
  
  def decode_zscii(self, text_address):
    """Decode ZSCII text to ASCII (Simplified for Version 3)."""
    result = ""
    while True:
      word = self.read_word(text_address)
      text_address += 2
      for shift in [10, 5, 0]:
        zchar = (word >> shift) & 0x1F
        if zchar == 0:
          result += " "
        elif zchar >= 6:
          result += chr(zchar + 91)
      if word & 0x8000:
        break
    return result
  
  def run(self):
    """Main interpreter loop."""
    while True:
      opcode = self.read_byte(self.pc)
      self.pc += 1
      self.execute_instruction(opcode)
  
  def execute_instruction(self, opcode):
    """Decode and execute an instruction."""
    if opcode == 0xB2:
      text_address = self.read_word(self.pc)
      self.pc += 2
      text = self.decode_zscii(text_address)
      print(text, end="")
    elif opcode == 0xB0:
      self.stack.pop()
      return
    elif opcode == 0xDA:
      operand_count = self.read_byte(self.pc)
      self.pc += 1
      operands = []
      for _ in range(operand_count):
        operand_type = self.read_byte(self.pc)
        self.pc += 1
        if operand_type == 0:
            value = self.read_word(self.pc)
            self.pc += 2
        elif operand_type == 1:
            value = self.read_byte(self.pc)
            self.pc += 1
        else:
            print(f"Unsupported operand type: {operand_type}")
            return
          
        operands.append(value)
        branch = self.read_byte(self.pc)
        self.pc += 1
  
        if len(operands) >= 2 and operands[0] == operands[1]:
          if branch & 0x80:
            offset = branch & 0x3F
            if branch & 0x40:
              self.pc += offset - 2
            else:
              offset = self.read_word(self.pc)
              self.pc += 2
              self.pc += offset - 2
    else:
      print(f"Unsupported opcode: {hex(opcode)}")
      sys.exit(1)


def main():
  if len(sys.argv) != 2:
    print("Usage: python zmachine_simulator.py <zork1.z3>")
    sys.exit(1)

  simulator = ZMachine(sys.argv[1])
  simulator.run()

if __name__ == "__main__":
  main()
