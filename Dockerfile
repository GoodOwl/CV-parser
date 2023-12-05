FROM python:3.12

ENV JAVA_HOME=/opt/java/openjdk
COPY --from=eclipse-temurin:21-jre $JAVA_HOME $JAVA_HOME
ENV PATH="${JAVA_HOME}/bin:${PATH}"

RUN pip install resume-parser \

# Dependency of spacy
 && pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz \
 && pip install importlib-metadata==3.2.0 \
# For NLP operations we use spacy and nltk. Install them using below commands:
# spaCy
 && python -m spacy download en_core_web_sm \

# nltk
 && python -m nltk.downloader stopwords \
 && python -m nltk.downloader punkt \
 && python -m nltk.downloader averaged_perceptron_tagger \
 && python -m nltk.downloader universal_tagset \
 && python -m nltk.downloader wordnet \
 && python -m nltk.downloader brown \
 && python -m nltk.downloader maxent_ne_chunker
