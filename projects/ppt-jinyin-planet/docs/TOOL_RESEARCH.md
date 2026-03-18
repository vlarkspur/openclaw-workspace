# PPT 设计工具调研报告

## 工具对比分析

### 1. Python 方案

| 工具 | 优势 | 劣势 | 适用场景 |
|------|------|------|----------|
| **python-pptx** | 直接生成.pptx，兼容性好 | 不支持渐变/阴影/高级效果 | 简单商务 PPT |
| **Pillow + reportlab** | 图像处理强，可生成 PDF | 不是真正的 PPT，交互性差 | 静态封面 |
| **CairoSVG** | 矢量图形，支持渐变 | 学习曲线陡，文档少 | 矢量设计 |

**结论：** Python 原生库功能有限，难以实现专业级效果

---

### 2. 在线工具 API

| 工具 | 优势 | 劣势 | 适用场景 |
|------|------|------|----------|
| **Canva API** | 模板丰富，效果专业 | 需付费，API 限制多 | 批量生产 |
| **Google Slides API** | 免费，协作方便 | 效果一般，需网络 | 团队协作文档 |

**结论：** 依赖外部服务，不适合本地化部署

---

### 3. HTML/CSS + 转 PNG/PDF ⭐ **推荐**

**优势：**
- ✅ CSS 支持高级渐变（线性、径向、锥形）
- ✅ 滤镜效果（blur, drop-shadow, opacity）
- ✅ 混合模式（multiply, screen, overlay）
- ✅ 动画和光效（box-shadow, text-shadow）
- ✅ 完全可控，本地执行
- ✅ 可用 Puppeteer/Playwright 转 PNG/PDF

**工具链：**
```bash
HTML/CSS → Puppeteer → PNG (1920×1080, 16:9)
```

**结论：** **最佳选择** - 灵活性最高，效果最专业

---

### 4. 其他创意方案

| 方案 | 说明 | 可行性 |
|------|------|--------|
| **Inkscape CLI** | 矢量图形，支持 SVG | ⭐⭐⭐ 需安装 |
| **ImageMagick** | 图像处理，可合成 | ⭐⭐ 效果有限 |
| **Blender Python** | 3D 渲染，超专业 | ⭐ 过度复杂 |

---

## 最终推荐：HTML/CSS + Puppeteer

**理由：**
1. 无需安装额外软件（已有 Node.js）
2. CSS 渐变/滤镜/混合模式完全满足需求
3. 可精确控制每个像素
4. 输出 PNG 后可插入任意 PPT
5. 可复用，批量生成

**安装：**
```bash
npm install puppeteer
```
