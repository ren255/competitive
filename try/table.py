# %%
import pandas as pd
from pylatex import Document, LongTable, MultiColumn
from pylatex.utils import NoEscape
import subprocess

# CSVを読み込み
df = pd.read_csv("flashcard.csv", header=True)

# LaTeX文書を作成
doc = Document(documentclass="jsarticle")
doc.packages.append(NoEscape(r"\usepackage{amsmath}"))
doc.packages.append(NoEscape(r"\usepackage{longtable}"))

# テーブルを追加k
with doc.create(LongTable("|p{10cm}|p{5cm}|")) as table:
    table.add_hline()
    for index, row in df.iterrows():
        table.add_row([NoEscape(row[0]), NoEscape(row[1])])
        table.add_hline()

# PDFを生成
doc.generate_pdf("output", clean_tex=False)

# %%
