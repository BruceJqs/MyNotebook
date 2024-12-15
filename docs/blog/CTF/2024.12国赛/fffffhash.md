# fffffhash

大胆猜测长度为 16 Byte，由于异或的可逆性，两边各搜索 8 Byte

下面这个脚本搜索中间值：

```cpp title="Solution1.cpp"
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <algorithm>

__attribute__((always_inline)) inline void fnv_forward(uint64_t *s, uint8_t c) {
	*s *= 0x0000000001000000000000000000013b;
	*s ^= c;
}
__attribute__((always_inline)) inline void fnv_backward(uint64_t *s,
                                                        uint8_t c) {
	*s ^= c;
	*s *= 0x6c62272e07bb014262b821756295c58d;
}
int main() {
	const size_t tbl_size = (1L << 32) * sizeof(uint64_t);

	uint64_t *tbl = (uint64_t *)malloc(tbl_size);
	uint64_t *tblend = tbl + (1L << 32);

	uint64_t start = 0x6c62272e07bb014262b821756295c58d;
	uint64_t end = 201431453607244229943761366749810895688;

	uint64_t *tblptr = tbl;
	for (uint8_t a = 0; a < 256; a++) {
		printf("a: %d\n", a);
		for (uint8_t b = 0; b < 256; b++) {
			for (uint8_t c = 0; c < 256; c++) {
				for (uint8_t d = 0; d < 256; d++) {
					uint64_t s = start;
					fnv_forward(&s, a);
					fnv_forward(&s, b);
					fnv_forward(&s, c);
					fnv_forward(&s, d);
					*tblptr = s;
					tblptr++;
					if (d == 255)
						break;
				}
				if (c == 255)
					break;
			}
			if (b == 255)
				break;
		}
		if (a == 255)
			break;
	}
	printf("done part 1\n");

	std::sort(tbl, tblend);
	printf("done sort\n");

	for (uint8_t a = 0; a < 256; a++) {
		printf("a: %d\n", a);
		for (uint8_t b = 0; b < 256; b++) {
			for (uint8_t c = 0; c < 256; c++) {
				for (uint8_t d = 0; d < 256; d++) {
					uint64_t s = end;
					fnv_backward(&s, a);
					fnv_backward(&s, b);
					fnv_backward(&s, c);
					fnv_backward(&s, d);
					uint64_t *f = std::lower_bound(tbl, tblend, s);
					if (f != tblend && *f == s) {
						printf("found %lx\n", s);
						printf("a: %d, b: %d, c: %d, d: %d\n", a, b, c, d);
					}
					if (d == 255)
						break;
				}
				if (c == 255)
					break;
			}
			if (b == 255)
				break;
		}
		if (a == 255)
			break;
	}
	return 0;
}
```

第二个脚本验证并得出答案

```cpp title="Solution2.cpp"
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <algorithm>

__attribute__((always_inline)) inline void fnv_forward(uint64_t *s, uint8_t c) {
	*s *= 0x0000000001000000000000000000013b;
	*s ^= c;
}
__attribute__((always_inline)) inline void fnv_backward(uint64_t *s,
                                                        uint8_t c) {
	*s ^= c;
	*s *= 0x6c62272e07bb014262b821756295c58d;
}
int main() {
	uint64_t start = 0x6c62272e07bb014262b821756295c58d;
	uint64_t end = 201431453607244229943761366749810895688;
	uint64_t target = 0x3631139703dd80a1315c10bab14ae2c6;
	for (uint8_t a = 0; a < 256; a++) {
		printf("a: %d\n", a);
		for (uint8_t b = 0; b < 256; b++) {
			for (uint8_t c = 0; c < 256; c++) {
				for (uint8_t d = 0; d < 256; d++) {
					uint64_t s = start;
					fnv_forward(&s, a);
					fnv_forward(&s, b);
					fnv_forward(&s, c);
					fnv_forward(&s, d);
					if (s == target) {
						printf("found %lx\n", s);
						printf("a: %d, b: %d, c: %d, d: %d\n", a, b, c, d);
					}
					if (d == 255)
						break;
				}
				if (c == 255)
					break;
			}
			if (b == 255)
				break;
		}
		if (a == 255)
			break;
	}
	printf("done\n");
	return 0;
}
```

得到最终解为 `020101081b04390001051a020a3d0f0f`

