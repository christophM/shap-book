import os

chapter_files = ['correlation.qmd', 'aggregated.qmd', 'logistic.qmd', 'classification.qmd', 'history.qmd', 'image.qmd', 'image-deepexplainer.qmd', 'text.qmd', 'extensions.qmd', 'other.qmd', 'dashboard.qmd', 'limitations.qmd', 'shap-library.qmd']

for chapter_file in chapter_files:
    print('Editing ' + chapter_file)
    os.system(f'python edit.py {chapter_file}')
