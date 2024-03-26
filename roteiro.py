import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('imagemPaisagem.jpg')

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Separar as bandas R, G, B
b, g, r = cv2.split(imagem)
hsv = cv2.cvtColor(imagem,cv2.COLOR_BGR2RGB)

# Banda R permanece inalterada
banda_r = r

# Calcular a banda G ponderada pela pureza da cor do pixel
banda_g = cv2.merge([r, g, r])  # Ponderação da banda G pela banda R

# Calcular o brilho como a média das bandas R, G e B
brilho = cv2.merge((r, g, b)).mean(axis=2).astype(np.uint8)

# Calcular a banda B como a diferença entre a banda R e o brilho
banda_b = cv2.absdiff(r, brilho)
V = hsv[:,:,2]
B_NEW = banda_r - V

# Calcular a nova banda G
S = hsv[:,:,1]
G_NEW = ((banda_r/255)*(S/255))*255

# Juntar as bandas novamente
imagem_final = cv2.merge([banda_r, G_NEW.astype(np.uint8), B_NEW.astype(np.uint8)])

# Mostrar as bandas e a imagem final
cv2.imshow('Banda R', banda_r)
cv2.waitKey(1000)  # Aguarda 1 segundo
cv2.imshow('Banda G', banda_g)
cv2.waitKey(1000)  # Aguarda 1 segundo
cv2.imshow('Banda B', banda_b)
cv2.waitKey(1000)  # Aguarda 1 segundo
cv2.imshow('Imagem Final', imagem_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
