# quest-learning · 闯关式学习教练 Skill

把"教我从零学 X"变成一场通关游戏。AI 只出题、给道具、当裁判、记进度，**不给答案**。学员靠自己完成挑战来学会东西。

适用于 **Claude Code**、**Codex** 和 Claude（Cowork）。同一份 `SKILL.md` 三边通用。

## 它会做什么

1. **摸底**：问清终极目标、当前基础、可用资源、笔记放在哪
2. **画地图**：世界 → 关卡 → 任务。每关 4 个任务（基础 ×2、应用、挑战），每个世界最后一个 Boss 关
3. **出关**：每关生成一个带 `TODO` 的挑战文件，底部附**自动裁判**，加一篇关卡笔记（目标 / 任务 / 道具卡 / 通关记录）。出完题会先自测：空模板必须 0 分，参考解答必须满分
4. **验收**：学员说"通关了"，AI 会自己读代码、跑裁判。发现写法明显超出所学，就加一场**口试**
5. **三级提示**：方向 → 工具 → 只差最后一步，一次只给一级
6. **实时记录**：地图状态、当前位置、冒险日志、每关通关记录，都写进学员的笔记（比如 Obsidian）
7. **自适应**：远处的关卡只定主题，解锁时再按学员的表现细化

## 安装

```bash
git clone https://github.com/kulakeepor/claude-skill-quest-learning.git ~/.codex/skills/quest-learning

# Codex：上面这步就装好了（~/.codex/skills/）
# Claude Code：再建个软链接，两边共用一份
ln -s ~/.codex/skills/quest-learning ~/.claude/skills/quest-learning
```

以后更新：`cd ~/.codex/skills/quest-learning && git pull`

## 使用

直接说就行：

- "教我从零学 Python / 机器学习 / 吉他乐理，用闯关的方式"
- "0-3 通关了"
- "0-3 任务4 要提示"
- "继续下一关"

## 文件

```
SKILL.md                    # 主说明（流程、规则、坑）
templates/judge_template.py # 带自动裁判的挑战文件模板
templates/map.md            # 关卡地图模板
templates/level_note.md     # 关卡笔记模板
examples/level_0-3.py       # 真实关卡示例（"从 0 打造迷你大模型"世界 0）
```

## 来历

这个 skill 来自一次"零基础从 0 学会搭建大模型"的学习实践，玩法是学员和 Claude 在学习过程中一起摸索出来的。

## License

MIT
