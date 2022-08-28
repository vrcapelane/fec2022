import cv2

face_cascade = cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml'
eye_cascade = cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml'

# carregar classificador
faceClassifier = cv2.CascadeClassifier(face_cascade)
eyeClassifier = cv2.CascadeClassifier(eye_cascade)

# iniciando a camera
capture = cv2.VideoCapture(0)

# definindo tamanho da imagem 
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# contadores
contadorDeOlhosAux = 0
contadorDeFacesAux = 0
contadorDeFacesMax = 0
contadorDeOlhosMax = 0

# logica de detecção
while not cv2.waitKey(8) & 0xFF == ord("q"):
    ret, frame_color = capture.read()

    faces = faceClassifier.detectMultiScale(frame_color)
    eyes = eyeClassifier.detectMultiScale(frame_color)

    font = cv2.FONT_HERSHEY_DUPLEX
    tamFont = 0.75
    boldFont = 2
    corFace = (0, 202, 99)
    corEye = (0, 165, 255)
    corMensagemSair = (0, 0, 180)
    corMsgContadores = (45, 0, 140)

    contadorDeFaces = 0
    contadorDeOlhos = 0

    cv2.putText(frame_color, 'Pressione "q" para fechar', (10, 25), font, tamFont, corMensagemSair, boldFont)

    for x, y, w, h in faces:

        contadorDeFaces = contadorDeFaces + 1
        cv2.rectangle(frame_color, (x, y), (x + w, y + h), corFace, 2)
        cv2.putText(frame_color, 'Rosto', (x, y - 5), font, tamFont, corFace, boldFont)
        cv2.putText(frame_color, 'Numero de faces encontradas: ' + str(contadorDeFacesAux) + ' (MAX: ' + str(contadorDeFacesMax) + ')', (10, 55), font, tamFont, corMsgContadores, boldFont)

    for x, y, w, h in eyes:

        contadorDeOlhos = contadorDeOlhos + 1
        cv2.rectangle(frame_color, (x, y), (x + w, y + h), corEye, 2)
        cv2.putText(frame_color, 'Olho', (x, y - 5), font, tamFont, corEye, boldFont)
        cv2.putText(frame_color, 'Numero de olhos encontrados: ' + str(contadorDeOlhosAux) + ' (MAX: ' + str(contadorDeOlhosMax) + ')', (10, 85), font, tamFont, corMsgContadores, boldFont)

    contadorDeOlhosAux = contadorDeOlhos
    contadorDeFacesAux = contadorDeFaces

    if(contadorDeFacesMax < contadorDeFacesAux):
        contadorDeFacesMax = contadorDeFacesAux

    if(contadorDeOlhosMax < contadorDeOlhosAux):
        contadorDeOlhosMax = contadorDeOlhosAux

    cv2.imshow('Fec2022-openCV', frame_color)