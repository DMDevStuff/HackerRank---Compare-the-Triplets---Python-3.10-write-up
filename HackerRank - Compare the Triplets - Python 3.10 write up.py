##    Alice and Bob each created one problem for HackerRank. A reviewer rates
##    the two challenges, awarding points on a scale from 1 to 100 for three
##    categories: problem clarity, originality, and difficulty.
##
##    The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]),
##    and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
##
##    The task is to find their comparison points by comparing a[0] with b[0],
##    a[1] with b[1], and a[2] with b[2].
##
##        If a[i] > b[i], then Alice is awarded 1 point.
##        If a[i] < b[i], then Bob is awarded 1 point.
##        If a[i] = b[i], then neither person receives a point.
##
##    Comparison points is the total points a person earned.
##
##    Given a and b, determine their respective comparison points. 

##### ##### ##### #####

#   An iterative solution.
#   O(n).  n is the length of the input arrays (they are the same length).
#   Compares the values at each index of the input arrays.
#   Returns a list containing two integers that are the result of the comparisons.

def solutionOne(integer_array_A, integer_array_B):
    alice_score = 0
    bob_score = 0
    for index in range(len(integer_array_A)):
        if integer_array_A[index] > integer_array_B[index]:
            alice_score += 1
        elif integer_array_A[index] < integer_array_B[index]:
            bob_score += 1
    return [alice_score, bob_score]

##### ##### ##### #####

#   Testing suite for solutionOne function.

def test():

    border = '##### ##### ##### #####'

    alice_ratings_one = [5,6,7]
    bob_ratings_one = [3,6,10]
    expected_result_one = [1,1]

    alice_ratings_two = [17,28,30]
    bob_ratings_two = [99,16,8]
    expected_result_two = [2,1]

    solution_one_test_one = solutionOne(alice_ratings_one, bob_ratings_one)
    solution_one_test_two = solutionOne(alice_ratings_two, bob_ratings_two)

    print()
    print(border)
    print()

    print('Solution One - Test One Result: ' + str(solution_one_test_one))
    print('Expected Result: ' + str(expected_result_one))

    print()
    print(border)
    print()

    print('Solution One - Test Two Result: ' + str(solution_one_test_two))
    print('Expected Result: ' + str(expected_result_two))

    print()
    print(border)
    print()

    return None
