
def Criacao_Bytes(Variavel):
    a = 0
    for i in bytes(str(Variavel),'utf-8'): a+=i
    return str(a)
def VerificarBytes(Byte,Verificar):
    if Byte == Verificar:
        return 'Efetuada com sucesso'
    else:
        return 'Erro ao verificar'

EmojiSenha = Criacao_Bytes("😉🐜🍇")
SenhaComum = Criacao_Bytes("uvadsffdfuvasdfdsad0")

print(VerificarBytes(EmojiSenha,SenhaComum))