# EmptyFlowMVP — 《空境漂流》MVP v0.1

《漂流少年》线稿+油彩手绘风格游戏的最小可玩原型。

## 快速开始

1. 安装 [Godot 4.2+](https://godotengine.org/download)
2. 打开 Godot，点击「导入」，选择本项目的 `project.godot`
3. 按 F5 运行

## 操作

- **WASD / 方向键**：移动角色
- **Enter**：在两个世界之间切换
- 走入发光区域触发彩蛋文字

## 项目结构

```
EmptyFlowMVP/
├─ project.godot          # 引擎配置（含输入映射）
├─ assets/
│  ├─ characters/
│  │  ├─ player_color.png # 角色油彩色彩层（占位图）
│  │  └─ player_line.png  # 角色独立线稿层（占位图）
│  └─ worlds/
│     ├─ world_a.png      # 世界A 油彩背景（占位图）
│     └─ world_b.png      # 世界B 油彩背景（占位图）
└─ scenes/
   ├─ player.gd           # 角色移动脚本
   ├─ player.tscn         # 角色预制体（双层Sprite分层渲染）
   ├─ trigger.gd          # 触发器彩蛋脚本
   ├─ global_switch.gd    # 世界切换脚本
   ├─ world_a.tscn        # 世界A场景
   └─ world_b.tscn        # 世界B场景
```

## 美术资产替换指南

当前 `assets/` 目录下为占位图。美术完成后按以下规则替换，**无需改动任何代码**：

1. **角色色彩层**：替换 `assets/characters/player_color.png`
   - 尺寸建议 2000×2000px，透明背景（Alpha通道）
   - 包含固有色 + 油彩肌理，不含黑色轮廓线

2. **角色线稿层**：替换 `assets/characters/player_line.png`
   - 尺寸建议 2000×2000px，透明背景（Alpha通道）
   - 仅纯黑色 #000000 轮廓线，无填充

3. **世界背景**：替换 `assets/worlds/world_a.png` 和 `world_b.png`
   - 尺寸建议 4000×2250px（16:9），不透明背景
   - 油彩手绘风格，不包含角色

> 替换后 Godot 会自动重新导入，无需修改场景文件。

## 核心技术点

- **分层渲染**：角色由两个 Sprite2D 叠加，color_sprite (z_index=0) + line_sprite (z_index=1)，保证线稿永远在油彩色彩之上，不被背景覆盖
- **CharacterBody2D**：Godot 4 原生移动节点，自带碰撞滑动
- **Area2D 触发器**：进入区域显示彩蛋文字，离开隐藏
- **场景切换**：`change_scene_to_file` 实现世界漂流跳转

## 验收清单

- [ ] WASD 控制角色移动
- [ ] 碰撞生效，角色不会穿出场景边界
- [ ] 角色线稿保持置顶，不会被背景覆盖
- [ ] 走入触发区域彩蛋文字显示，离开隐藏
- [ ] Enter 键在两个世界间切换
- [ ] 多次切换场景无崩溃
