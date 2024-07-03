"""
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board.
The player has to fill the board in a very specific way:

each row of the board must contain all digits from 1 to 9 (the order doesn't
matter)
each column of the board must contain all digits from 1 to 9 (again, the order
doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table
must contain all digits from 1 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the
data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.

Test Data
Sample input:
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
Sample output:
Yes

Sample input:
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
Sample output:
No


"""


def sudoku(b):
    for box in b:
        cell_dict = {1: False, 2: False, 3: False,
                     4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
        for cell in box:
            if cell_dict.get(int(cell)):
                return "No"

            cell_dict[int(cell)] = True

        for item in cell_dict.values():
            if item:
                continue
            return "No"

    return "Yes"


a = input("")

if len(a) == 81:
    sub_list = [a[i:i+9] for i in range(0, len(a), 9)]
    board = list(["" for _ in range(9)])
    rows = [list(sub_list[i:i+3]) for i in range(0, 9, 3)]
    row_one, row_two, row_three, row_four, row_five, row_six, row_seven, row_eight, row_nine = [
        row for group in rows for row in group]
    board[0] = ''.join([row_one[num] + row_two[num] +
                        row_three[num] for num in range(3)])
    board[1] = ''.join([row_one[num] + row_two[num] + row_three[num]
                        for num in range(3, 6)])
    board[2] = ''.join([row_one[num] + row_two[num] + row_three[num]
                        for num in range(6, 9)])

    board[3] = ''.join([row_four[num] + row_five[num] +
                        row_six[num] for num in range(3)])
    board[4] = ''.join([row_four[num] + row_five[num] + row_six[num]
                        for num in range(3, 6)])
    board[5] = ''.join([row_four[num] + row_five[num] + row_six[num]
                        for num in range(6, 9)])

    board[6] = ''.join([row_seven[num] + row_eight[num] +
                        row_nine[num] for num in range(3)])
    board[7] = ''.join([row_seven[num] + row_eight[num] +
                        row_nine[num] for num in range(3, 6)])
    board[8] = ''.join([row_seven[num] + row_eight[num] +
                        row_nine[num] for num in range(6, 9)])

    print(sudoku(b=board))
