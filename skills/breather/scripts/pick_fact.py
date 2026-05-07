#!/usr/bin/env python3
"""
从 cold-facts.md 随机挑一条冷知识。

用法:
  python pick_fact.py
  python pick_fact.py --exclude 3,17,42        # 排除已展示过的序号
  python pick_fact.py --seed 1714000000        # 固定随机种子（调试用）

输出格式（stdout，两行）:
  INDEX\t实际冷知识文本
"""
import argparse
import random
import re
import sys
import time
from pathlib import Path

FACTS_FILE = Path(__file__).parent.parent / "references" / "cold-facts.md"


def load_facts(path: Path) -> list[str]:
    """从 Markdown 文件中解析冷知识条目，返回去除了列表标记的纯文本列表。"""
    facts = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- ") and len(stripped) > 10:
            facts.append(stripped[2:].strip())
    return facts


def main():
    """解析命令行参数，从冷知识库中随机挑选一条并输出。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--exclude", default="", help="逗号分隔的已用序号，如 3,17,42")
    parser.add_argument("--seed", type=int, default=None, help="随机种子（默认用当前时间戳）")
    args = parser.parse_args()

    facts = load_facts(FACTS_FILE)
    if not facts:
        print("ERROR: 冷知识库为空", file=sys.stderr)
        sys.exit(1)

    excluded = set()
    if args.exclude:
        for x in args.exclude.split(","):
            x = x.strip()
            if x.isdigit():
                excluded.add(int(x))

    candidates = [i for i in range(len(facts)) if i not in excluded]
    if not candidates:
        # 全部都展示过，重置
        candidates = list(range(len(facts)))

    seed = args.seed if args.seed is not None else int(time.time() * 1000)
    rng = random.Random(seed)
    idx = rng.choice(candidates)

    print(f"{idx}\t{facts[idx]}")


if __name__ == "__main__":
    main()
