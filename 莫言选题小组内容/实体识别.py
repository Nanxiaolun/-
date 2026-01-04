import os
import spacy
import hanlp
from docx import Document

def extract_entities(doc_path):
    if not os.path.exists(doc_path):
        print("文件不存在，请检查路径是否正确。")
        return

    try:
        doc = Document(doc_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

        nlp = spacy.load("zh_core_web_sm")
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        print("命名实体识别结果：")
        for entity, label in entities:
            print(f'实体: {entity}, 类型: {label}')

        triples = hanlp.extract_trigram(text)
        print("\n关系抽取结果：")
        for triple in triples:
            print(triple)

    except Exception as e:
        print(f"读取或处理文件时发生错误: {e}")

doc_path = "D:\莫言\檀香刑-莫言\檀香刑.docx"  # 替换为你的Word文件路径
extract_entities(doc_path)
