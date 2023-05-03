from pygame import mixer, event

# Inicializa o módulo mixer
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load('musica.mp3')

# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda a reprodução por alguns segundos
input()
pygame.event.wait()

# Finaliza o módulo mixer
pygame.mixer.quit()
