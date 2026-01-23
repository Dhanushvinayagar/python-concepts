class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    

li = [1,2,3,4,5,6]

cycle_start=3

root = None
temp = None
cycle = None
for num in li:
    if not root:
        root = Node(num)
        temp=root
    else:
        temp.next = Node(num)
        temp = temp.next
        if cycle_start == num:
            cycle = temp
# create cycle            
temp.next = cycle

# find cycle in list
temp = root

slow = temp
fast = temp

is_cycle = False
while slow.next and fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        is_cycle = True
        break

if is_cycle:
    print("cycle found")
else:
    print("cycle not found")