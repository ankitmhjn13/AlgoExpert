
"""


Time Complexity - o(n^2)
Space Complexity - o(n)

"""


def minRewards(scores):
    # Write your code here.
    reward = [1] * len(scores)
	idx = 0
        for i in range(1, len(scores)):
	    for j in range(i, idx, -1):
	        if scores[j] < scores[j-1] and reward[j-1] <= reward[j]:
		    reward[j-1] = reward[j-1] + 1
		elif scores[j] > scores[j-1]:
		    idx = j
		    reward[j] = reward[j-1] + 1
		    break
	sum = 0
        for elem in reward:
		sum = sum + elem
        return sum


if __name__ == "__main__":
    scores = <<user input>>
    print(minRewards(scores))

