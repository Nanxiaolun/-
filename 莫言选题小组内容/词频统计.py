import os
import jieba
from collections import Counter
from docx import Document

# 指定Word文档的路径
doc_path = "D:\莫言\檀香刑-莫言\檀香刑.docx"  # 确保路径正确，使用原始字符串

# 检查文件是否存在
if not os.path.exists(doc_path):
    print("文件不存在，请检查路径是否正确。")
else:
    try:
        # 加载文档
        doc = Document(doc_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

        # 使用jieba进行分词
        seg_list = jieba.cut(text, cut_all=False)

        # 定义停用词列表
        stopwords = set(['的', '是', '在', '和', '了', '我', '有', '他', '她', '它', '这', '那', '也', '就', '不', '人', '都', '一个', '知县','他们','看到','大老爷','知道','已经','起来','自己','你们','不是','什么','咱家','就是','没有','这个','大人','两个','还是','感到','两只','之后','只有','不会'])
        
        # 过滤停用词并统计词频
        filtered_words = [word for word in seg_list if word not in stopwords and len(word) > 1]
        word_counts = Counter(filtered_words)

        # 打印词频统计结果
        for word, count in word_counts.most_common(100):  # 打印前20个最常见的词
            print(f"{word}: {count}")
    except Exception as e:
        print(f"读取或处理文件时发生错误: {e}")
