FROM python:3.9

# expose container for API
EXPOSE 5000
LABEL MAINTAINER="Tim Dentry <tdentry@arizona.edu>"

COPY . .

# PYTHON DATA SCIENCE PACKAGES
#   * numpy: support for large, multi-dimensional arrays and matrices
#   * matplotlib: plotting library for Python and its numerical mathematics extension NumPy.
#   * scipy: library used for scientific computing and technical computing
#   * scikit-learn: machine learning library integrates with NumPy and SciPy
#   * pandas: library providing high-performance, easy-to-use data structures and data analysis tools
#   * nltk: suite of libraries and programs for symbolic and statistical natural language processing for English
#   * spacy:  a package built for NLP tasks such as text processing and data analysis
#   * gensim:  a package used for NLP tasks such as semantic modeling
ENV PYTHON_PACKAGES="\
    numpy \
    matplotlib \
    scikit-learn \
    pandas \
    nltk \
    wordcloud \
    spacy \
    seaborn \
    gensim \
"

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt

# CMD tail -f /dev/null
CMD python app.py