#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 PPT 封面预览图（PNG）- 简化版
由于 PIL 6.2.2 不支持中文，使用英文占位
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_PNG = "/home/admin/.openclaw/workspace/ppt-output/01-cover-preview.png"
CHARACTER_IMAGE = "/home/admin/.openclaw/workspace/images/jinyin-character/04-cover-final.png"

# 颜色
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
WHITE = (255, 255, 255)

def main():
    # 创建 1920x1080 黑色背景
    img = Image.new('RGB', (1920, 1080), color=BLACK)
    draw = ImageDraw.Draw(img)
    
    # 使用默认字体（仅支持 ASCII）
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_footer = ImageFont.load_default()
    
    # 1. 标题 "JIN YIN Planet" - 金色（英文占位）
    title_text = "JIN YIN Planet"
    try:
        title_width, title_height = draw.textsize(title_text, font=font_title)
    except:
        title_width = 300
        title_height = 40
    title_x = (1920 - title_width) // 2
    title_y = 200
    draw.text((title_x, title_y), title_text, font=font_title, fill=GOLD)
    
    # 2. 副标题 - 白色（英文占位）
    subtitle_text = "One Person Group, AI Army"
    try:
        subtitle_width, _ = draw.textsize(subtitle_text, font=font_subtitle)
    except:
        subtitle_width = 350
    subtitle_x = (1920 - subtitle_width) // 2
    subtitle_y = 300
    draw.text((subtitle_x, subtitle_y), subtitle_text, font=font_subtitle, fill=WHITE)
    
    # 3. 底部小字 - 银色（英文占位）
    footer_text = "Let AI work for you, you just be the boss"
    try:
        footer_width, _ = draw.textsize(footer_text, font=font_footer)
    except:
        footer_width = 450
    footer_x = (1920 - footer_width) // 2
    footer_y = 400
    draw.text((footer_x, footer_y), footer_text, font=font_footer, fill=SILVER)
    
    # 4. 添加金银形象图片（如果存在）
    if os.path.exists(CHARACTER_IMAGE):
        try:
            character = Image.open(CHARACTER_IMAGE)
            # 调整大小
            character = character.resize((400, 400), Image.LANCZOS)
            # 放在右侧
            if character.mode == 'RGBA':
                img.paste(character, (1400, 150), character)
            else:
                img.paste(character, (1400, 150))
            print("✓ 已添加金银形象图片到预览")
        except Exception as e:
            print(f"⚠ 图片添加失败：{e}")
    
    # 添加说明文字
    note_text = "[PNG preview - Chinese text in PPTX file]"
    try:
        note_width, _ = draw.textsize(note_text, font=font_footer)
    except:
        note_width = 300
    note_x = (1920 - note_width) // 2
    draw.text((note_x, 500), note_text, font=font_footer, fill=SILVER)
    
    # 保存 PNG
    img.save(OUTPUT_PNG, 'PNG')
    print(f"✓ PNG 预览已保存：{OUTPUT_PNG}")
    print(f"  注：由于 PIL 版本限制，PNG 仅显示英文占位，中文文字在 PPTX 文件中")

if __name__ == "__main__":
    main()
