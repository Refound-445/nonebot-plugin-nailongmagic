<!-- markdownlint-disable MD028 MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# Nonebot-Plugin-NaiLongMagic

_✨ 一个基于 AI 模型的简单插件~ ✨_

<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>

<br />

<a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/pyd-v1-or-v2.json" alt="Pydantic Version 1 Or 2" >
</a>
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/Refound-445/nonebot-plugin-nailongremove.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nailongremove">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-nailongremove.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nailongremove">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-nailongremove" alt="pypi download">
</a>

<br />

<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-nailongremove:nonebot_plugin_nailongremove">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-nailongremove" alt="NoneBot Registry">
</a>
<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-nailongremove:nonebot_plugin_nailongremove">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-nailongremove" alt="Supported Adapters">
</a>

</div>

## 📖 介绍

### 声明

本插件仅供娱乐和学习交流。

### 简介

世界就是一个巨大的奶龙~

### 技术
 
基于StableDiffusion模型，通过Lora微调训练而来

### 安装

以下提到的方法 任选**其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-nailongmagic
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-nailongmagic
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-nailongmagic
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-nailongmagic
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-nailongmagic
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_nailongmagic"
]
```

</details>

## ⚙️ 配置

在 nonebot2 项目的 `.env` 文件中添加下表中的必填配置

|               配置项                | 必填 |              默认值              |                                                                                                                说明                                                                                                                |
|:--------------------------------:|:--:|:-----------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|             **全局配置**             |    |                               |                                                                                                                                                                                                                                  |
|             `PROXY`              | 否  |            `None`             |                                                                                                         下载模型等文件时使用的代理地址                                                                                                          |
|             **响应配置**             |    |                               |                                                                                                                                                                                                                                  |
|  `NAILONGMAGIC_NEED_SUPERUSER`   | 否  |            `True`             |                                                                                                          是否只处理超级用户发送的图片                                                                                                          |
|    `NAILONGMAGIC_LIST_SCENES`    | 否  |             `[]`              |                                                                      聊天场景 ID 黑白名单列表<br />在单级聊天下为该聊天 ID，如 QQ 群号；<br />在多级聊天下为以 `_` 分割的各级聊天 ID，如频道下的子频道或频道下私聊                                                                      |
|     `NAILONGMAGIC_BLACKLIST`     | 否  |            `True`             |                                                                                                            是否使用黑名单模式                                                                                                             |
|  `NAILONGMAGIC_USER_BLACKLIST`   | 否  |             `[]`              |                                                                                                           用户 ID 黑名单列表                                                                                                            |
|     `NAILONGMAGIC_PRIORITY`      | 否  |             `100`             |                                                                                                           Matcher 优先级                                                                                                            |
|             **模型配置**             |    |                               |                                                                                                                                                                                                                                  |
|        `NAILONGMAGIC_TIP`        | 否  | `["奶龙已生成~{$checked_result}"]` |                                    发送的提示，使用 [Alconna 的消息模板](https://nonebot.dev/docs/best-practice/alconna/uniseg#%E4%BD%BF%E7%94%A8%E6%B6%88%E6%81%AF%E6%A8%A1%E6%9D%BF)，可用变量见下，随机发送列表其中一条消息                                    |
|      `NAILONGMAGIC_PROMPT`       | 否  |         `["nailong"]`         |                                                                                                          模型生成图片所使用的关键词                                                                                                           |
|     `NAILONGMAGIC_CACHE_DIR`     | 否  |     `./data/nailongmagic`     |                                                                                                             模型的下载位置                                                                                                              |
| `NAILONGMAGIC_AUTO_UPDATE_MODEL` | 否  |            `True`             |                                                                                                             是否自动更新模型                                                                                                             |
|     `NAILONGMAGIC_HF_TOKEN`      | 否  |            `None`             |                                                                                              GitHub Access Token，遇到模型下载或更新问题时可尝试填写                                                                                               |

### 消息模板可用变量

| 变量名            | 类型                                                                                                                         | 说明      |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |---------|
| `$event`          | [`Event`](https://nonebot.dev/docs/api/adapters/#Event)                                                                      | 当前事件    |
| `$target`         | [`Target`](https://nonebot.dev/docs/best-practice/alconna/uniseg#%E6%B6%88%E6%81%AF%E5%8F%91%E9%80%81%E5%AF%B9%E8%B1%A1)     | 事件目标    |
| `$message_id`     | `str`                                                                                                                        | 消息 ID   |
| `$msg`            | [`UniMessage`](https://nonebot.dev/docs/best-practice/alconna/uniseg#%E9%80%9A%E7%94%A8%E6%B6%88%E6%81%AF%E5%BA%8F%E5%88%97) | 当前消息    |
| `$ss`             | [`Session`](https://github.com/RF-Tar-Railt/nonebot-plugin-uninfo?tab=readme-ov-file#session)                                | 当前会话    |
| `$checked_result` | [`Image`](https://nonebot.dev/docs/best-practice/alconna/uniseg#%E9%80%9A%E7%94%A8%E6%B6%88%E6%81%AF%E6%AE%B5)               | 模型生成的图片 |

## 🎉 使用

发送“变奶龙+[咒语(可选，即prompt)]+图片”，等待时间后，即可收到bot返回消息，例如：`变奶龙nailong[图片]`，或者`变奶龙[图片]`

## 📞 联系

- [机器人插件学习交流群](https://qm.qq.com/q/o6x7IEZyO4)：200980266（安装部署，机器人 BUG 模型精度等问题反馈来这里哟）
- [插件性能测试群](https://qm.qq.com/q/7MMizTMMV2)：829463462（此群有已部署bot，可以测试当前已有模型的性能）
- [人工智能学习交流群](https://qm.qq.com/q/xdRGrt3y3C)：949992679（学习交流 AI 相关技术可以来这里捏）

欢迎大家进群一起学习交流~

## 📝 更新日志

### 1.0.0

- 创建了插件