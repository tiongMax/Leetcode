#include <vector>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rows = matrix.size(), cols = matrix[0].size();
        bool firstRowZero {}, firstColZero {};

        // Check if first row has any zeros
        for (int c { 0 }; c < cols; ++c) {
            if (matrix[0][c] == 0) {
                firstRowZero = true;
                break;
            }
        }

        // Check if first column has any zeros
        for (int r { 0 }; r < rows; ++r) {
            if (matrix[r][0] == 0) {
                firstColZero = true;
                break;
            }
        }

        // Use first row and column as markers
        for (int r { 1 }; r < rows; ++r) {
            for (int c { 1 }; c < cols; ++c) {
                if (matrix[r][c] == 0) {
                    matrix[r][0] = 0;
                    matrix[0][c] = 0;
                }
            }
        }

        // Set matrix cells to 0 based on markers
        for (int r { 1 }; r < rows; ++r) {
            for (int c { 1 }; c < cols; ++c) {
                if (matrix[r][0] == 0 || matrix[0][c] == 0) {
                    matrix[r][c] = 0;
                }
            }
        }

        // Zero out the first row if needed
        if (firstRowZero) {
            for (int c { 0 }; c < cols; ++c) {
                matrix[0][c] = 0;
            }
        }

        // Zero out the first column if needed
        if (firstColZero) {
            for (int r { 0 }; r < rows; ++r) {
                matrix[r][0] = 0;
            }
        }
    }
};
