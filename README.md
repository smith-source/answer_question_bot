# Answer_bot 项目说明文档

## 项目简介

Answer_bot 是一个智能问答机器人项目，结合了图像识别（OCR）和自然语言处理功能，能够从图像中提取文字并回答相关问题。该项目使用了OCR模型进行文字识别，并利用大型语言模型提供答案。

## 功能特点

- **图像文字识别**：支持从图像中提取文字内容
- **智能问答**：基于提取的文字内容，结合网络搜索，提供准确的答案
- **交互式图像裁剪**：支持通过鼠标选择图像中的特定区域进行文字识别
- **环境变量管理**：使用 dotenv 管理 API keys，提高安全性

## 安装说明

### 1. 克隆项目

```bash
git clone https://github.com/smith-source/answer_question_bot.git
cd Answer_bot
```

### 2. 安装依赖

```bash
pip install python-dotenv langchain langchain_community tavily transformers pillow opencv-python
```

### 3. 配置环境变量

复制示例配置文件并填入您的 API 密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入您的 API 密钥：

```
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
OPENAI_API_BASE=https://api.chatanywhere.tech/v1
```

### 4. 下载 OCR 模型

下载 GOT-OCR2_0 模型并放置在指定路径（默认为 `/GOT-OCR2_0`）。您可以在代码中修改模型路径。

## 文件结构说明

- **api.py**：核心 API 功能，包含使用 OpenAI 和 Tavily 进行问答的逻辑
- **chat.py**：OCR 模型加载和文字识别功能
- **crop_img.py**：图像裁剪和主程序逻辑
- **tmp.py**：OCR 测试脚本
- **.env**：环境变量配置文件（不应提交到版本控制）
- **.env.example**：环境变量配置示例

## 使用方法

### 1. 直接运行问答功能

修改 `crop_img.py` 中的示例文本，然后运行：

```bash
python crop_img.py
```

### 2. 使用图像识别功能

```bash
python chat.py
```

您需要在代码中修改图像路径或传入图像参数。

### 3. 交互式图像裁剪

取消注释 `crop_img.py` 中的相关代码，然后运行：

```bash
python crop_img.py
```

使用鼠标选择图像中的区域，然后按 'q' 退出捕获，系统将自动识别选中区域的文字并回答相关问题。

## API 说明

### 核心函数

#### answer_qustion(question)
- **功能**：回答给定问题
- **参数**：`question` - 要回答的问题文本
- **返回值**：包含答案的详细报告

#### read_img(img)
- **功能**：从图像中提取文字
- **参数**：`img` - 图像对象或路径
- **返回值**：识别出的文字内容

## 注意事项

- 确保已正确配置环境变量中的 API 密钥
- OCR 模型需要较大的显存，建议在支持 CUDA 的 GPU 上运行
- 图像识别的准确性取决于图像质量和文本清晰度

## 依赖项

- python-dotenv
- langchain
- langchain_community
- tavily
- transformers
- pillow
- opencv-python
- torch

## License

该项目为个人学习和研究使用。
