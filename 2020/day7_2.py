f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

checked_bags = []
found = []
bag_count = []

# return dict['bag color'] = number
def clean_contained(contained_bags: list) -> dict:
  cleaned = {}
  for bag in contained_bags:
    if bag == "no other bags.":
      return {}
    else:
      # 6 dotted black bags. -> dict[dotted black] = 6
      number = int(bag.strip().split(' ')[0])
      b = ' '.join(bag.split(' ')[1:-1])
      cleaned[b] = number
  return cleaned

def parse_tree():
    adj = {}
    for line in input:
        top_bag = line.split('bags')[0].strip()
        contained_bags = [i.strip() for i in line.split('contain')[1].split(',')]
        contained_bags = clean_contained(contained_bags)
        adj[top_bag] = contained_bags
    return adj

adj = parse_tree()
print(adj)


def dfs(adj, curr_bag, final_bag):
    if curr_bag == final_bag:
        return True
    if curr_bag in checked_bags:
        return False
    checked_bags.append(curr_bag)

    for bag in adj[curr_bag]:
        if bag not in checked_bags:
            if dfs(adj, bag, 'shiny gold'):
                checked_bags.append('shiny gold')
                return True
    return False

count = 0
dfs(adj, "shiny gold", "")
print(checked_bags)

