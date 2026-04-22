import cv2

# --- CONFIGURAÇÃO ---
fonte_video = 'http://192.168.210.9:8080/video' 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(fonte_video)

print("Sistema de Refrigeração Inteligente Iniciado...")
print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Erro: Sem sinal da câmera. Tentando reconectar...")
        cap = cv2.VideoCapture(fonte_video)
        cv2.waitKey(2000)
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    num_pessoas = len(faces)

    # --- NOVA LÓGICA DE TEMPERATURA ---
    if num_pessoas > 0:
        # A cada 2 pessoas, subtrai 1 grau. 
        # Ex: 1 pessoa = 25°C | 2 pess. = 24°C | 3 pess. = 24°C | 4 pess. = 23°C
        reducao = num_pessoas // 2
        temp_ideal = 25 - reducao
        
        # Garante que não baixe de 18°C
        if temp_ideal < 18: 
            temp_ideal = 18
    else:
        temp_ideal = 26

    # --- VISUAL ---
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Informações na tela
    cv2.putText(frame, f'Pessoas: {num_pessoas}', (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f'Ajuste Ar: {temp_ideal}C', (20, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow('Monitoramento Ar Condicionado', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()