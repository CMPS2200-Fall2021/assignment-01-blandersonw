"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb

def longest_run(mylist, key):
    runlist = []
    count = 0
    for i in range(len(mylist)):
        if mylist[i] == key:
            count+=1
            runlist.append(count)
        else:
            count=0
            runlist.append(count)
    return(max(runlist))

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def merge_results(left_result, right_result):
    result=Result(0,0,0,False)

    if(left_result.is_entire_range == True) and (right_result.is_entire_range == True):
            summ = left_result.left_size + right_result.left_size
            result = Result(summ, summ, summ, True)
            return result

    if(left_result.is_entire_range == True) and (right_result.is_entire_range == False):
            result = Result((left_result.longest_size + right_result.right_size), right_result.right_size, max(left_result.longest_size, right_result.longest_size, (left_result.right_size + right_result.left_size)), False)
            return result
    if(left_result.is_entire_range == False) and (right_result.is_entire_range == True):
             result = Result(left_result.left_size, (right_result.longest_size + left_result.right_size), max(left_result.longest_size, right_result.longest_size, (left_result.right_size + right_result.left_size)), False)
             return result
    if(left_result.is_entire_range == False) and (right_result.is_entire_range == False):
            result = Result(left_result.left_size, right_result.right_size, max(left_result.longest_size, right_result.longest_size, (left_result.right_size + right_result.left_size)), False)
            return result

def longest_run_recursive(mylist, key):
    if len(mylist) == 1:
        if (mylist[0] == key):
            res1 = Result(1, 1, 1, True)
            return res1
        else:
            res2 = Result(0, 0, 0, False)
            return res2
    else:
        left_result = longest_run_recursive(mylist[:len(mylist)//2], key)
        right_result = longest_run_recursive(mylist[len(mylist)//2:], key)
        return merge_results(left_result, right_result)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
print(longest_run_recursive([2,1,2,1,2,2,1,2,2,2,1,1], 2))
