'''
ให้นักศึกษาสร้าง Class linklist2d , prinode , secnode และ method Append_primary, 
Delete_primary,
Append_secondary,
Delete_secondary
และ PrintList() และสร้าง 2Dlinklist ตามรูปในเอกสาร Lab4:Implement Datastructure ตอนที่ 2
'''


class Prinode:

  def __init__(self, data):
    self.data = data
    self.next_primary = None
    self.secondary = None


class Secnode:

  def __init__(self, data):
    self.data = data
    self.next_secondary = None


class Linklist2d:

  def __init__(self):
    self.head = None

  def Append_primary(self, new_data):
    new_node = Prinode(new_data)
    if not self.head:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next_primary:
      last_node = last_node.next_primary
    last_node.next_primary = new_node

  def Delete_primary(self, key):
    temp = self.head
    if temp is not None:
      if temp.data == key:
        self.head = temp.next_primary
        temp = None
        return
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next_primary
    if temp is None:
      return
    prev.next_primary = temp.next_primary
    temp = None

  def Append_secondary(self, primary_key, new_data):
    current = self.head
    while current:
      if current.data == primary_key:
        new_secnode = Secnode(new_data)
        if not current.secondary:
          current.secondary = new_secnode
        else:
          sec_last = current.secondary
          while sec_last.next_secondary:
            sec_last = sec_last.next_secondary
          sec_last.next_secondary = new_secnode
        return
      current = current.next_primary

  def Delete_secondary(self, primary_key, sec_key):
    current = self.head
    while current:
      if current.data == primary_key:
        sec_current = current.secondary
        if sec_current is not None:
          if sec_current.data == sec_key:
            current.secondary = sec_current.next_secondary
            sec_current = None
            return
          while sec_current:
            if sec_current.data == sec_key:
              break
            sec_prev = sec_current
            sec_current = sec_current.next_secondary
          if sec_current is None:
            return
          sec_prev.next_secondary = sec_current.next_secondary
          sec_current = None
        return
      current = current.next_primary

  def PrintList(self):
    primary = self.head
    while primary:
      print(f"Primary Node {primary.data}: ", end="")
      secondary = primary.secondary
      while secondary:
        print(f"{secondary.data},", end="")
        secondary = secondary.next_secondary
      print()
      primary = primary.next_primary


ll2d = Linklist2d()
ll2d.Append_primary('A')
ll2d.Append_primary('B')
ll2d.Append_primary('C')
ll2d.Append_secondary('A', "A1")
ll2d.Append_secondary('A', "A2")
ll2d.Append_secondary('B', "B1")
ll2d.Append_secondary('B', "B2")
ll2d.Append_secondary('C', "C1")
ll2d.Append_secondary('C', "C2")
ll2d.PrintList()
