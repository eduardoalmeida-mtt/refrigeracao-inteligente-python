from ultralytics import YOLO
import cv2

# 1. Carrega o modelo YOLO (versão nano é a mais rápida para PC comum)
model = YOLO("yolov8n.pt")

# 2. Configuração da fonte de vídeo (0 para webcam ou link do IP Webcam)
# retira do "#" se for web cam e colocar "#" o que tem ip 
#fonte_video = 0
fonte_video = 'http://192.168.150.44:8080/video'
cap = cv2.VideoCapture(fonte_video)   

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. O YOLO faz a detecção (conf=0.5 ignora detecções duvidosas)
    results = model(frame, conf=0.5, verbose=False)
    
    # Filtramos apenas a classe 'person' (ID 0 no YOLO)
    pessoas_detectadas = 0
    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # 0 é o código para 'pessoa'
                pessoas_detectadas += 1
                # Desenha o quadrado na tela
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 4. Lógica da Temperatura
    if pessoas_detectadas == 0:
        temp = 26
    elif pessoas_detectadas == 1:
        temp = 24
    else:
        temp = max(18, 24 - (pessoas_detectadas - 1))

    # 5. Exibe as informações na tela
    cv2.putText(frame, f"Pessoas: {pessoas_detectadas}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"Temp. Ideal: {temp}C", (10, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Ar Condicionado Inteligente (YOLO)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()