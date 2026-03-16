#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
金银 Planet PPT 封面 - 王家卫风格
生成电影海报质感的封面图片
"""

from PIL import Image, ImageDraw, ImageFilter
import random

# 创建 1920x1080 的画布
width, height = 1920, 1080
img = Image.new('RGB', (width, height), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

# 1. 绘制深空渐变背景（蓝绿调 - 王家卫《重庆森林》风格）
for y in range(height):
    r = int(10 + 20 * (y / height))
    g = int(14 + 30 * (y / height))
    b = int(26 + 40 * (1 - y / height))
    
    if y < height // 2:
        g = int(g * 1.2)
    else:
        b = int(b * 1.3)
    
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# 2. 绘制光斑效果
def draw_bokeh(draw, cx, cy, radius, color, alpha=80):
    for r in range(radius, 0, -5):
        a = int(alpha * (1 - r / radius))
        if a > 0:
            draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(color[0], color[1], color[2], a))

bokeh_colors = [(26, 74, 90), (42, 90, 74), (58, 74, 106), (74, 58, 90)]
bokeh_positions = [(300, 150, 150), (1600, 500, 200), (600, 800, 125), (1200, 300, 100)]

for i, (cx, cy, r) in enumerate(bokeh_positions):
    color = bokeh_colors[i % len(bokeh_colors)]
    for _ in range(3):
        offset_x = random.randint(-20, 20)
        offset_y = random.randint(-20, 20)
        draw_bokeh(draw, cx+offset_x, cy+offset_y, r, color, 40)

# 3. 绘制雨丝效果
for _ in range(200):
    x = random.randint(0, width)
    y = random.randint(0, height)
    length = random.randint(20, 50)
    alpha = random.randint(30, 60)
    draw.line([(x, y), (x, y+length)], fill=(alpha+150, alpha+150, alpha+170))

# 4. 添加胶片颗粒
pixels = img.load()
for x in range(0, width, 3):
    for y in range(0, height, 3):
        if random.random() < 0.15:
            noise = random.randint(-20, 20)
            try:
                old = pixels[x, y]
                pixels[x, y] = (
                    max(0, min(255, old[0] + noise)),
                    max(0, min(255, old[1] + noise)),
                    max(0, min(255, old[2] + noise))
                )
            except:
                pass

# 5. 添加暗角
for r in range(300, 0, -10):
    alpha = int(150 * (1 - r / 300))
    draw.ellipse([width//2-r, height//2-r, width//2+r, height//2+r], 
                 fill=(0, 0, 0, alpha))

# 6. 绘制装饰线条（顶部和底部）
draw.line([(width//2, 30), (width//2, 150)], fill=(100, 100, 100), width=1)
draw.line([(width//2, height-30), (width//2, height-150)], fill=(100, 100, 100), width=1)

# 7. 文字（由于没有中文字体，用英文占位，用户可以在 PPT 里替换）
# 主标题
title = "JIN YIN PLANET"
title_x = width // 2
title_y = height // 2 - 40

# 发光效果
for offset in [4, 3, 2, 1]:
    draw.text((title_x-200-offset, title_y-50), title, fill=(255, 200, 50))
    draw.text((title_x+200-offset, title_y-50), title, fill=(255, 200, 50))

# 主标题 - 金色
try:
    font_large = ImageFont.load_default()
except:
    font_large = None

draw.text((title_x-180, title_y-40), title, fill=(255, 215, 0))

# 副标题
subtitle = "One Person · Twenty-Two AIs · One Planet"
draw.text((title_x-250, title_y+50), subtitle, fill=(180, 180, 180))

# 底部文字
footer1 = "March 16, 2026 · Chongqing"
footer2 = "22 AIs working for you"
draw.text((title_x-150, height-120), footer1, fill=(150, 150, 150))
draw.text((title_x-120, height-90), footer2, fill=(120, 120, 120))

# 8. 保存
img = img.convert('RGB')
img.save('/home/admin/.openclaw/workspace/ppt-output/01-cover-wkh.png', 'PNG')
print("✅ 封面已生成：/home/admin/.openclaw/workspace/ppt-output/01-cover-wkh.png")

img.save('/home/admin/.openclaw/workspace/ppt-output/01-cover-wkh.jpg', 'JPEG', quality=90)
print("✅ JPEG 版本：/home/admin/.openclaw/workspace/ppt-output/01-cover-wkh.jpg")
