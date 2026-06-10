def usar_pocion(vida_actual, esta_envenenado):
    pocion = 50
    
    if esta_envenenado:
        pocion = 25
        print("⚠️ ¡Estás envenenado! La poción cura la mitad.")
    
    vida_final = vida_actual + pocion
    
    if vida_final > 100:
        vida_final = 100
        print("❤️ ¡Vida al máximo!")
    else:
        print(f"✨ Te has curado. Vida actual: {vida_final}")
        
    return vida_final

print("-- Simulando inicio de partida --")
vida_jugador = 60

vida_jugador = usar_pocion(vida_jugador, esta_envenenado=True)