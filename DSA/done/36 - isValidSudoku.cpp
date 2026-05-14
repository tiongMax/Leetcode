// https://leetcode.com/problems/valid-sudoku/

#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> rows, cols, squares;

        for (int r{0}; r < 9; r++) {
            for (int c{0}; c < 9; c++) {
                if (board[r][c] == '.') continue;

                int squareKey = (r / 3) * 3 + (c / 3);  // encodes to 0–8

                if (
                    rows[r].count(board[r][c]) ||
                    cols[c].count(board[r][c]) ||
                    squares[squareKey].count(board[r][c])
                )
                    return false;

                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[squareKey].insert(board[r][c]);
            }
        }
        return true;
    }
};
