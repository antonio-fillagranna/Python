def criar_face():
    face = [
        ['B', 'B', 'B'],
        ['B', 'B', 'B'],
        ['B', 'B', 'B']
    ]
    return face

def girar_face_horario(face):
    # Rotação horária de 90 graus
    nova_face = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            nova_face[j][2-i] = face[i][j]
    return nova_face

face = criar_face()
face = girar_face_horario(face)
print(face)