# 伏羲先天八卦 · 六十四卦 · 五行五音 / Fuxi's Innate Bagua · 64 Hexagrams · Five Elements and Five Tones

> 一套将伏羲先天序排列的六十四卦转化为五行五音的听觉生成系统 / A system that translates the 64 Hexagrams, arranged according to Fuxi's Innate Sequence, into an auditory generation based on the Five Elements and Five Tones.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Creator / 创作者：DongQin 冬琴（星幻Annie）**

![伏羲八卦五音 · 先天回响-五行五音可视化v1](https://raw.githubusercontent.com/ruoxuer/Fuxi-64gua-Wu-Xing-Five-Elements/main/伏羲八卦五音%20·%20先天回响-五行五音可视化v1.png)

---

## 📖 Introduction / 项目简介

本创作当前曲谱采用传说中伏羲所创的「先天卦序」，使用的序列基于宋代邵雍对"伏羲先天图"的诠释，其排列与二进制数理（0-63）相合，刚好在64 个数学上呈现完美的声学结构。

/ The musical score for this creation adopts the 'Innate Hexagram Sequence' (Xiantian Gua Xu), traditionally attributed to Fuxi. The sequence used is based on the Song Dynasty scholar Shao Yong's interpretation of the "Fuxi Innate Diagram," whose arrangement aligns with binary mathematics (0-63), presenting a perfect acoustic structure across the 64 mathematical positions.

结合古琴五音体系与声学谐振逻辑，将伏羲先天卦的六十四种阴阳五行能量状态，转译为可听见的物理振动（即五音旋律），每一个卦象对应一组特定的双音结构（下卦+上卦各一个音）。

/ Combining the Guqin's Five-Tone (Wu Yin) system with the logic of acoustic resonance, the sixty-four states of Yin-Yang and Five Elements energy from Fuxi's Innate Hexagrams are translated into audible physical vibrations (i.e., Five-Tone melodies). Each hexagram corresponds to a specific dual-tone structure (one tone for the Lower Trigram and one for the Upper Trigram).

在伏羲的先天宇宙里，没有吉凶，只有能量的阴阳呼吸。愿听者的身心仿佛走完一次完整的宇宙能量循环。也许，通过声波的有序干涉，能让混乱的身心频率能回归数理的和谐。

/ In Fuxi's innate cosmos, there is no good or bad fortune, only the Yin-Yang breathing of energy. May the listener's body and mind feel as though they have completed a full cycle of cosmic energy. Perhaps, through the ordered interference of sound waves, chaotic physical and mental frequencies can return to the harmony of mathematics.

---

## 🎵 Core Mapping / 核心映射规则

The soul of this project lies in its translation rules. We allow the Hexagrams to "speak" through their elemental properties.

/ 本项目的灵魂在于其转译规则——让卦象通过五行属性"发声"。

### 1. Trigram → Element → Tone / 八卦 → 五行 → 五音

| Trigram 八卦 | Element 五行 | Tone 五音 | Number 简谱 |
| :---: | :---: | :---: | :---: |
| **Qian 乾☰** | Metal 金 | Shang 商 | 2' (High) |
| **Dui 兑☱** | Metal 金 | Shang 商 | 2 |
| **Zhen 震☳** | Wood 木 | Jue 角 | 3' (High) |
| **Xun 巽☴** | Wood 木 | Jue 角 | 3 |
| **Kan 坎☵** | Water 水 | Yu 羽 | 6 |
| **Li 离☲** | Fire 火 | Zhi 徵 | 5 |
| **Kun 坤☷** | Earth 土 | Gong 宫 | 1' (High) |
| **Gen 艮☶** | Earth 土 | Gong 宫 | 1 |

> **Sources / 依据**
>
> - Trigram-Element correspondence: Zhouyi·Shuo Gua Zhuan (Commentary on the Trigrams, part of the I Ching) and the image-number Yijing & cosmological traditions of the Han Dynasty
> - 八卦与五行的对应关系，核心源自《周易·说卦传》及汉代象数易学、宇宙论传统等
> - Element-Tone correspondence: Core sources include Huangdi Neijing (Huangdi's Internal Classic) and Liji·Yueling (Book of Rites·Monthly Ordinances)
> - 五行与五音的对应关系，核心依据为《黄帝内经》《礼记·月令》等先秦两汉经典

---

### 2. Tuning System / 音律系统

We adopt the logic of the ancient Chinese Sanfen Sunyi (Three Parts Loss and Gain, 三分损益) tuning method (similar to but not identical with Pythagorean tuning), with Gong (宫) = 256 Hz as the fundamental pitch (a creative design choice, not a traditional fixed value).

/ 下表频率借鉴于中国古代**三分损益律**逻辑作了如下创意调整，系创作性设定，非传统三分损益律的精准计算值。以 **宫音 = 256Hz** 为基准：

| Tone 音名 | Number 简谱 | Frequency 频率 |
| :---: | :---: | :---: |
| Gong 宫 | 1 | 256 Hz |
| Shang 商 | 2 | 288 Hz |
| Jue 角 | 3 | 324 Hz |
| Zhi 徵 | 5 | 384 Hz |
| Yu 羽 | 6 | 432 Hz |
| Gong' 高宫 | 1' | 512 Hz |
| Shang' 高商 | 2' | 576 Hz |
| Jue' 高角 | 3' | 648 Hz |

> **Note / 说明**
>
> Traditional Guqin music emphasizes relative pitch relationships rather than fixed frequency standards. The choice of 256 Hz (Philosophical Pitch C4, distinct from modern concert pitch C4=261.63 Hz) is a creative design decision by the author, chosen for its mathematical elegance (2⁸) and because it places Yu (羽) at 432 Hz—a frequency some consider harmonious with natural resonance.
>
> / 传统古琴音乐注重相对音高关系，而非固定频率标准。本项目选取256Hz作为宫音基准（属哲学音高Philosophical Pitch范畴，区别于现代音乐会音高C4=261.63Hz），既取其数理之美（2⁸），也使羽音对应432Hz。

---

### 3. Dual-Tone Structure / 一卦双音结构

Each Hexagram consists of a **Lower Trigram** and an **Upper Trigram**, creating a "Call and Response" musical structure:

/ 每一卦由**下卦**（内卦）与**上卦**（外卦）组成，形成"呼与应"的双音结构：

- **Sequence / 顺序**: Lower Trigram → Upper Trigram (following the natural growth of hexagram energy)
  / 下卦音 → 上卦音（顺应卦气自下而上的生长）

- **Octave Anchors / 八度锚点** (Creative Design / 创作设计):
  - **High Octave 高八度**: Kun 坤, Zhen 震, Qian 乾 — representing structural pillars
  - **Mid Octave 中八度**: Gen 艮, Kan 坎, Xun 巽, Li 离, Dui 兑 — representing flowing elements

---

### 4. Musical Meaning / 音乐意义

- 64 Hexagrams ≠ 64 single notes
  / 六十四卦 ≠ 六十四个单音
- Rather, they form:
  / 而是：
  - 64 **dual-tone units** / 六十四个**双音单元**
  - Earth / Heaven — 地 / 天
  - Root / Echo — 根 / 响
  - Inhale / Exhale — 呼吸 / 回应

These can be woven into melodies, rhythmic structures, or interactive audio installations.

/ 它们可以被串联为旋律、节奏结构或交互触发序列。

---
### 5. python files

/ 本项目包含一个 Python 脚本，用于将核心映射规则程序化，实现自动化乐谱生成。
/ This project includes a Python script to programmatically implement the core mapping rules and automatically generate musical scores.

FuXi64_Score_mid_v1.py,  简谱与 MIDI 生成器 / Score and MIDI Generator

该 Python 脚本 (需安装 midiutil 库) 能够将六十四卦的映射规则自动生成以下文件：
/ This Python script (requires the midiutil library) automatically generates the following files based on the 64 Hexagram mapping rules:

TXT 格式简谱 / TXT Format Jianpu (Numbered Score)：包含完整的 64 卦序列、卦名、下上卦的五音简谱对应，以及详细的音律说明。

MIDI 文件 / MIDI File：可直接在任何音乐软件中打开和播放。当前音色默认为编钟近似（Tubular Bells），速度设定为 60 BPM。

如何在本地运行脚本 (How to Run the Script Locally)
pip install midiutil
python FuXi64_Score_mid_v1.py



An interactive web version visualizing the correspondence of the 64 Hexagrams to the Five Elements and Five Tones has also been created. Click the link to access it:

/ 顺便也做了网页版的六十四卦对应五行五音的可视化交互程序，点击链接即可访问：

https://www.xinghuanlab.com/Annie/dao/fuxi64

---

## 🎼 Future Directions / 可扩展方向

- Individual line interpretations → Rhythm / Rests / Sustain
  / 六爻 → 节奏 / 留白 / 延音
- Hexagram transformations → Key changes / Range variations
  / 卦变 → 转调 / 音域变化
- Five Elements generating/overcoming cycles → Harmonic structures
  / 五行相生相克 → 和声结构
- Different timbres: Bianzhong bells, Xun flute, Guqin, Crystal bowls...
  / 不同音色版本：编钟、埙、古琴、水晶音钵...

---

## ⚖️ License & Usage / 授权与使用

This project is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

/ 本项目采用 **知识共享署名 4.0 (CC BY 4.0)** 国际许可协议。

**You are free to / 您可以自由地：**

- Use, share, adapt, or build upon this work for any purpose, including commercial use.
  / 使用、分享、改编本作品，包括商业用途。

**Under the following terms / 惟须遵守：**

- **Attribution / 署名**: Please credit the original creator (**DongQin / 冬琴 / 星幻Annie**) in your work or documentation.
  / 请在您的作品或文档中注明原作者，以此作为对创作来源的尊重。

---

## 💬 Author's Note / 作者声明

The author's background is in **digital art and interactive media**, rather than traditional Yi Jing studies or musicology. This project represents a creative exploration at the intersection of ancient wisdom and modern technology.

/ 作者主要从事**数字艺术与多媒体交互**领域的工作，并非易学或音乐学专业人士。本项目是一次将古老智慧与现代技术相结合的创意探索。其诠释与映射体系以艺术表达为核心，不代表传统易学/音乐学权威解读。

While every effort has been made to respect traditional sources and maintain scholarly rigor, there may be interpretations or mappings that differ from established academic perspectives. **Feedback, corrections, and constructive suggestions from experts in Yi Jing studies, traditional Chinese music theory, or related fields are warmly welcomed.**

/ 尽管我们尽力尊重传统文献并保持学术严谨，但其中的诠释或映射方式可能与学界既有观点存在差异。**诚挚虚心欢迎易学、中国传统音乐理论或相关领域的专业人士提出宝贵意见、指正或建议，共同探讨和发掘古老智慧。**

This work is offered in a spirit of open inquiry and cross-disciplinary dialogue.

/ 本作品以开放探究和跨学科对话的精神提供。

---

## ✨ Acknowledgements / 致谢

Dedicated to the ancient wisdom that encoded the universe into broken and unbroken lines.

/ 致敬那将宇宙编码为阴阳爻画的古老智慧。

---