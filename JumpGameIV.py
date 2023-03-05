from collections import defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        last_item = arr[-1]
        dups = defaultdict(list)
        f_dups = {}
        for i,j in enumerate(arr):
            dups[j].append(i)
        for i,j in dups.items():
            if len(j)>1:
                items = j
                continuous = items[0]
                f_dups[i] = [continuous]
                for k in range(1,len(items)):
                    if items[k] == continuous+1:
                        continuous = items[k]
                        continue
                    else:
                        f_dups[i].append(items[k])
                        continuous = items[k]
                f_dups[i].append(continuous)


        adjacents = defaultdict(list)
        for i in range(len(arr)):
            if i < len(arr)-1:
                adjacents[i].append(i+1)
            if i >= 1:
                adjacents[i].append(i-1)
            if arr[i] in f_dups.keys():
                for j in f_dups[arr[i]]:
                    if i != j:
                        adjacents[i].insert(0,j)
        #print(arr)
        #print(f_dups)
        # return 0
        #print(adjacents)
        visit =[False for _ in range(len(arr))]
        queue = []
        queue.append(0)
        visit[0] = True
        if len(arr) == 1:
            return 0
        steps = 1
        while len(queue) != 0:
            l = len(queue)
            while l > 0:
                item = queue[0]
                del queue[0]
                if item == len(arr) -1:
                    # print("STEP {} FOUND LAST ITEM {}: {}".format(steps, item, arr[item]))
                    break
                for i in adjacents[item]:
                    if visit[i] != True:
                        # print("STEP {} INSERTED FOR {} {}: {}".format(steps, item, i, arr[i]))
                        if i == len(arr) - 1:
                            return steps
                        queue.append(i)
                        visit[i] = True
                adjacents.pop(item)
                #print(adjacents)
                l -= 1
            steps += 1
        return steps
