# pyiunstir

A simple NLP framework for the Iberian language

The framework includes different modules:

* Encoding. Support for Northeastern, Southeasterh and Greek Iberian scripts, dual and simplified version and ASCII.
* Corpus. Including texts using the 3 scripts and metadata (geolocation, support, Hesperia IDs, etc.)
* Alignment. Multiple and pair word alignments using the ALINE method for paradigm detection and language comparison (e.g. euskera)
* Spellchecker. Hidden Markov Model based on the corpus (e.g. identification of celtic words, wrong symbols, etc.)
* Segmentation model. Trained using the available corpus using methodology applied to the Chinese language (e.g. scriptio continua)
* Part-of-speech tagger. Based on a combinatorial dictionary (tagging of personal names, numbers and verbs)
