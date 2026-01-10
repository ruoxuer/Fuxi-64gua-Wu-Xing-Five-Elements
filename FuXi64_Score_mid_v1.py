"""
Project: 伏羲先天八卦 · 六十四卦 · 简谱与MIDI生成器
Version: Score_v1 (基于邵雍先天图·二进制诠释)
Creator: 冬琴（星幻Annie）

功能：
    1. 生成 TXT 简谱歌词文件
    2. 生成 MIDI 文件

学术说明：
    - 采用"邵雍-莱布尼茨二进制序列"，非考古实证的"原始伏羲序"
    - 高八度规则为创作者本人的艺术设计想法，非传统规定

【八卦与五行五音映射转换规则】

五行转换：
    坤艮=土，乾兑=金，震巽=木，离=火，坎=水

五音转换：
    土=宫1，金=商2，木=角3，火=徵5，水=羽6

转换结果：
    坤＝高八度1，乾＝高八度2，震＝高八度3
    其余（艮、坎、巽、离、兑）为"中"八度：中1/中6/中3/中5/中2

频率说明：
    频率借鉴于中国古代**三分损益律**逻辑的创意调整，系创作性设定，非传统三分损益律的精准计算值。，以 **宫音 = 256Hz** 为基准：
"""

import os

try:
    from midiutil import MIDIFile
    HAS_MIDI = True
except ImportError:
    HAS_MIDI = False
    print("[!] 未安装 midiutil，无法生成MIDI文件")
    print("    请运行: pip install midiutil")

TEMPO_BPM = 60  # ♩= 60，每拍1秒
BEAT_DURATION = 60.0 / TEMPO_BPM

# 5/4拍，每小节2卦（4音）+ 1拍停顿
BEATS_PER_MEASURE = 5

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "qupu")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==========================================
# 八卦属性表 
# ==========================================
trigrams_data = {
    0: {"name": "坤", "element": "土", "tone_num": 1, "is_high": True},
    1: {"name": "艮", "element": "土", "tone_num": 1, "is_high": False},
    2: {"name": "坎", "element": "水", "tone_num": 6, "is_high": False},
    3: {"name": "巽", "element": "木", "tone_num": 3, "is_high": False},
    4: {"name": "震", "element": "木", "tone_num": 3, "is_high": True},
    5: {"name": "离", "element": "火", "tone_num": 5, "is_high": False},
    6: {"name": "兑", "element": "金", "tone_num": 2, "is_high": False},
    7: {"name": "乾", "element": "金", "tone_num": 2, "is_high": True},
}

# 六十四卦名表
hexagram_names = {
    (0,0): "坤", (0,1): "剥", (0,2): "比", (0,3): "观", 
    (0,4): "豫", (0,5): "晋", (0,6): "萃", (0,7): "否",
    (1,0): "谦", (1,1): "艮", (1,2): "蹇", (1,3): "渐", 
    (1,4): "小过", (1,5): "旅", (1,6): "咸", (1,7): "遁",
    (2,0): "师", (2,1): "蒙", (2,2): "坎", (2,3): "涣", 
    (2,4): "解", (2,5): "未济", (2,6): "困", (2,7): "讼",
    (3,0): "升", (3,1): "蛊", (3,2): "井", (3,3): "巽", 
    (3,4): "恒", (3,5): "鼎", (3,6): "大过", (3,7): "姤",
    (4,0): "复", (4,1): "颐", (4,2): "屯", (4,3): "益", 
    (4,4): "震", (4,5): "噬嗑", (4,6): "随", (4,7): "无妄",
    (5,0): "明夷", (5,1): "贲", (5,2): "既济", (5,3): "家人", 
    (5,4): "丰", (5,5): "离", (5,6): "革", (5,7): "同人",
    (6,0): "临", (6,1): "损", (6,2): "节", (6,3): "中孚", 
    (6,4): "归妹", (6,5): "睽", (6,6): "兑", (6,7): "履",
    (7,0): "泰", (7,1): "大畜", (7,2): "需", (7,3): "小畜", 
    (7,4): "大壮", (7,5): "大有", (7,6): "夬", (7,7): "乾"
}

