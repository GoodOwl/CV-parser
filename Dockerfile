FROM base-image # TODO: find image with python and java
RUN pip install resume-parser

# Dependency of spacy
RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
RUN pip install importlib-metadata==3.2.0
# For NLP operations we use spacy and nltk. Install them using below commands:
# spaCy
RUN python -m spacy download en_core_web_sm

# nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN python -m nltk.downloader universal_tagset
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader brown
RUN python -m nltk.downloader maxent_ne_chunker
