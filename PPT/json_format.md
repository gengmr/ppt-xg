# PPT JSON 文件格式规范

本文档严格定义了网页版课程PPT所使用的 JSON 数据文件格式，供课程内容编辑者参考使用。

---

## 顶层结构

```json
{
  "meta": { ... },
  "theme": { ... },
  "slides": [ ... ]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `meta` | Object | ✅ | 课程元数据 |
| `theme` | Object | ✅ | 全局主题配置 |
| `slides` | Array\<Slide\> | ✅ | 幻灯片内容列表，顺序即播放顺序 |

---

## `meta` 对象

描述整个演示文稿的基本信息。

```json
"meta": {
  "course": "Web应用开发技术",
  "chapter": "第一章",
  "title": "Web应用开发技术简介",
  "subtitle": "Introduction to Web Application Development",
  "instructor": "张三",
  "department": "计算机科学与技术学院",
  "school": "石家庄信息工程技术学院",
  "semester": "2026年春季学期",
  "duration": 60,
  "version": "1.0.0",
  "lastModified": "2026-03-10"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `course` | string | ✅ | 课程名称 |
| `chapter` | string | ✅ | 章节编号，如 `"第一章"` |
| `title` | string | ✅ | 课件标题（中文） |
| `subtitle` | string | ❌ | 课件标题（英文/副标题） |
| `instructor` | string | ✅ | 主讲教师姓名 |
| `department` | string | ❌ | 所属学院/系 |
| `school` | string | ✅ | 学校全称 |
| `semester` | string | ✅ | 学期，如 `"2026年春季学期"` |
| `duration` | integer | ✅ | 课程时长，单位**分钟** |
| `version` | string | ❌ | 文件版本号，语义化版本格式 |
| `lastModified` | string | ❌ | 最后修改日期，ISO 8601格式 `YYYY-MM-DD` |

---

## `theme` 对象

全局视觉主题配置（当前版本由 HTML 渲染器使用，可留空以使用默认主题）。

```json
"theme": {
  "primaryColor": "#1a237e",
  "accentColor": "#42a5f5",
  "backgroundColor": "#0d1117",
  "fontFamily": "Inter, 'Noto Sans SC', sans-serif",
  "codeFont": "'JetBrains Mono', monospace"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `primaryColor` | string (CSS色值) | ❌ | 主色调，用于标题、强调元素 |
| `accentColor` | string (CSS色值) | ❌ | 强调色，用于高亮、链接 |
| `backgroundColor` | string (CSS色值) | ❌ | 全局背景色 |
| `fontFamily` | string | ❌ | 正文字体族（CSS font-family格式） |
| `codeFont` | string | ❌ | 代码块专用字体 |

---

## `slides` 数组

每个元素为一张幻灯片。

---

## Slide 对象（通用字段）

```json
{
  "id": "slide-01",
  "type": "cover",
  "notes": "教师备注，不在屏幕上显示",
  "duration": 3,
  "content": { ... }
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `id` | string | ✅ | 幻灯片唯一标识符，建议 `"slide-01"` 格式 |
| `type` | string | ✅ | 幻灯片类型，见下方类型枚举 |
| `notes` | string | ❌ | 教师备注/讲稿要点（不显示在屏幕上） |
| `duration` | integer | ❌ | 建议讲授时间（分钟） |
| `content` | Object | ✅ | 该页具体内容，结构因 `type` 而异 |

---

## 幻灯片类型枚举（`type` 字段）

| 类型值 | 中文名称 | 适用场景 |
|--------|----------|----------|
| `cover` | 封面 | 课程第一页 |
| `agenda` | 目录/大纲 | 章节提纲 |
| `section` | 节标题 | 大节分隔页 |
| `content` | 内容页 | 通用文字内容 |
| `bullets` | 要点列表 | 多要点、条目式内容 |
| `comparison` | 对比页 | 两列对比展示 |
| `image` | 图文混排 | 含图片的内容页 |
| `code` | 代码演示 | 展示代码片段 |
| `diagram` | 图解页 | 架构图、流程图（HTML代码） |
| `table` | 表格页 | 数据表格 |
| `timeline` | 时间线 | 发展历程 |
| `quote` | 金句/引用 | 名人名言、重要定义 |
| `summary` | 小结 | 章节总结 |
| `thankyou` | 结束页 | 最后一页 |

---

## 各类型 `content` 字段详细说明

### `cover` — 封面

```json
"content": {
  "courseTitle": "Web应用开发技术",
  "chapterTitle": "第一章",
  "title": "Web应用开发技术简介",
  "subtitle": "Introduction to Web Application Development",
  "instructor": "张三 / Prof. Zhang San",
  "school": "石家庄信息工程技术学院",
  "semester": "2026年春季学期",
  "tags": ["HTML", "CSS", "JavaScript", "全栈开发"]
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `courseTitle` | string | 课程名称（大标题区域） |
| `chapterTitle` | string | 章节编号 |
| `title` | string | 本章标题 |
| `subtitle` | string | 英文副标题 |
| `instructor` | string | 授课教师 |
| `school` | string | 学校名称 |
| `semester` | string | 学期 |
| `tags` | string[] | 关键技术标签，展示为标签徽章 |

---

### `agenda` — 目录/大纲

```json
"content": {
  "title": "本章大纲",
  "items": [
    { "index": "01", "title": "互联网与Web的起源", "subtitle": "从ARPANET到WWW" },
    { "index": "02", "title": "Web基本工作原理", "subtitle": "HTTP、URL、浏览器" }
  ]
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 目录页标题 |
| `items` | AgendaItem[] | 目录条目列表 |
| `items[].index` | string | 序号，如 `"01"` |
| `items[].title` | string | 条目标题 |
| `items[].subtitle` | string | 条目副标题/描述（可选） |

---

### `section` — 节标题

```json
"content": {
  "section": "01",
  "title": "互联网与Web的起源",
  "subtitle": "从ARPANET到万维网的诞生",
  "icon": "🌐"
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `section` | string | 节序号 |
| `title` | string | 节标题 |
| `subtitle` | string | 节副标题 |
| `icon` | string | Unicode emoji 图标 |

---

### `content` — 通用内容页

```json
"content": {
  "title": "什么是Web应用？",
  "subtitle": "Web Application Definition",
  "body": [
    { "type": "paragraph", "text": "Web应用（Web Application）是指..." },
    { "type": "highlight", "text": "核心特征：无需安装，浏览器即客户端" },
    { "type": "paragraph", "text": "与传统桌面程序的区别在于..." }
  ],
  "aside": "扩展阅读：参见 RFC 2616 HTTP/1.1 规范"
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 页面标题 |
| `subtitle` | string | 英文副标题（可选） |
| `body` | BodyBlock[] | 正文内容块列表 |
| `aside` | string | 侧边注释/延伸阅读（可选） |

**BodyBlock 类型：**

| `type` 值 | 渲染效果 |
|-----------|----------|
| `paragraph` | 普通段落文字 |
| `highlight` | 带背景色高亮框 |
| `warning` | 警告/注意框（橙色） |
| `tip` | 提示框（绿色） |
| `definition` | 术语定义框（蓝色描边） |

---

### `bullets` — 要点列表

```json
"content": {
  "title": "前端三大核心技术",
  "subtitle": "The Three Core Web Technologies",
  "layout": "grid",
  "items": [
    {
      "icon": "📄",
      "title": "HTML",
      "subtitle": "结构语言",
      "detail": "定义页面的语义结构和内容，是Web的骨架",
      "badge": "HyperText Markup Language"
    }
  ]
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 页标题 |
| `subtitle` | string | 副标题 |
| `layout` | `"list"` \| `"grid"` \| `"cards"` | 条目排列方式 |
| `items` | BulletItem[] | 要点列表 |
| `items[].icon` | string | emoji图标 |
| `items[].title` | string | 要点主标题 |
| `items[].subtitle` | string | 副标题（小字） |
| `items[].detail` | string | 详细说明文字 |
| `items[].badge` | string | 技术名称徽章 |

---

### `comparison` — 对比页

```json
"content": {
  "title": "前端 vs 后端",
  "left": {
    "label": "前端（Frontend）",
    "icon": "🎨",
    "color": "blue",
    "items": ["HTML / CSS / JavaScript", "用户界面渲染", "浏览器中运行"]
  },
  "right": {
    "label": "后端（Backend）",
    "icon": "⚙️",
    "color": "green",
    "items": ["Node.js / Python / Java", "业务逻辑处理", "服务器中运行"]
  }
}
```

| 字段 | 说明 |
|------|------|
| `title` | 页标题 |
| `left` / `right` | 两列内容，结构相同 |
| `[col].label` | 列标题 |
| `[col].icon` | emoji图标 |
| `[col].color` | 主题色，支持 `blue` `green` `orange` `purple` |
| `[col].items` | string[] 条目列表 |

---

### `code` — 代码演示

```json
"content": {
  "title": "第一个HTML页面",
  "subtitle": "Hello World in HTML",
  "language": "html",
  "code": "<!DOCTYPE html>\n<html>\n  <head><title>My Page</title></head>\n  <body><h1>Hello, World!</h1></body>\n</html>",
  "explanation": [
    { "line": "1", "text": "DOCTYPE声明，告知浏览器这是HTML5文档" },
    { "line": "3-4", "text": "head区域放置元数据，不在页面显示" }
  ],
  "output": "<rendered output description or omit>"
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string | 页标题 |
| `language` | string | 代码语言：`html` `css` `javascript` `python` `sql` `bash` 等 |
| `code` | string | 代码内容，用 `\n` 换行 |
| `explanation` | ExplanationItem[] | 逐行注释（可选） |
| `explanation[].line` | string | 行号或行范围，如 `"3-5"` |
| `explanation[].text` | string | 该行/区块的说明 |
| `output` | string | 运行结果描述（可选） |

---

### `timeline` — 时间线

```json
"content": {
  "title": "Web发展历程",
  "subtitle": "Evolution of the Web",
  "items": [
    { "year": "1991", "event": "Tim Berners-Lee 发布 WWW", "detail": "在CERN发布第一个网页", "highlight": true },
    { "year": "1995", "event": "JavaScript 诞生", "detail": "Netscape 的 Brendan Eich 用10天创造了JS" }
  ]
}
```

| 字段 | 说明 |
|------|------|
| `items[].year` | 年份字符串 |
| `items[].event` | 事件标题 |
| `items[].detail` | 详细说明 |
| `items[].highlight` | `true` 时该节点重点高亮 |

---

### `table` — 表格页

```json
"content": {
  "title": "常用HTTP方法对比",
  "headers": ["方法", "作用", "是否有请求体", "典型场景"],
  "rows": [
    ["GET", "获取资源", "否", "查询数据"],
    ["POST", "提交数据", "是", "表单提交、创建资源"]
  ]
}
```

---

### `quote` — 金句/引用

```json
"content": {
  "quote": "The Web is more a social creation than a technical one.",
  "author": "Tim Berners-Lee",
  "role": "万维网发明者",
  "context": "用于强调Web技术服务于人、连接人的本质"
}
```

---

### `summary` — 小结

```json
"content": {
  "title": "本章小结",
  "points": [
    "Web诞生于1991年，由Tim Berners-Lee在CERN提出",
    "HTTP、URL、HTML是Web的三大基础",
    "前端（HTML/CSS/JS）+ 后端 + 数据库构成Web应用的完整架构"
  ],
  "nextChapter": {
    "chapter": "第二章",
    "title": "HTML基础",
    "preview": "HTML语义化标签、文档结构、表单设计"
  }
}
```

---

### `thankyou` — 结束页

```json
"content": {
  "title": "感谢聆听",
  "subtitle": "Thank You",
  "message": "如有疑问，请课后联系或在教学平台提问",
  "contact": "teacher@example.edu.cn",
  "qrcode": null,
  "nextClass": "下次课：第二章 HTML基础结构"
}
```

---

## 完整示例骨架

```json
{
  "meta": {
    "course": "Web应用开发技术",
    "chapter": "第一章",
    "title": "Web应用开发技术简介",
    "instructor": "张老师",
    "school": "石家庄信息工程技术学院",
    "semester": "2026年春季学期",
    "duration": 60
  },
  "theme": {
    "primaryColor": "#1a237e",
    "accentColor": "#42a5f5"
  },
  "slides": [
    { "id": "slide-01", "type": "cover", "duration": 3, "content": { ... } },
    { "id": "slide-02", "type": "agenda", "duration": 2, "content": { ... } },
    { "id": "slide-03", "type": "section", "duration": 1, "content": { ... } }
  ]
}
```

---

## 注意事项

1. **`id` 唯一性**：每张幻灯片的 `id` 必须全局唯一，推荐使用 `slide-01`、`slide-02` 格式。
2. **`duration` 总和**：所有幻灯片的 `duration` 之和应接近 `meta.duration`（单位分钟）。
3. **字符串转义**：`code` 字段中的代码换行必须使用 `\n`，引号使用 `\"` 转义。
4. **可选字段**：标注 ❌ 的字段可以省略，渲染器有默认处理逻辑。
5. **emoji兼容性**：`icon` 字段使用 Unicode emoji，确保操作系统字体支持。
6. **文件编码**：JSON文件必须使用 **UTF-8** 编码保存，否则中文将乱码。