# MIDI音符映射（基于256Hz = C4 = 60）
midi_notes = {
    "Mid_1": 60,   # 宫 C4
    "Mid_2": 62,   # 商 D4
    "Mid_3": 64,   # 角 E4
    "Mid_5": 67,   # 徵 G4
    "Mid_6": 69,   # 羽 A4
    "High_1": 72,  # 高宫 C5
    "High_2": 74,  # 高商 D5
    "High_3": 76,  # 高角 E5
}

# 简谱符号映射
jianpu_symbols = {
    "Mid_1": "1",
    "Mid_2": "2",
    "Mid_3": "3",
    "Mid_5": "5",
    "Mid_6": "6",
    "High_1": "1'",
    "High_2": "2'",
    "High_3": "3'",
}

def get_hexagram_info(i):
    table_upper_val = (i >> 3) & 0b111
    table_lower_val = i & 0b111
    
    # 设置卦象从下往上读的顺序
    actual_lower_val = table_upper_val
    actual_upper_val = table_lower_val
    
    actual_low_attr = trigrams_data[actual_lower_val]
    actual_up_attr = trigrams_data[actual_upper_val]
    
    hex_name = hexagram_names.get((table_upper_val, table_lower_val), "未知")
    
    key_low = f"{'High' if actual_low_attr['is_high'] else 'Mid'}_{actual_low_attr['tone_num']}"
    key_up = f"{'High' if actual_up_attr['is_high'] else 'Mid'}_{actual_up_attr['tone_num']}"
    
    return {
        "index": i,
        "hex_name": hex_name,
        "binary": f"{i:06b}",
        "actual_lower": actual_low_attr['name'],
        "actual_upper": actual_up_attr['name'],
        "key_low": key_low,
        "key_up": key_up,
        "jianpu_low": jianpu_symbols[key_low],
        "jianpu_up": jianpu_symbols[key_up],
    }

# 生成简谱TXT
def generate_score_txt(output_path):
    """生成简谱歌词文件"""
    
    lines = []
    lines.append("=" * 60)
    lines.append("  伏伏羲八卦五音 · 先天回响-五行五音可视化v1 · 简谱")
    lines.append("  (基于邵雍先天图·二进制诠释)")
    lines.append("  创作者: 冬琴（星幻Annie）")
    lines.append("=" * 60)
    lines.append("")
    lines.append("【学术说明】")
    lines.append("  - 采用「邵雍-莱布尼茨二进制序列」")
    lines.append("  - 八卦与五行的对应关系，核心源自《周易·说卦传》及汉代象数易学、宇宙论传统等")
    lines.append("  - 五行与五音的对应关系，核心依据为《黄帝内经》《礼记·月令》等先秦两汉经典")
    lines.append("  - 高八度规则为创作者个人创作的艺术设计，非权威标准")
    lines.append("")
    lines.append("【八卦与五行五音映射转换规则】")
    lines.append("")
    lines.append("五行转换:")
    lines.append("  坤艮=土，乾兑=金，震巽=木，离=火，坎=水")
    lines.append("")
    lines.append("五音转换:")
    lines.append("  土=宫1，金=商2，木=角3，火=徵5，水=羽6")
    lines.append("")
    lines.append("转换结果:")
    lines.append("  坤＝高八度1，乾＝高八度2，震＝高八度3")
    lines.append("  其余（艮、坎、巽、离、兑）为中八度：中1/中6/中3/中5/中2")
    lines.append("")
    lines.append("-" * 60)
    lines.append("")
    lines.append("调式: 三分损益律 (宫=256Hz，羽=432Hz)")
    lines.append("拍号: 5/4")
    lines.append(f"速度: {TEMPO_BPM} BPM")
    lines.append("")
    lines.append("音符设计:")
    lines.append("  1=宫(256Hz)  2=商(288Hz)  3=角(324Hz)")
    lines.append("  5=徵(384Hz)  6=羽(432Hz)")
    lines.append("  1'=高宫(512Hz)  2'=高商(576Hz)  3'=高角(648Hz)")
    lines.append("")
    lines.append("节奏说明:")
    lines.append("  每小节5拍: 下卦音(1拍) 上卦音(1拍) 下卦音(1拍) 上卦音(1拍) 休止(1拍)")
    lines.append("  | 表示小节线")
    lines.append("  0 表示休止符")
    lines.append("")
    lines.append("-" * 60)
    lines.append("简谱:")
    lines.append("-" * 60)
    lines.append("")
    
    # 按每行2小节（4卦）排列
    measure_count = 0
    current_line_notes = []
    current_line_names = []
    
    for i in range(64):
        info = get_hexagram_info(i)
        
        # 添加卦名和音符
        current_line_names.append(f"{info['hex_name']}")
        current_line_notes.append(f"{info['jianpu_low']} {info['jianpu_up']}")
        
        # 每2卦一小节
        if (i + 1) % 2 == 0:
            measure_count += 1
            current_line_notes.append("0 |")  # 休止+小节线
            
            # 每4卦（2小节）换行
            if measure_count % 2 == 0:
                # 卦名行
                name_line = "  "
                for j, name in enumerate(current_line_names):
                    name_line += f"{name:^8s}"
                lines.append(name_line)
                
                # 音符行
                note_line = "  "
                for j, note in enumerate(current_line_notes):
                    note_line += f"{note:^8s}"
                lines.append(note_line)
                lines.append("")
                
                current_line_notes = []
                current_line_names = []
    
    # 处理剩余
    if current_line_notes:
        name_line = "  "
        for name in current_line_names:
            name_line += f"{name:^8s}"
        lines.append(name_line)
        
        note_line = "  "
        for note in current_line_notes:
            note_line += f"{note:^8s}"
        lines.append(note_line)
    
    lines.append("")
    lines.append("-" * 60)
    lines.append("详细卦序表:")
    lines.append("-" * 60)
    lines.append("")
    lines.append("卦序  卦名    二进制    下卦  上卦    简谱")
    lines.append("-" * 50)
    
    for i in range(64):
        info = get_hexagram_info(i)
        lines.append(
            f"{i:3d}   {info['hex_name']:4s}    {info['binary']}    "
            f"{info['actual_lower']:2s}    {info['actual_upper']:2s}      "
            f"{info['jianpu_low']:>2s} {info['jianpu_up']:<2s}"
        )
    
    lines.append("")
    lines.append("=" * 60)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    return output_path

