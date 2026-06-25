# Pseudo

## Tag

LCG 截断+BSGS

***

## Writeup

题目给出的 LCG 生成器满足：
$$
\begin{aligned}
K_{i+1} &= (a K_i + b)\text{ mod }c\\
R_i &= K_{i+1} // d
\end{aligned}
$$
已知 $R_0$ 和 $R_1$，有：
$$
\begin{aligned}
K_1 &= d R_0 + e_0\\
K_2 &= d R_1 + e_1\\
0 \leq &e_0, e_1 < d
\end{aligned}
$$
其中 $e_0, e_1$ 是未知的低位截断部分。又由于 $K_2 = (a K_1 + b)\text{ mod }c$，故存在整数 $n$ 使得 $a(dR_0 + e_0) + b = dR_1 + e_1 + nc$，整理可得：

$$
\begin{aligned}
ae_0 - e_1 &= n c - A\\
A = a d R_0 &+ b - d R_1
\end{aligned}
$$
这样，原问题被转化为恢复 $(e_0, e_1, n)$，由 $0 \leq e_0, e_1 < d$ 可知 $-(d - 1) \leq a e_0 - e_1 \leq a(d - 1)$，代回上式即可得到 $n$ 的取值区间：$\text{ceil}(\frac{A - (d - 1)}{c}) \leq n \leq \text{floor}(\frac{A + a(d - 1)}{c})$，该区间的长度约为 $\frac{ad}{c}$，结合题目参数位数，可估计候选数规模约为 $2^{281 + 256 - 512} = 2^{25}$，还可以用 Baby-Step Giant Step（BSGS）优化。

观察到 $e_1(n) = (A - n c)\text{ mod }a$，当 $n$ 增加 1 时，$e_1$ 在模 $a$ 意义下仅仅减去一个固定步长 $c\text{ mod }a$。也就是说，随着 $n$ 变化，$e_1$ 沿着模 $a$ 上的一条等差轨道移动。设候选区间长度为 $N$，取 $m = \text{ceil}(\sqrt{N})$，将偏移量表示为

$$
\begin{aligned}
n &= n_0 + i m + j\\
0 &\leq j < m
\end{aligned}
$$
于是有 $e_1(n) = e_1(n_0) - i(m(c\text{ mod }a)) - j(c\text{ mod }a)\text{ mod }a$，此时可以分成两部分：

1. 预处理所有 baby step，即 $j(c\text{ mod }a)\text{ mod }a$
2. 枚举 giant step，即 $e_1(n_0) - i(m(c\text{ mod }a))\text{ mod }a$

对于每个 giant step，只需查询哪些 baby step 会使最终结果落入区间 $[0, d)$。由于这是模 $a$ 上的区间查询，实现时可将 baby step 按值排序，并对对应的环形区间做二分检索。Payload 如下：

