---
name: movie-bug
description: 用经典电影台词来解读编程 Bug。当用户输入 /movie-bug、用电影解释 bug、电影台词、用电影解释报错、有趣地解释这个错误、搞笑解读 bug，或用户遇到 bug/报错并希望以趣味方式理解时使用此技能。也适用于用户说"这个报错好烦能不能有趣点"、"给我讲个故事解释这个错误"、"用通俗的方式解释这个异常"等场景。即使用户没有明确提到"电影"，只要有"趣味/有趣/搞笑 + 解释错误"的意图就应触发。
argument-hint: "[bug描述或错误信息] 可选风格: 悲剧/喜剧/动作/惊悚"
allowed-tools: [Read, Glob, Grep]
---

# 电影台词解释 Bug

用经典电影台词解读编程 Bug。分析用户遇到的错误类型，匹配最贴切的电影台词，给出趣味解读后附带正经修复建议。

**用户请求:** $ARGUMENTS

---

## 工作流程

1. 分析用户提供的 bug/错误信息，判断 bug 类型
2. 从 `references/movie-quotes.md` 读取对应电影台词映射
3. 如果用户指定风格（悲剧/喜剧/动作/惊悚），优先匹配该风格
4. 生成电影台词解读卡片
5. 在卡片末尾附上正经修复建议

## 输出格式

```
🎬 电影台词解读

Bug 类型: [bug类型名称]

---

> "[电影台词，融入用户实际代码的变量名/函数名]"
> —— 《电影名称》(年份)

---

【正经解法】
[具体的修复建议和代码示例]
```

## Bug 类型识别

根据错误信息关键词自动匹配 bug 类型：
- `null`, `undefined`, `NoneType`, `NullPointerException` → 空指针
- `deadlock`, `waiting for lock` → 死锁
- `memory`, `heap`, `OutOfMemory`, `leak` → 内存泄漏
- `infinite loop`, `maximum call stack`, `timed out` → 无限循环
- `StackOverflow`, `recursion`, `maximum recursion depth` → 栈溢出
- `race condition`, `concurrent`, `thread` → 并发竞态
- `TypeError`, `type mismatch`, `cannot convert` → 类型错误
- `legacy`, `old code`, `nobody knows` → 祖传屎山
- `works on my machine`, `环境`, `environment` → 环境问题

## 扩展玩法

### 代入用户代码的故事化解读
用用户真实的函数名/变量名编入电影剧情，增强代入感。
- 示例：如果用户的函数叫 `processOrder`，台词变为："你调用的那个 processOrder……从一开始就不存在。"

### 多台词模式
同一个 bug 提供2-3部电影的不同解读，让用户选择最喜欢的。

### 导演点评模式
不仅引用台词，还假装进行艺术分析：
> 这个 bug 的艺术性在于，它完美复现了《盗梦空间》中关于层级嵌套的哲学困境……

## 无匹配时的兜底

如果 bug 类型无法精确匹配，使用通用电影台词：
- 《阿甘正传》：*生活就像一盒巧克力，你永远不知道下一个 bug 是什么类型的。*
- 《终结者》：*I'll be back. —— 这个 bug 如是说。*
- 《指环王》：*One does not simply fix a bug in production.*
