import os
if __name__ =='__main__':
  while True:
    x = input("what u want to speak (press q to quit): ")
    cmd = f"powershell -Command \"Add-Type -AssemblyName System.speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'{x}\')\" "
    if x == 'q':
        x = 'bye friend';
        cmd = f"powershell -Command \"Add-Type -AssemblyName System.speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak(\'{x}\')\" "
        os.system(cmd);
        break
    os.system(cmd)






 