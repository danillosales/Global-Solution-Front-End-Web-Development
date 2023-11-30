'''--------------VARIÁVEIS--------------'''
vld_2 = 'n'
lista_bpm = []
'''--------------FUNÇÕES----------------'''
def media_bpm(lista_bpm): #Calcula a média das 5 frequências cardíacas inseridas
    soma_bpm = 0
    for i in range(len(lista_bpm)):
        soma_bpm += int(lista_bpm[i])
    med_bpm = soma_bpm / len(lista_bpm)
    return med_bpm

def verif_parametros(idade,atv_fis,m): #Verifica o valor médio das frequências cardiácas de acordo com idade e condições físicas do paciente
    if idade <= 2 and (m < 120 or m > 140):
        return "\nA média de batimentos cardiácos não está dentro dos parâmetros para a idade inserida."
    elif 3 <= idade <= 17 and (m < 80 or m > 100):
        return "\nA média de batimentos cardiácos não está dentro dos parâmetros para a idade inserida."
    elif 18 <= idade < 60 and (m < 70 or m > 80) and atv_fis == 'n':
        return "\nA média de batimentos cardiácos não está dentro dos parâmetros para a idade e para a condição física inserida."
    elif 18<= idade < 60 and (m < 50 or m > 60) and atv_fis == 's':
        return "\nA média de batimentos cardiácos não está dentro dos parâmetros para a idade e para a condição física inserida."
    elif idade >= 60 and (m < 40 or m > 60):
        return "\nA média de batimentos cardiácos não está dentro dos parâmetros para a idade inserida."
    else:
        return "\nA média de batimentos cardiácos está dentro dos parâmetros."

'''--------------CÓDIGO------------------'''

print("----------------Smartwatch Data Validation--------------------")
print("\nVocê faz parte da equipe médica ou é um profissional da área de saúde?")
print("'s' - sim\n'n' - não")
vld_1 = input("Resposta: ")

if vld_1=='n': #Finaliza o programa caso a pessoa não seja um profissional da saúde
    print("\nInfelizmente o programa é voltado somente para médicos e profissionais de saúde.\nAgradecemos o interesse!")
    exit()

while vld_1 != "n" and vld_1 != "s":
    print("\nFavor responder a pergunta de acordo com os parâmetros apresentados.")
    vld_1 = input("Resposta: ")


print("\nCerto, será necessário criar um cadastro:")
login1 = input("login: ")
print("\nAVISO: Para a senha é obrigatório ter no mínimo 8 dígitos.")
senha1 = input("senha: ")
while len(senha1) < 8:
    print("\nA senha escolhida precisa ter 8 números no mínimo.")
    senha1 = input("senha: ")


while vld_2 == 'n': #Permite voltar ao início do programa após fazer uma verificação das frequências cardíacas
    print("\nAgora por favor insira suas credenciais:")
    login2=input("login: ")
    senha2=input("senha: ")
    while login1 != login2 or senha1 != senha2: #Verifica se as credenciais estão iguais as cadastradas
        print("\nO login ou a senha estão errados, favor inserir novamente.")
        login2 = input("login: ")
        senha2 = input("senha: ")

    print("\nIremos iniciar a inserção de dados:")
    idade=int(input("Idade do paciente: "))
    while idade<1 or idade>100:
        print("\nA idade do paciente deve variar entre 1 e 100 anos.")
        idade = int(input("Idade do paciente: "))

    print("Pratica atividade física?\n's' - sim\n'n' - não")
    atv_fis = input("Resposta: ")
    while atv_fis != 's' and atv_fis != 'n':
        print("\nFavor responder de acordo com o paramêtros solicitados.")
        atv_fis = input("Resposta: ")

    print("\nInsira pelo menos 5 batimentos cardíacos do paciente.")
    for i in range(5):
        bpm_input = input("Frequência cardiaca: ")
        while not bpm_input.isnumeric():
            print("\nA frequência cardiaca deve ser um número.")
            bpm_input = input("Frequência cardiaca: ")
        lista_bpm.append(bpm_input)

    m = media_bpm(lista_bpm)

    resultado_verificacao = verif_parametros(idade,atv_fis,m)
    print(f"\nA média das frequências cardíacas é: {m: .2f}")
    print(resultado_verificacao)

    print("\nDeseja finalizar o programa?")
    print("'s' - sim\n'n' - não")
    vld_2 = input("Resposta: ")

    if vld_2=='s':
        print("\nObrigado por utilizar o programa!\n---------------------PROGRAMA FINALIZADO---------------------------")
        break
