# 伏羲先天六十四卦 · 五行五音 Fuxi-64gua&Wu Xing (Five Elements)

> **A Sonification System translating I Ching Hexagrams into Five-Element Pentatonic Music** > 一套将《周易》六十四卦转化为五行五音的听觉生成系统

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## 📖 Introduction / 项目简介

This project explores the acoustic representation of the **I Ching (Book of Changes)**. By establishing a rigorous mapping system between the **Eight Trigrams (八卦)**, **Five Elements (五行)**, and the **Guqin Pentatonic Scale (古琴五音)**, we transform the visual symbols of the I Ching into mathematical musical structures.

The core goal is to audibly manifest the energy dynamics of the "Former Heaven" (Primal) state.

本项目探索《周易》的听觉化表达。通过建立**八卦-五行-古琴五音**之间的严谨映射体系，我们将易经的视觉符号转化为可计算的音乐结构，旨在以声音的形式呈现“先天”能量的流动与回响。

### 📅 Current Version: The Binary Sequence (v1.0)
**当前版本：二进制伏羲序列**

In this initial version, we organize the 64 Hexagrams using **Shao Yong's "Former Heaven" Sequence** (Strict Binary 0-63). This sequence represents the mathematical evolution of the cosmos from Stillness (0) to Fullness (63).
*Note: Future versions may explore different ordering logics based on sonic characteristics or philosophical meanings.*

在首个版本中，我们采用北宋理学家**邵雍**整理的**「伏羲先天六十四卦方圆图」**序列（即严格二进制 0-63）进行排列。该序列象征着宇宙从“混沌”（坤 0）到“鼎盛”（乾 63）的数理演化。
*注：本系统具有开放性，未来版本可能探索基于声音特质或义理的排序方式。*

---

## 🎵 Resources / 资源下载

* **📄 Score (Sheet Music):** 
* **🎹 MIDI / Audio:** 

---

## 🧮 Core Mapping Logic / 核心映射体系

The soul of this project lies in its translation rules. We do not compose melodies arbitrarily; we let the Hexagrams "speak" through their elemental properties.

本项目的灵魂在于其转译规则。我们不随意创作旋律，而是让卦象通过其五行属性“发声”。

### 1. From Trigram to Tone (从八卦到五音)

We map the Trigrams based on their **Wu Xing (Five Elements)** attributes to the traditional Chinese **Pentatonic Scale**.

我们根据八卦的**五行**属性，将其映射为中国传统**五声调式**：

| Trigram (八卦) | Element (五行) | Guqin Tone (古琴五音) | Number (简谱) |
| :--- | :--- | :--- | :--- |
| **Earth (土)** | Earth (土) | Gong (宫) | 1 |
| **Metal (金)** | Metal (金) | Shang (商) | 2 |
| **Wood (木)**  | Wood (木) | Jue (角) | 3 |
| **Fire (火)**  | Fire (火) | Zhi (徵) | 5 |
| **Water (水)** | Water (水) | Yu (羽) | 6 |

坤＝高音1，震＝高音3，乾＝高音2
其余（艮、坎、巽、离、兑）为“中音”八度：中1/中6/中3/中5/中2


### 2. The Binary Structure (二进制读取规则)

For computational accuracy, we define the Hexagram lines as binary bits:
为了计算的精确性，我们将爻定义为二进制位：

* **Yang (阳) = 1**
* **Yin (阴) = 0**
* **Reading Direction:** Bottom Line = Lowest Bit (Right); Top Line = Highest Bit (Left).
* **位序规则：** 初爻（最下）= 最低位；上爻（最上）= 最高位。

### 3. Hexagram as Dual-Tone (一卦双音结构)

Every Hexagram is composed of a Lower Trigram and an Upper Trigram. This creates a "Call and Response" structure.
每一卦由上下两个单卦组成，形成“呼与应”的双音结构。

* **Sequence:** Lower Trigram Sound → Upper Trigram Sound (自下而上，顺应卦气生长)
* **Octave Anchors (Structure):**
    * **High Octave:** Kun (坤), Zhen (震), Qian (乾) — The Pillars.
    * **Mid Octave:** Gen (艮), Kan (坎), Xun (巽), Li (离), Dui (兑) — The Flow.

---

## 📜 Philosophical Basis / 理论依据

> "The number of the Former Heaven springs from Kun to Qian... The order of the 64 hexagrams is derived from the expansion of the 8 trigrams based on numbers." — Shao Yong, *Huangji Jingshi Shu*

“先天之数，自坤至乾，皆得自然之数也……重之，则六十四卦之序，皆以数推之。” —— 邵雍《皇极经世书》

We respect this "Natural Number" (Binary) logic as the foundation for the structural integrity of the music, ensuring it aligns with the mathematical laws of the universe.

我们尊崇这一“自然之数”（二进制）逻辑，将其作为音乐结构的基石，以确保声音频率与宇宙数理的共振。

---

## ⚖️ License & Usage / 授权与使用说明

This project is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.
本项目采用 **知识共享署名 4.0 (CC BY 4.0)** 国际许可协议进行授权。

**You are free to / 您可以自由地：**
* Use this system for inspiration, modification, or commercial creation.
* 使用本系统寻找灵感、修改或进行商业创作。

**Under the following terms / 惟须遵守下列条件：**
* **Attribution (署名):** You must credit the original creator (**WinterQin / Annie**) in your work or documentation.
* **您必须在作品或文档中注明原作者（冬琴 / 星幻Annie），以此作为对灵感来源的尊重。**

---

### ✨ Acknowledgements

Dedicated to the ancient wisdom that encoded the universe into broken and unbroken lines.
致敬那将宇宙编码为阴阳爻画的古老智慧。