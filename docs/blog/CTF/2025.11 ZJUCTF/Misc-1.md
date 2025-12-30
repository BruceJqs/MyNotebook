# Bingo

## Tag

Dirty Work

## Writeup

根据描述一个一个写约束然后求解器求解即可，Payload 如下：

```python
from z3 import *

def solve():
    s = Solver()

    grid = [[Int(f'x_{r}_{c}') for c in range(5)] for r in range(5)]

    for r in range(5):
        for c in range(5):
            s.add(grid[r][c] >= 0, grid[r][c] <= 1)

    def Sum(lst): return sum(lst)
    
    row_sums = [Sum(grid[r]) for r in range(5)]
    col_sums = [Sum([grid[r][c] for r in range(5)]) for c in range(5)]
    
    diag1 = [grid[i][i] for i in range(5)]
    diag2 = [grid[i][4-i] for i in range(5)]
    diag1_sum = Sum(diag1)
    diag2_sum = Sum(diag2)
    
    total_sum = Sum([grid[r][c] for r in range(5) for c in range(5)])

    primes = [2,3,5,7,11,13,17,19,23]
    composites = [4,6,8,9,10,12,14,15,16,18,20,21,22,24,25]

    def is_prime(n):
        return Or([n == p for p in primes])
    
    def is_composite(n):
        return Or([n == c for c in composites])
    
    # "答案中有且仅有一个行/列/对角线全为 1"
    rows_full = [If(rs == 5, 1, 0) for rs in row_sums]
    cols_full = [If(cs == 5, 1, 0) for cs in col_sums]
    d1_full = If(diag1_sum == 5, 1, 0)
    d2_full = If(diag2_sum == 5, 1, 0)
    s.add(Sum(rows_full + cols_full + [d1_full, d2_full]) == 1)


    # ================= 逐行逐列添加约束 =================

    # --- 第 1 行 ---
    
    # R1C1 (0,0): 此格为 1，且总勾数为素数
    s.add(Implies(grid[0][0] == 1, is_prime(total_sum)))

    # R1C2 (0,1): 总勾数 >= 12
    s.add(grid[0][1] == If(total_sum >= 12, 1, 0))

    # R1C3 (0,2): 第2列勾数 <= 第3列勾数，且第2列与第3列勾数奇偶性相同
    cond_r1c3 = And(col_sums[1] <= col_sums[2], col_sums[1] % 2 == col_sums[2] % 2)
    s.add(grid[0][2] == If(cond_r1c3, 1, 0))

    # R1C4 (0,3): 第1行勾数 < 第4列勾数
    s.add(grid[0][3] == If(row_sums[0] < col_sums[3], 1, 0))

    # R1C5 (0,4): 存在一行被填满
    s.add(grid[0][4] == If(Sum(rows_full) >= 1, 1, 0))


    # --- 第 2 行 ---

    # R2C1 (1,0): 此格为 1，都可以，没有约束
    # R2C2 (1,1): total <= 13 XOR 至少两行为奇数
    odd_rows_count = Sum([If(rs % 2 != 0, 1, 0) for rs in row_sums])
    cond_r2c2 = (total_sum <= 13) != (odd_rows_count >= 2)
    s.add(grid[1][1] == If(cond_r2c2, 1, 0))

    # R2C3 (1,2): 恰好存在 1 行完全为空
    empty_rows_count = Sum([If(rs == 0, 1, 0) for rs in row_sums])
    s.add(grid[1][2] == If(empty_rows_count == 1, 1, 0))

    # R2C4 (1,3): 1 不是质数
    s.add(grid[1][3] == 1)

    # R2C5 (1,4): 存在某个2*2的区域全为 1
    wins_2x2 = []
    for r in range(4):
        for c in range(4):
            wins_2x2.append(And(grid[r][c]==1, grid[r+1][c]==1, grid[r][c+1]==1, grid[r+1][c+1]==1))
    s.add(grid[1][4] == If(Or(wins_2x2), 1, 0))


    # --- 第 3 行 ---

    # R3C1 (2,0): 中心格为 1，且两条对角线上的 1 数为合数
    diag_indices = set([(i,i) for i in range(5)] + [(i,4-i) for i in range(5)])
    diag_union_sum = Sum([grid[r][c] for r,c in diag_indices])
    
    s.add(grid[2][0] == If(And(grid[2][2] == 1, is_composite(diag_union_sum)), 1, 0))

    # R3C2 (2,1): 左上 3×3 区域至少 5 个为 1
    tl_3x3_sum = Sum([grid[r][c] for r in range(3) for c in range(3)])
    s.add(grid[2][1] == If(tl_3x3_sum >= 5, 1, 0))

    # R3C3 (2,2): 上下相邻均为1的格对不少于四对
    v_pairs = Sum([If(And(grid[r][c]==1, grid[r+1][c]==1), 1, 0) for r in range(4) for c in range(5)])
    s.add(grid[2][2] == If(v_pairs >= 4, 1, 0))

    # R3C4 (2,3): 上下相邻均为1的格对不多于六对
    s.add(grid[2][3] == If(v_pairs <= 6, 1, 0))

    # R3C5 (2,4): 答案不是对角线
    is_diag_ans = Or(diag1_sum == 5, diag2_sum == 5)
    s.add(grid[2][4] == If(Not(is_diag_ans), 1, 0))


    # --- 第 4 行 ---

    # R4C1 (3,0): 此格相邻三格的勾数为偶数
    neighbors_sum = grid[2][0] + grid[4][0] + grid[3][1]
    s.add(grid[3][0] == If(neighbors_sum % 2 == 0, 1, 0))

    # R4C2 (3,1): 令 a = 第4行和，b = 第2列和，要求 (a*a + b) % 5 <= 3 且 a <= b
    a = row_sums[3]
    b = col_sums[1]
    val = (a * a + b) % 5
    s.add(grid[3][1] == If(And(val <= 3, a <= b), 1, 0))

    # R4C3 (3,2): 全体勾的重心不偏右
    moment_x = Sum([c * grid[r][c] for r in range(5) for c in range(5)])
    s.add(grid[3][2] == If(moment_x <= 2 * total_sum, 1, 0))

    # R4C4 (3,3): 此行不是正确答案
    s.add(grid[3][3] == If(row_sums[3] != 5, 1, 0))

    # R4C5 (3,4): "如果没有'请先将本格打勾'的逻辑起点,此题不可解"
    s.add(grid[3][4] == 0)


    # --- 第 5 行 ---

    # R5C1 (4,0): 第四列的勾数与第二列的勾数之和为合数
    s.add(grid[4][0] == If(is_composite(col_sums[3] + col_sums[1]), 1, 0))

    # R5C2 (4,1): 1 不是合数 XOR 此列是正确答案
    s.add(grid[4][1] == If(col_sums[1] != 5, 1, 0))

    # R5C3 (4,2): 此列是勾数唯一最少的列
    others = [0, 1, 3, 4]
    is_unique_min = And([col_sums[2] < col_sums[j] for j in others])
    s.add(grid[4][2] == If(is_unique_min, 1, 0))

    # R5C4 (4,3): 至少存在某一行连续三个格子打勾且至少存在某一列连续三个格子打勾
    def has_consec_3(line_vars):
        c1 = And(line_vars[0]==1, line_vars[1]==1, line_vars[2]==1)
        c2 = And(line_vars[1]==1, line_vars[2]==1, line_vars[3]==1)
        c3 = And(line_vars[2]==1, line_vars[3]==1, line_vars[4]==1)
        return Or(c1, c2, c3)

    row_has_3 = Or([has_consec_3(grid[r]) for r in range(5)])
    cols_list_vars = [[grid[r][c] for r in range(5)] for c in range(5)]
    col_has_3 = Or([has_consec_3(cols_list_vars[c]) for c in range(5)])
    
    s.add(grid[4][3] == If(And(row_has_3, col_has_3), 1, 0))

    # R5C5 (4,4): 不存在某一对角线有至少三个格子打勾
    d1_cnt = diag1_sum
    d2_cnt = diag2_sum
    s.add(grid[4][4] == If(And(d1_cnt <= 2, d2_cnt <= 2), 1, 0))

    if s.check() == sat:
        m = s.model()
        
        res_grid = []
        flag_parts = []
        
        print("\n矩阵:")
        for r in range(5):
            row_vals = []
            row_str = ""
            for c in range(5):
                val = m[grid[r][c]].as_long()
                row_vals.append(val)
                row_str += str(val)
            res_grid.append(row_vals)
            flag_parts.append(row_str)
            print(row_vals)
            
        flag = "ZJUCTF{" + "_".join(flag_parts) + "}"
        print("\nFlag:")
        print(flag)
        
    else:
        print("无解，请检查约束条件是否理解有误。")

if __name__ == "__main__":
    solve()

```

最终 flag：`ZJUCTF{10110_00010_00111_01010_01010}`