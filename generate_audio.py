import os
from TTS.api import TTS

def generate_audio_for_folder(speaker, model_name):
    print(f"Generating voice for '{speaker}' using model '{model_name}'")

    tts = TTS(model_name=model_name, progress_bar=True, gpu=False)

    base_path = os.path.dirname(os.path.abspath(__file__))
    text_dir = os.path.join(base_path, "text", speaker)
    output_dir = os.path.join(base_path, "audio", speaker)

    os.makedirs(output_dir, exist_ok=True)

    for file_name in sorted(os.listdir(text_dir)):
        if file_name.endswith(".txt"):
            text_path = os.path.join(text_dir, file_name)
            output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}.wav")

            with open(text_path, "r", encoding="utf-8") as f:
                text = f.read().strip()

            print(f"Generating audio for: {file_name} -> {output_path}")
            tts.tts_to_file(text=text, file_path=output_path)

    print(f"Finished generating audio for '{speaker}'")

# Both models are espeak-free
generate_audio_for_folder("host", "tts_models/en/ljspeech/glow-tts")
generate_audio_for_folder("guest", "tts_models/en/ljspeech/tacotron2-DDC")
