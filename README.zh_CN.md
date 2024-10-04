# Bangshow

![card_after_training](https://sprooc-pic.oss-cn-hangzhou.aliyuncs.com/pics/card_after_training.png)

**选择语言:**

- [English](README.md) / 中文

## 杂念

最近在折腾Linux桌面美化（是的，我闲得蛋疼），突然想整工具在终端放图片。我主要是想放邦多利的图，还要按乐队和成员来分类。试了好几个工具，结果都不太给力。最后发现还不如不如自己写一个。功能嘛确实很简陋，bug估计也不少，但反正自己用得开心就行哈哈。如果哪位邦友偶然看见了，欢迎试试看，有兴趣也可以来一起添点新功能。

## 概述

**Bangshow** 是一个命令行工具，用于在终端中显示 Bang Dream 图像。它提供了一种简单的方法来可视化您最喜欢的角色，并增强您的终端体验。

---

## 特性

- 直接在终端中显示 Bang Dream 角色的图像。
- 轻量级且易于使用。

---

## 准备

在开始之前，请确保您已安装以下内容：

- Python 3.x
- `chafa`（用于在终端中渲染图像。如果您尚未安装，可以使用 `install.sh` 脚本帮助您安装）

---

## 安装

1. **克隆仓库**：

   ```bash
   git clone https://github.com/sprooc/bangshow.git
   cd bangshow
   ```

2. **运行安装脚本**：

   执行以下命令以设置虚拟环境并安装所需的包：

   ```bash
   ./install.sh
   ```

   此脚本将：
   - 在 `~/.bangshow` 中创建一个虚拟环境。
   - 安装 `bangshow` 包。
   - 将 `bangshow` 可执行文件链接到 `/usr/bin`，使其可全局访问。

---

## 用法

要显示 Bang Dream 角色或乐队的图像，请使用以下命令格式：

```bash
bangshow [-h] [-u] [-s] [-d D] [-l] name [name ...]
```

### 描述

**Bang Dream 图像显示工具**

#### 位置参数:
- **name**: 要显示的乐队或角色名称。

#### 选项:
- `-h, --help`: 显示帮助信息并退出。
- `-u`: 更新图像。
- `-s`: 显示图像。
- `-d D`: 指定图像显示之间的延迟（以秒为单位）。
- `-l`: 循环播放图像。

---

### 示例

1. **显示角色**：  
   要显示名为 "Hina" 的角色的图像：

   ```bash
   bangshow Hina
   ```

2. **显示乐队**：  
   要显示乐队 "Poppin'Party" 的图像：

   ```bash
   bangshow "Poppin'Party"
   ```

3. **更新图像**：  
   要更新特定角色的图像：

   ```bash
   bangshow -u Hina
   ```

4. **以延迟显示图像**：  
   要以 2 秒的延迟显示 "Kasumi" 的图像：

   ```bash
   bangshow -d 2 Kasumi
   ```

5. **循环播放**：  
   要循环显示 "Ran" 的图像：

   ```bash
   bangshow -l Ran
   ```

6. **多个名称**：  
   要显示多个角色的图像：

   ```bash
   bangshow Hina Kasumi Rimi
   ```

---

## 选项

### 角色选项

| 角色       | 缩写                    |
|------------|-------------------------|
| Kasumi     | ksm, kasumi             |
| Tae        | tae                     |
| Rimi       | rimi                    |
| Saya       | saya, saaya             |
| Arisa      | arisa, ars              |
| Ran        | ran                     |
| Moca       | moca, moka              |
| Himari     | himari, hmr             |
| Tomoe      | tomoe                   |
| Tsugumi    | tsugumi, tsugu          |
| Kokoro     | kokoro, kkr             |
| Kaoru      | kaoru                   |
| Hagumi     | hagumi, hgm             |
| Kanon      | kanon                   |
| Misaki     | misaki, msk             |
| Aya        | aya                     |
| Hina       | hina                    |
| Chisato    | chisato                 |
| Maya       | maya                    |
| Eve        | eve                     |
| Yukina     | yukina, ykn             |
| Sayo       | sayo                    |
| Lisa       | lisa                    |
| Ako        | ako                     |
| Rinko      | rinko                   |
| Mashiro    | mashiro, msr            |
| Toko       | toko                    |
| Nanami     | nanami, nnm             |
| Tsukushi   | tsukushi, tks           |
| Rui        | rui                     |
| Rei        | rei, layer              |
| Rokka      | rokka, lock             |
| Masuki     | masuki, masking         |
| Reona      | reona, pareo            |
| Chiyu      | chiyu, chuchu, chu2     |
| Tomori     | tomori, tmr             |
| Anon       | anon                    |
| Rana       | rana                    |
| Soyo       | soyo                    |
| Taki       | taki, rikki             |

### 乐队选项

| 乐队               | 缩写                    |
|--------------------|-------------------------|
| Poppin'Party       | ppp                     |
| Afterglow          | ag                      |
| Pastel*Palettes    | PasPale, pp             |
| Roselia            | roselia, R              |
| Hello, Happy World!| hhw                     |
| Morfonica          | mofonica                |
| RAISE A SUILEN     | ras                     |
| MyGO!!!!!          | mygo                    |

---

## 致谢

本项目中使用的图像和材料来源于 [BestDori](https://bestdori.com/)。

---

## 许可证

本项目根据 MIT 许可证进行许可。有关详细信息，请参见 [LICENSE](LICENSE) 文件。

---

## 联系

如有任何问题或反馈，请联系 [1127626033@qq.com]。
