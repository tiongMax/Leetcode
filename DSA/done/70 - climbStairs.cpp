// https://leetcode.com/problems/climbing-stairs/

#include <vector>

// Memo
class Solution {
private:
    int solve(int currentStep, int targetStep, std::vector<int>& memo) {
        // Base case: If we reach exactly the top, we found 1 valid way
        if (currentStep == targetStep) {
            return 1;
        }
        // Base case: If we overstep the top, this path is invalid
        if (currentStep > targetStep) {
            return 0;
        }
        
        // If we have already calculated the ways for this step, return the cached result
        if (memo[currentStep] != -1) {
            return memo[currentStep];
        }
        
        // Recursively find ways by taking 1 step + taking 2 steps
        int takeOneStep = solve(currentStep + 1, targetStep, memo);
        int takeTwoSteps = solve(currentStep + 2, targetStep, memo);
        
        // Cache and return the result for the current step
        return memo[currentStep] = takeOneStep + takeTwoSteps;
    }

public:
    int climbStairs(int n) {
        // Initialize memo vector with -1 to indicate uncalculated steps
        // Size is n + 1 to comfortably index from 0 up to n
        std::vector<int> memo(n + 1, -1);
        
        // Start from step 0
        return solve(0, n, memo);
    }
};

// Tabular
class Solution {
public:
    int climbStairs(int n) {
        int prev{1}, prev2{0};
        for (int i{n - 1}; i >= 0; i--) {
            int cur{prev + prev2};
            prev2 = prev;
            prev = cur;
        }

        return prev;
    }
};