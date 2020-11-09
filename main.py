# Inspiração: DankiCode
chave = input("Digite sua senha: ")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "!"
    elif letra in "Bb": senha = senha + "@"
    elif letra in "Cc": senha = senha + "&"
    elif letra in "Dd": senha = senha + "("
    elif letra in "Ee": senha = senha + "+"
    elif letra in "Ff": senha = senha + ")"
    elif letra in "Gg": senha = senha + "*"
    elif letra in "Hh": senha = senha + "/"
    elif letra in "Ii": senha = senha + "-"
    elif letra in "Jj": senha = senha + "="
    elif letra in "Kk": senha = senha + "_"
    elif letra in "Ll": senha = senha + "§"
    elif letra in "Mm": senha = senha + "º"
    elif letra in "Nn": senha = senha + "°"
    elif letra in "Oo": senha = senha + "ª"
    elif letra in "Pp": senha = senha + "["
    elif letra in "Qq": senha = senha + "}"
    elif letra in "Rr": senha = senha + "~"
    elif letra in "Ss": senha = senha + "{"
    elif letra in "Tt": senha = senha + "]"
    elif letra in "Uu": senha = senha + "^"
    elif letra in "Vv": senha = senha + "`"
    elif letra in "Ww": senha = senha + "'"
    elif letra in "Xx": senha = senha + "´"
    elif letra in "Yy": senha = senha + "<"
    elif letra in "Zz": senha = senha + ">"
    else: senha = senha + letra # Caso digite algum simbolo que não esteja na lista, ele irá manter na senha final
print("Sua nova senha: " + senha + " - Ela tambem foi salva no arquivo: senhas.txt")

# Essa parte irá procurar o arquivo senhas.txt, e irá salvar a senha alterada junto com a original
arquivo = open('senhas.txt', 'r+')
texto = arquivo.readlines()
arquivo.writelines(senha + " / " + chave + "\n")
arquivo.close()