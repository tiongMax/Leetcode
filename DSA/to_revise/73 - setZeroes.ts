// # https://leetcode.com/problems/set-matrix-zeroes/

/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    const rows = matrix.length;
    const cols = matrix[0].length;

    let firstRowZero = false;
    let firstColZero = false;

    // Check first row for zeros
    for (let c = 0; c < cols; c++) {
        if (matrix[0][c] === 0) {
            firstRowZero = true;
            break;
        }
    }

    // Check first column for zeros
    for (let r = 0; r < rows; r++) {
        if (matrix[r][0] === 0) {
            firstColZero = true;
            break;
        }
    }

    // Use first row and column as markers
    for (let r = 1; r < rows; r++) {
        for (let c = 1; c < cols; c++) {
            if (matrix[r][c] === 0) {
                matrix[r][0] = 0;
                matrix[0][c] = 0;
            }
        }
    }

    // Set matrix cells to 0 based on markers
    for (let r = 1; r < rows; r++) {
        for (let c = 1; c < cols; c++) {
            if (matrix[r][0] === 0 || matrix[0][c] === 0) {
                matrix[r][c] = 0;
            }
        }
    }

    // Zero out the first row if needed
    if (firstRowZero) {
        for (let c = 0; c < cols; c++) {
            matrix[0][c] = 0;
        }
    }

    // Zero out the first column if needed
    if (firstColZero) {
        for (let r = 0; r < rows; r++) {
            matrix[r][0] = 0;
        }
    }
}