```python
import argparse
import bisect
import math
import re
from dataclasses import dataclass
from functools import reduce
from hashlib import sha256

from Crypto.Util.number import long_to_bytes as i2b


LINE_PATTERNS = {
    "a": re.compile(r"a\s*=\s*([0-9a-fA-F]+)"),
    "b": re.compile(r"b\s*=\s*([0-9a-fA-F]+)"),
    "c": re.compile(r"c\s*=\s*([0-9a-fA-F]+)"),
    "d": re.compile(r"d\s*=\s*([0-9a-fA-F]+)"),
    "r0": re.compile(r"R0\s*=\s*([0-9a-fA-F]+)"),
    "r1": re.compile(r"R1\s*=\s*([0-9a-fA-F]+)"),
    "digest": re.compile(r"sha256\(R\)\[:16\]\s*=\s*([0-9a-fA-F]+)"),
}


@dataclass
class Challenge:
    a: int
    b: int
    c: int
    d: int
    r0: int
    r1: int
    digest_prefix: str


def digest_prefix(outputs):
    blob = reduce(lambda acc, value: acc + i2b(value), outputs, b"")
    return sha256(blob).hexdigest()[:16]


def generate_outputs(a, b, c, d, k1, count=20):
    outputs = []
    state = k1
    for _ in range(count):
        outputs.append(state // d)
        state = (a * state + b) % c
    return outputs


def parse_challenge(text):
    fields = {}
    for key, pattern in LINE_PATTERNS.items():
        match = pattern.search(text)
        if not match:
            raise ValueError(f"missing field: {key}")
        fields[key] = match.group(1)
    return Challenge(
        a=int(fields["a"], 16),
        b=int(fields["b"], 16),
        c=int(fields["c"], 16),
        d=int(fields["d"], 16),
        r0=int(fields["r0"], 16),
        r1=int(fields["r1"], 16),
        digest_prefix=fields["digest"].lower(),
    )


def _values_in_circular_interval(sorted_pairs, sorted_values, modulus, right, width):
    left = (right - (width - 1)) % modulus
    if left <= right:
        lo = bisect.bisect_left(sorted_values, left)
        hi = bisect.bisect_right(sorted_values, right)
        for idx in range(lo, hi):
            yield sorted_pairs[idx]
        return

    lo = bisect.bisect_left(sorted_values, left)
    hi = len(sorted_pairs)
    for idx in range(lo, hi):
        yield sorted_pairs[idx]
    lo = 0
    hi = bisect.bisect_right(sorted_values, right)
    for idx in range(lo, hi):
        yield sorted_pairs[idx]


def recover_outputs(a, b, c, d, r0, r1, prefix=None):
    target_prefix = prefix.lower() if prefix else None

    if c == 0 or d == 0:
        raise ValueError("challenge parameters are invalid: c and d must be non-zero")

    if a == 0:
        k1 = b % c
        if k1 // d != r0:
            raise ValueError("no state matches the provided outputs")
        outputs = [r0]
        state = k1
        for _ in range(19):
            state = b % c
            outputs.append(state // d)
        if outputs[1] != r1:
            raise ValueError("no state matches the provided outputs")
        if target_prefix and digest_prefix(outputs) != target_prefix:
            raise ValueError("hash prefix does not match")
        return outputs

    A = a * d * r0 + b - d * r1
    n_lo = (A - (d - 1) + c - 1) // c
    n_hi = (A + a * (d - 1)) // c
    total = n_hi - n_lo + 1
    if total <= 0:
        raise ValueError("no candidate state interval")

    t0 = n_lo * c - A
    _, rem = divmod(t0, a)
    e1_base = 0 if rem == 0 else a - rem
    s = c % a

    step = math.isqrt(total) + 1
    giant_count = (total + step - 1) // step
    giant_stride = (step * s) % a

    baby_pairs = sorted(((j * s) % a, j) for j in range(step))
    baby_values = [value for value, _ in baby_pairs]

    candidates = []
    seen = set()
    giant = e1_base
    for i in range(giant_count):
        for _, j in _values_in_circular_interval(
            baby_pairs, baby_values, a, giant, d
        ):
            offset = i * step + j
            if offset >= total:
                continue
            n = n_lo + offset
            t = n * c - A
            e1 = (A - n * c) % a
            e0 = (t + e1) // a
            if 0 <= e0 < d and e1 < d:
                k1 = d * r0 + e0
                outputs = generate_outputs(a, b, c, d, k1)
                if outputs[0] == r0 and outputs[1] == r1:
                    if target_prefix is None or digest_prefix(outputs) == target_prefix:
                        marker = tuple(outputs)
                        if marker not in seen:
                            seen.add(marker)
                            candidates.append(outputs)
        giant = (giant - giant_stride) % a

    if not candidates:
        raise ValueError("failed to recover a valid output sequence")
    if len(candidates) > 1:
        raise ValueError(f"recovered multiple candidates: {len(candidates)}")
    return candidates[0]


def recv_text(ws):
    message = ws.recv()
    if isinstance(message, bytes):
        return message.decode("utf-8", "replace")
    return message


def solve_remote(url):
    import websocket

    ws = websocket.create_connection(url, timeout=10)
    try:
        transcript = recv_text(ws)
        challenge = parse_challenge(transcript)
        outputs = recover_outputs(
            challenge.a,
            challenge.b,
            challenge.c,
            challenge.d,
            challenge.r0,
            challenge.r1,
            challenge.digest_prefix,
        )

        chunks = [transcript]
        for value in outputs:
            ws.send(f"{value:x}\n")
            reply = recv_text(ws)
            chunks.append(reply)
            if "Impressive!" in reply or "Nah" in reply:
                break
        return "".join(chunks)
    finally:
        ws.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="remote websocket challenge url")
    args = parser.parse_args()

    print(solve_remote(args.url), end="")


if __name__ == "__main__":
    main()
```

得到 flag：`ZJUCTF{Cr4cK_7rUnC4t3d_1c9_w1tH_4_l17tl3_b1t_0f_m4Th}`
