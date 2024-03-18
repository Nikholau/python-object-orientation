def melhor_classificado(C, Ce, Cs, Fv, Fe, Fs):
    pontos_cormengo = C * 3 + Ce
    pontos_flaminthians = Fv * 3 + Fe

    if pontos_cormengo == pontos_flaminthians:
        if Cs == Fs:
            return "Empate"
        elif Cs > Fs:
            return "Cormengo"
        else:
            return "Flaminthians"
    elif pontos_cormengo > pontos_flaminthians:
        return "Cormengo"
    else:
        return "Flaminthians"

C, Ce, Cs, Fv, Fe, Fs = map(int, input().split(','))

print(melhor_classificado(C, Ce, Cs, Fv, Fe, Fs))
