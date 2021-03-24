"""
A Boy decided to visit his girlfriend’s house. It turned out that the boy's house is located at
point 0 and his girlfriend's house is located at point x (x > 0) of the coordinate line. In one step the
boy can move 1, 2, 3, 4 or 5 positions forward. Determine what is the minimum number of steps he
need to make in order to get to his girlfriend's house?
Input:
The first line of the input contains an integer x (1 ≤ x ≤ 1000000) — the coordinate of the
girlfriend's house.
Output:
Print the minimum number of steps that boy needs to make to get from point 0 to point x.
Examples:
Input:
5
Output:
1
Input:
12
Output:
3
Note:
In the first sample the boy needs to make one step of length 5 to reach the point x.
In the second sample the boy can get to point x if he moves by 3, 5 and 4. There are other ways to
get the optimal answer but the boy cannot reach x in less than three moves
"""
n = int(input("Enter the coordinates of girlfriend's house="))
print(f"The minimum number of steps that boy needs to make to get from point 0 to point {n} are={n//5 +1}")
