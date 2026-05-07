# fun-comate

不正经的 Comate Plugin —— 让编程不再无聊。

## 功能

### 1. 风格库系统 (`/cosplay`)

切换 Comate 的回答人格风格，支持 13 种人格：

**名人嘴替系列**: 马斯克、特朗普、孔子、李白、毛主席
**二次元系列**: 五条悟、路飞、艾伦
**风格流派系列**: 中二病、古风、暴躁老哥、甲方、心灵鸡汤

```
/cosplay musk        # 切换到马斯克模式
/cosplay confucius   # 切换到孔子模式
/cosplay off         # 恢复正常
/cosplay list        # 查看所有可用人格
```

### 2. 今日编程运势 (`/fortune`)

每日编程运势预测，包含宜忌、箴言、幸运语言、凶险时段。

```
/fortune           # 抽取今日运势
```

运势等级：大吉 → 吉 → 中吉 → 小吉 → 末吉 → 小凶 → 凶 → 大凶

### 3. 电影台词解释 Bug (`/movie-bug`)

用经典电影台词解读编程 Bug，覆盖空指针、死锁、内存泄漏、无限循环等常见 bug 类型。

```
/movie-bug NullPointerException       # 用电影台词解释空指针
/movie-bug 死锁 悲剧                   # 指定悲剧风格
```

### 4. 喘口气 (`/breather`)

连续写代码感到疲惫时，随机掉落一条反直觉冷知识或实时生成一张魔性图片（跳舞小火柴人、蹦迪柴犬、泡温泉水豚等），帮你切换状态。

```
/breather            # 随机（70% 冷知识 / 30% 图片）
/breather fact       # 强制冷知识
/breather image      # 强制生成图片
```

## 安装

```bash
# 克隆仓库到本地
git clone https://github.com/fanxin05/fun-comate.git

# 将插件目录放到你的项目中使用
cp -r fun-comate /path/to/your/project/.comate/plugins/
```

## 目录结构

```
fun-comate/
├── plugin.json       # Plugin 元数据描述文件
├── skills/           # Skill 组件
│   ├── breather/
│   ├── cosplay/
│   ├── fortune/
│   └── movie-bug/
└── README.md
```

## 作者

fanxin
