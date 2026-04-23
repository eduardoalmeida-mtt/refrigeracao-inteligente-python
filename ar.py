from ultralytics import YOLO
import cv2

# 1. Carrega o modelo YOLO
model = YOLO("yolov8n.pt")

# 2. Configuração da fonte de vídeo
# fonte_video = 0  # Descomente para usar a webcam do PC
fonte_video = 'http://192.168.150.44:8080/video'
cap = cv2.VideoCapture(fonte_video)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Detecção com YOLO
    results = model(frame, conf=0.5, verbose=False)
    
    pessoas_detectadas = 0
    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # ID 0 = Pessoa
                pessoas_detectadas += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 4. Nova Lógica da Temperatura (Redução por Grupos)
    # Se quiser mudar para 3 pessoas, troque o 2 abaixo por 3
    pessoas_por_grau = 2 
    
    if pessoas_detectadas == 0:
        temp = 26  # Modo Econômico
    else:
        # Começa em 24°C e subtrai 1 grau para cada grupo de X pessoas
        # Exemplo: 4 pessoas / 2 = reduz 2 graus -> 22°C
        reducao = pessoas_detectadas // pessoas_por_grau
        temp = max(18, 24 - reducao)

    # 5. Exibe as informações na tela
    # Fundo preto para as letras ficarem mais legíveis
    cv2.rectangle(frame, (5, 10), (300, 120), (0, 0, 0), -1) 
    cv2.putText(frame, f"Pessoas: {pessoas_detectadas}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"Temp. Ideal: {temp}C", (10, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Ar Condicionado Inteligente (YOLO)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()