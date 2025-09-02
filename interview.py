import os
from pydub import AudioSegment

# Paths
base_path = os.path.dirname(os.path.abspath(__file__))
host_path = os.path.join(base_path, "audio", "host")
guest_path = os.path.join(base_path, "audio", "guest")
output_path = os.path.join(base_path, "audio", "interview.wav")

# Load files in order
host_files = sorted([f for f in os.listdir(host_path) if f.endswith(".wav")])
guest_files = sorted([f for f in os.listdir(guest_path) if f.endswith(".wav")])

# Alternate host and guest responses
interview_audio = AudioSegment.silent(duration=1000)  # 1 sec intro silence

for h, g in zip(host_files, guest_files):
    host_audio = AudioSegment.from_wav(os.path.join(host_path, h))
    guest_audio = AudioSegment.from_wav(os.path.join(guest_path, g))

    interview_audio += host_audio + AudioSegment.silent(duration=700)  # pause
    interview_audio += guest_audio + AudioSegment.silent(duration=1000)

# If more host replies are present after guests
if len(host_files) > len(guest_files):
    for i in range(len(guest_files), len(host_files)):
        host_audio = AudioSegment.from_wav(os.path.join(host_path, host_files[i]))
        interview_audio += host_audio + AudioSegment.silent(duration=800)

# Export final combined audio
interview_audio.export(output_path, format="wav")
print(f"Exported full interview to: {output_path}")
