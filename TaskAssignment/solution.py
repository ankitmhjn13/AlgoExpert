'''

The solution is - sort the array
the maximum time taken by any two tasks would be equal to sum of first element in array and sum of last element in arary
keep two counter first counter at first element of array and end counter at last element of array.
form the group of element at first counter and end counter
now increment the first counter and decrement the secong counter and add both the elem to result 
and keep performing the steps untill the first counter is less than last counter

Time Complexity - o(nlogn)
Space Complexity - o(n)

time complexity is complexity due to sorting array elements.
space complexity is due to extra key value mapping maintained for mapping the elem and index.

'''


def taskAssignment(k, tasks):
    # Write your code here.
    elemIndexDict = getElemIdxMapping(tasks)
	finalResult = []
	tasks.sort()

	start = 0
	end = len(tasks) - 1
	while start < end:
		elemList = []
		elemList.append(elemIndexDict[tasks[start]][0])
        elemList.append(elemIndexDict[tasks[end]][0])
        if len(elemIndexDict[tasks[start]]) > 1:
            elemIndexDict[tasks[start]] = elemIndexDict[tasks[start]][1:]
        if len(elemIndexDict[tasks[end]]) > 1:
            elemIndexDict[tasks[end]] = elemIndexDict[tasks[end]][1:]
        finalResult.append(elemList)
		start += 1
		end -= 1
	return finalResult


def getElemIdxMapping(tasksList):
	elemIndexDict = {}
	for idx, elem in enumerate(tasksList):
		if elem in elemIndexDict:
			elemIndexDict[elem].append(idx)
		else:
			elemIndexDict[elem] = [idx]
	return elemIndexDict



if __name__ == "__main__":
    tasks = <<user input>>
    taskAssignment(tasks)
