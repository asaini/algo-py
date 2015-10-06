import sys

def lev(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(lev(a[1:], b[1:])+(a[0] != b[0]), lev(a[1:], b)+1, lev(a, b[1:])+1)


def search(listA, listB):
    out = []
    
    for itemA in listA:
        min_edit_distance, min_index = sys.maxint, 0
        for index, itemB in enumerate(listB):
            distance = lev(itemA, itemB)
            if distance < min_edit_distance:
                min_index = index
                min_edit_distance = distance
        out.append(listB[min_index])
    return out


if __name__ == '__main__':

	listA = ['aple', 'lookin', 'naamez', 'bookz']
	listB = ['apple', 'apples', 'names', 'looking', 'orange']

	out = search(listA, listB)

	print out