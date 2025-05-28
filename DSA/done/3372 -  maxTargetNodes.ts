// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

function maxTargetNodes(edges1: number[][], edges2: number[][], k: number): number[] {
    const buildAdj = (edges: number[][]): Map<number, number[]> => {
        const adj = new Map<number, number[]>();
        for (const [u, v] of edges) {
            if (!adj.has(u)) adj.set(u, []);
            if (!adj.has(v)) adj.set(v, []);
            adj.get(u)!.push(v);
            adj.get(v)!.push(u);
        }
        return adj;
    };

    const dfs = (node: number, depth: number, adj: Map<number, number[]>, visited: Set<number>): number => {
        if (depth < 0) return 0;
        visited.add(node);
        let count = 1;
        for (const neighbor of adj.get(node)!) {
            if (!visited.has(neighbor)) {
                count += dfs(neighbor, depth - 1, adj, visited);
            }
        }
        return count;
    };

    const adj1 = buildAdj(edges1);
    const adj2 = buildAdj(edges2);
    const n = edges1.length + 1;
    const m = edges2.length + 1;

    let max2 = 0;
    for (let i = 0; i < m; i++) {
        max2 = Math.max(max2, dfs(i, k - 1, adj2, new Set()));
    }

    const res: number[] = [];
    for (let i = 0; i < n; i++) {
        const cnt = dfs(i, k, adj1, new Set());
        res.push(cnt + max2);
    }

    return res;
}
