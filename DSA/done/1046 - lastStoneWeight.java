import java.util.PriorityQueue;

class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        for (int s : stones) {
            maxHeap.offer(-s);
        }

        while (maxHeap.size() > 1) {
            int first = maxHeap.poll();
            int second = maxHeap.poll();
            if (second > first) {
                maxHeap.offer(first - second);
            }
        }

        return maxHeap.size() == 0 ? 0 : -maxHeap.peek();
    }
}