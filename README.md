# 伏羲先天六十四卦 · 五行五音  
# Fuxi 64 Hexagrams · Wu Xing Pentatonic

> **A Sonification System translating the Fuxi Earlier Heaven Hexagrams into Five-Element Pentatonic Music**  
> 一套将伏羲先天六十四卦转化为五行五音的听觉生成系统

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Creator / 创作者：WinterQin 冬琴（星幻Annie）**

---

## 📖 Introduction / 项目简介

This project explores the **acoustic representation** of the ancient Chinese Hexagram system. By establishing a mapping between the **Eight Trigrams (八卦)**, **Five Elements (五行)**, and the traditional **Guqin Pentatonic Scale (古琴五音)**, we transform visual symbols into audible musical structures.

The core goal is to manifest the energy dynamics of the "Former Heaven" (先天) cosmological state through sound.

本项目探索**伏羲先天六十四卦**的听觉化表达。通过建立**八卦-五行-古琴五音**之间的映射体系，我们将古老的卦象符号转化为可聆听的音乐结构，旨在以声音的形式呈现"先天"能量的流动与回响。

---

## 📋 Terminology Note / 术语说明

> **Important Clarification / 重要说明**  
>
> This project specifically adopts the **"Former Heaven" (先天) Hexagram Sequence**, traditionally attributed to the legendary sage **Fuxi (伏羲)**. This differs from the more commonly known **"Later Heaven" sequence** associated with **King Wen of Zhou (周文王)** and the *Zhou Yi (周易 / Book of Changes)*.
>
> The sequence we use is based on **Shao Yong's (邵雍, Song Dynasty) interpretation** of the Fuxi diagram, which aligns with a binary numerical progression (0-63). This interpretation was later studied by the German mathematician **Leibniz** in the 18th century.
>
> 本项目采用传说中**伏羲**所创的**「先天卦序」**，有别于**周文王**整理的**《周易》后天序**。  
> 我们使用的序列基于**宋代邵雍**对"伏羲先天图"的诠释，其排列与二进制数理（0-63）相合，后于18世纪为德国数学家**莱布尼茨**所研究。

---

## 🎵 Core Mapping / 核心映射规则

The soul of this project lies in its translation rules. We allow the Hexagrams to "speak" through their elemental properties.

本项目的灵魂在于其转译规则——让卦象通过五行属性"发声"。

### 1. Trigram → Element → Tone / 八卦 → 五行 → 五音

| Trigram 八卦 | Element 五行 | Tone 五音 | Number 简谱 |
|:---:|:---:|:---:|:---:|
| **Qian 乾☰** | Metal 金 | Shang 商 | 2' (High) |
| **Dui 兑☱** | Metal 金 | Shang 商 | 2 |
| **Zhen 震☳** | Wood 木 | Jue 角 | 3' (High) |
| **Xun 巽☴** | Wood 木 | Jue 角 | 3 |
| **Kan 坎☵** | Water 水 | Yu 羽 | 6 |
| **Li 离☲** | Fire 火 | Zhi 徵 | 5 |
| **Kun 坤☷** | Earth 土 | Gong 宫 | 1' (High) |
| **Gen 艮☶** | Earth 土 | Gong 宫 | 1 |

