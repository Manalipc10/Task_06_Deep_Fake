# Task_06_Deep_Fake

This project is part of Research Task 6: Deep Fake for Syracuse University. The objective is to convert a narrative or script into an AI-generated interview using free and open-source tools, focusing on process and automation over polished visuals.

## Objective

- Convert host and guest dialogue scripts into synthetic speech using Text-to-Speech (TTS) models.
- Generate individual audio files for each segment.
- Stitch all audio clips together in a realistic conversational sequence.
- Produce a final interview audio in `.wav` format.

## Folder Structure
Task_06_Deep_Fake/
├── generate_audio.py # Generates individual audio clips from text
├── interview.py # Merges all clips into a full interview
├── README.md # Project documentation
├── requirements.txt # Dependencies
│
├── text/ # Input dialogue scripts
│ ├── host/ # host1.txt to host9.txt
│ └── guest/ # guest1.txt to guest7.txt
│
├── audio/ # Generated audio clips and final output
│ ├── host/ # host1.wav, host2.wav, ...
│ ├── guest/ # guest1.wav, guest2.wav, ...
│ └── interview.wav # Final stitched interview
│
├── voices/ # Local model configs (not committed to GitHub)
│ └── *.json or checkpoints # Not required for pretrained model usage


Note: The `voices/` folder was excluded from the GitHub commit due to size and format constraints. This folder contained locally downloaded model configuration files for Coqui TTS, which are not required when loading public models from Hugging Face by name.
Github repo reference: https://github.com/rhasspy/piper/blob/master/VOICES.md
This project uses official Piper
voice models in ONNX format. The following voices were used for generating the interview audio:

Role	Voice File Name	Description
Host	en_US-ryan-high.onnx	Male English (US), high quality
Guest	en_US-libritts-high.onnx	Female English (US), high quality

Each voice consists of a .onnx model file and a corresponding .json configuration file.

## Process Overview

1. Input `.txt` files are stored under `text/host` and `text/guest`.
2. `generate_audio.py` uses Coqui TTS to convert each text file to `.wav` format using publicly available models.
3. `interview.py` merges the audio clips into a continuous back-and-forth interview format with brief silences between speakers.
4. The result is exported as `audio/interview.wav`.

## How to Run

1. Set up a virtual environment with Python 3.10.
2. Install required dependencies:

```bash
pip install -r requirements.txt


