# 魔性图片 Prompt 模板库

> 本文件用于给 `create-image` skill 提供 **prompt 起点**。触发时随机挑一个模板，再结合用户当前上下文微调（比如代码刚修的 bug 类型、当前技术栈、时间/季节等），然后送入图像生成。
>
> **尺寸约束**：统一使用 `1K` + 方形 `1:1` 构图，单主体居中，便于在 IDE 侧边栏以 `width="280"` 的缩略图呈现而不失真。
>
> **绝不要**生成具体真人（李小冉、蔡徐坤等），规避肖像权。统一使用卡通 / 3D Q 版 / 像素风 / 插画风。

---

## 模板列表（随机挑一个作为起点）

### 1. 抖腿鸽子
`A chubby cartoon pigeon standing on a computer keyboard, violently shaking its legs in a meme dance pose, exaggerated expression, bright neon background, sticker style, 3D render, square composition`

### 2. 蹦迪柴犬
`A cute shiba inu wearing sunglasses and a tiny disco headset, dancing on a table with rainbow disco ball in the background, tongue out, flat illustration, meme sticker style`

### 3. 泡温泉水豚
`A zen capybara soaking in a steaming hot spring, yellow rubber duck on its head, eyes half closed in bliss, soft watercolor illustration, cozy vibe, square composition`

### 4. 火柴人蹦迪
`A tiny stick figure character violently breakdancing in the center of a neon grid, motion blur trails, retro vaporwave background, minimal line art, absurd and chaotic energy`

### 5. This is fine 打工狗
`A cartoon dog wearing glasses, sitting calmly at a desk with a laptop, while the office around it is engulfed in orange flames, dog holds a coffee mug saying "this is fine", flat meme illustration style`

### 6. 戴 VR 头盔的熊猫
`A panda wearing a giant VR headset, flailing arms in mid-air in confusion, bamboo forest background replaced with glitching pixels, 3D Pixar style, funny expression`

### 7. 弹幕魔性章鱼
`A cute octopus in business attire holding 8 smartphones with each tentacle, each screen showing a different error message, googly eyes, minimal flat illustration, pastel colors`

### 8. 摸鱼仓鼠
`A tiny hamster lying flat on a keyboard pretending to be dead, sunglasses on, tropical drink next to it with umbrella, cartoon sticker style, bright colors, square`

### 9. bug 变蝴蝶
`A cute cartoon software bug with tiny antenna transforming into a beautiful neon butterfly, metamorphosis sequence, left-to-right progression, flat illustration, fantasy style`

### 10. 程序员僵尸
`A friendly zombie programmer hunched over a laptop at 3am, dark circles under eyes, glowing monitor light, speech bubble saying "just one more fix", cartoon illustration, square composition`

### 11. 小小工位
`A tiny 3D isometric cubicle scene with a small character dancing on the desk, sticky notes flying around, mechanical keyboard, mini plant, blender 3D render style, cozy aesthetic`

### 12. 抓狂 emoji 变体
`An exploding brain emoji character jumping out of a laptop screen, rainbow sparkles around, chibi style, sticker pack illustration, bright colors`

---

## 微调思路（结合上下文）

生成 prompt 时，根据用户刚刚的场景替换细节：

- 刚修空指针 bug → 让角色手里举着一张**空白的便利贴**，或键盘上写 `NULL`
- 刚完成性能优化 → 给角色加上**火箭尾焰**特效
- 在写前端 → 背景加 `<div>` 标签氛围
- 在写后端 → 背景加数据库柱状图 / K8s 集群积木
- 深夜（0-6 点）→ 场景加夜色、咖啡、月亮
- 周五完成 → 加鸡尾酒杯、彩带

## 调用示例

伪代码：

```
pick_template() → "抖腿鸽子"
context_tweak()  → 在 prompt 中追加 "holding a tiny note that says 'NullPointerException fixed'"
call_skill("create-image", prompt=final_prompt, size="1K", aspect_ratio="1:1")
```
