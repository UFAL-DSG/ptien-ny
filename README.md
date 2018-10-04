PTIEN-NY dataset
================

Collection process
------------------
The audio was collected using Public Transport Information service for New York provided in English language(PTIEN-NY).
The PTIEN-NY is an automated service using [Alex spoken dialogue system framework](https://github.com/UFAL-DSG/alex).
See the [project website](http://alex-ptien.com/).

Release Notes
----------------------------
The data are released in a raw format, not thoroughly checked and validated.
The audio transcriptions were obtained using crowd sourcing.

### Audio
- Storage format: 16khz, signed-integer, 16bit, little endian wav
- Recording via HTML5 audio element or VOIP telephone channel
- The directory `all` contains the audio from the whole dialogues but only with the customer voice (no TTS).
- The directory `recorded` contains the customers audio with `Total Duration of 4166 files: 03:13:35.06`.
    - Contains `key_transcriptions.scp` which stores transcriptions for each of recorded wav files in the folders
- The `ptien-ny-extracted-flat` contains subset of `recorded` with `Total Duration of 1328 files: 00:58:49.09`.
    - Contains scp files containing transcriptions and `train, dev, test` are disjointly slitted.
    - `all-trns.scp` - 1328 utterances
    - `dev-trns.scp` - 200 utterances
    - `test-trns.scp` - 400 utterances
    - `train-trns.scp` - 729 utterances

### Scripts & metadata
- The meta data were created automatically but may contain errors.
- The `asr_transcribed_concatenated.xml` contains meta data about the dialogues
- The `extract_trans.py` script extract transcription given the `asr_transcribed_concatenated.xml` and `all` directory.


Contributors
------------
- Martin Vejman
- Filip Jurcicek
- Ondrej Dusek
- Ondrej Platek

License
-------
[Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/)