# 生成MIDI
def generate_midi(output_path):
    """生成MIDI文件"""
    if not HAS_MIDI:
        return None
    
    midi = MIDIFile(1)
    track = 0
    channel = 0
    volume = 80
    
    midi.addTempo(track, 0, TEMPO_BPM)
    midi.addProgramChange(track, channel, 0, 14)  # Tubular Bells (编钟近似)
    
    current_beat = 0
    note_duration = 1.0  # 每音1拍
    
    for i in range(64):
        info = get_hexagram_info(i)
        
        # 下卦音
        pitch_low = midi_notes[info['key_low']]
        midi.addNote(track, channel, pitch_low, current_beat, note_duration * 1.5, volume)
        current_beat += 1
        
        # 上卦音
        pitch_up = midi_notes[info['key_up']]
        midi.addNote(track, channel, pitch_up, current_beat, note_duration * 1.5, volume)
        current_beat += 1
        
        # 每2卦加1拍休止
        if (i + 1) % 2 == 0:
            current_beat += 1
    
    with open(output_path, 'wb') as f:
        midi.writeFile(f)
    
    return output_path

# 主程序
def main():
    print("=" * 60)
    print("  伏羲八卦五音 · 先天回响-五行五音可视化- 简谱与MIDI生成器 v1")
    print("=" * 60)
    print()
    
    # 验证前8卦
    print("  前8卦验证:")
    print("  " + "-" * 50)
    for i in range(8):
        info = get_hexagram_info(i)
        print(f"  {i}: {info['hex_name']:4s} 下:{info['actual_lower']} 上:{info['actual_upper']} "
              f"简谱: {info['jianpu_low']} {info['jianpu_up']}")
    print("  " + "-" * 50)
    print()
    
    # 生成简谱TXT
    txt_path = os.path.join(OUTPUT_DIR, "伏羲八卦五音 · 先天回响-五行五音可视化-简谱-v1.txt")
    generate_score_txt(txt_path)
    print(f"  简谱TXT: {txt_path}")
    
    # 生成MIDI
    if HAS_MIDI:
        midi_path = os.path.join(OUTPUT_DIR, "伏羲八卦五音 · 先天回响-五行五音可视化-MIDI-v1.mid")
        generate_midi(midi_path)
        print(f"  MIDI: {midi_path}")
    else:
        print("  MIDI: 跳过 (需安装 midiutil)")
    
    print()
    print("=" * 60)
    print("  生成完毕!")
    print("=" * 60)

if __name__ == "__main__":
    main()