> **Sources / 依据**  
> - Trigram-Element correspondence: Zhouyi·Shuo Gua Zhuan (Commentary on the Trigrams, part of the I Ching) and the image-number Yijing & cosmological traditions of the Han Dynasty
> - Element-Tone correspondence: Core sources include Huangdi Neijing (Huangdi's Internal Classic) and Liji·Yueling (Book of Rites·Monthly Ordinances)
> - 八卦与五行的对应关系，核心源自《周易·说卦传》及汉代象数易学、宇宙论传统等
> - 五行与五音的对应关系，核心依据为《黄帝内经》《礼记·月令》等先秦两汉经典
---

### 2. Tuning System / 音律系统

We adopt the logic of the ancient Chinese Sanfen Sunyi (Three Parts Loss and Gain, 三分损益) tuning method (similar to but not identical with Pythagorean tuning), with Gong (宫) = 256 Hz as the fundamental pitch (a creative design choice, not a traditional fixed value).

下表频率借鉴于中国古代**三分损益律**逻辑的创意调整，系创作性设定，非传统三分损益律的精准计算值。，以 **宫音 = 256Hz** 为基准：

| Tone 音名 | Number 简谱 | Frequency 频率 |
|:---:|:---:|:---:|
| Gong 宫 | 1 | 256 Hz |
| Shang 商 | 2 | 288 Hz |
| Jue 角 | 3 | 324 Hz |
| Zhi 徵 | 5 | 384 Hz |
| Yu 羽 | 6 | 432 Hz |
| Gong' 高宫 | 1' | 512 Hz |
| Shang' 高商 | 2' | 576 Hz |
| Jue' 高角 | 3' | 648 Hz |

> **Note / 说明**  
> Traditional Guqin music emphasizes relative pitch relationships rather than fixed frequency standards. The choice of 256 Hz (Philosophical Pitch C4, distinct from modern concert pitch C4=261.63 Hz) is a creative design decision by the author, chosen for its mathematical elegance (2⁸) and because it places Yu (羽) at 432 Hz—a frequency some consider harmonious with natural resonance. 
> 传统古琴音乐注重相对音高关系，而非固定频率标准。本项目选取256Hz作为宫音基准（属哲学音高Philosophical Pitch范畴，区别于现代音乐会音高C4=261.63Hz），既取其数理之美（2⁸），也使羽音对应432Hz。

---

### 3. Dual-Tone Structure / 一卦双音结构

Each Hexagram consists of a **Lower Trigram** and an **Upper Trigram**, creating a "Call and Response" musical structure:

每一卦由**下卦**（内卦）与**上卦**（外卦）组成，形成"呼与应"的双音结构：

- **Sequence / 顺序**: Lower Trigram → Upper Trigram (following the natural growth of hexagram energy)  
  下卦音 → 上卦音（顺应卦气自下而上的生长）

- **Octave Anchors / 八度锚点** (Creative Design / 创作设计):
  - **High Octave 高八度**: Kun 坤, Zhen 震, Qian 乾 — representing structural pillars  
  - **Mid Octave 中八度**: Gen 艮, Kan 坎, Xun 巽, Li 离, Dui 兑 — representing flowing elements

---

### 4. Musical Meaning / 音乐意义

- 64 Hexagrams ≠ 64 single notes  
  六十四卦 ≠ 六十四个单音
- Rather, they form:  
  而是：
  - 64 **dual-tone units** / 六十四个**双音单元**
  - Earth / Heaven — 地 / 天
  - Root / Echo — 根 / 响
  - Inhale / Exhale — 呼吸 / 回应

These can be woven into melodies, rhythmic structures, or interactive audio installations.  
它们可以被串联为旋律、节奏结构或交互触发序列。

---

## 📜 Philosophical Basis / 理论依据

> *"The numbers of the Former Heaven arise naturally from Kun to Qian... The sequence of the 64 Hexagrams is derived through numerical expansion."*  
> — **Shao Yong**, *Huangji Jingshi Shu (皇极经世书)*

> "先天之数，自坤至乾，皆得自然之数也……重之，则六十四卦之序，皆以数推之。"  
> —— **邵雍**《皇极经世书》

We honor this "Natural Number" logic as the foundation for the structural integrity of the music, seeking resonance between sound frequencies and cosmic mathematics.

我们尊崇这一"自然之数"逻辑，将其作为音乐结构的基石，追求声音频率与宇宙数理的共振。

---


## 🎼 Future Directions / 可扩展方向

- Individual line interpretations → Rhythm / Rests / Sustain  
  六爻 → 节奏 / 留白 / 延音
- Hexagram transformations → Key changes / Range variations  
  卦变 → 转调 / 音域变化
- Five Elements generating/overcoming cycles → Harmonic structures  
  五行相生相克 → 和声结构
- Different timbres: Bianzhong bells, Xun flute, Guqin, Crystal bowls...  
  不同音色版本：编钟、埙、古琴、水晶音钵...

---

## ⚖️ License & Usage / 授权与使用

This project is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
本项目采用 **知识共享署名 4.0 (CC BY 4.0)** 国际许可协议。

**You are free to / 您可以自由地：**
- Use, share, adapt, or build upon this work for any purpose, including commercial use.  
  使用、分享、改编本作品，包括商业用途。

**Under the following terms / 惟须遵守：**
- **Attribution / 署名**: Please credit the original creator (**WinterQin / 冬琴 / 星幻Annie**) in your work or documentation.  
  请在您的作品或文档中注明原作者，以此作为对创作来源的尊重。

---

## 💬 Author's Note / 作者声明

The author's background is in **digital art and interactive media**, rather than traditional Yi Jing studies or musicology. This project represents a creative exploration at the intersection of ancient wisdom and modern technology.

While every effort has been made to respect traditional sources and maintain scholarly rigor, there may be interpretations or mappings that differ from established academic perspectives. **Feedback, corrections, and constructive suggestions from experts in Yi Jing studies, traditional Chinese music theory, or related fields are warmly welcomed.**

This work is offered in a spirit of open inquiry and cross-disciplinary dialogue.

作者主要从事**数字艺术与多媒体交互**领域的工作，并非易学或音乐学专业人士。本项目是一次将古老智慧与现代技术相结合的创意探索。其诠释与映射体系以艺术表达为核心，不代表传统易学/音乐学的权威解读。

尽管我们尽力尊重传统文献并保持学术严谨，但其中的诠释或映射方式可能与学界既有观点存在差异。**诚挚虚心欢迎易学、中国传统音乐理论或相关领域的专业人士提出宝贵意见、指正或建议，共同探讨和发掘古老智慧。**

---

## ✨ Acknowledgements / 致谢

Dedicated to the ancient wisdom that encoded the universe into broken and unbroken lines.  
致敬那将宇宙编码为阴阳爻画的古老智慧。

---



