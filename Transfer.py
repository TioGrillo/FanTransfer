import aminofix
import os
import pyfiglet
import colorama
import getpass
import colored
from colored import fg, bg, attr
from progress.bar import IncrementalBar
#
#
#                                      🐈‍⬛
#                Script edit by Grígio and Dragomir
#                            BASED KAPIDEV
#
# ============= OBSERVAÇÃO ===========
#
#   Por favor, não alterar as informações do
#   script ou ele provavelmente irá parar de 
#   funcionar!
# #======================================

#color = bg('gold_1') + fg('black')
color2 = bg('orange_red_1') + fg('white')
color3 = bg('red_1') + fg('black')
color4 = bg('white') + fg('black')
##color3 = bg('yellow_1') + fg('black')
##color3 = bg('yellow_1') + fg('black')

color3 = bg('gold_1') + fg('black')
color = bg('medium_violet_red') + fg('white')
#color = bg('red_1') + fg('white')
color4 = bg('white') + fg('black')
##color3 = bg('yellow_1') + fg('black')
##color3 = bg('yellow_1') + fg('black')

reset = attr('reset')


print("\n" + color+(f"""{pyfiglet.figlet_format("GD Transfer", font="standard")}""")+reset)
print("""


""")



print("""                                                🐈‍⬛""")
print("   " + color+ (" × ") +  (" SUBMUNDO") + "            " + color4+("  × Grígio -") + (" Castiel   ") + reset)
print("""


""")
    
    
    
client = aminofix.Client()
client.login(email = input(' ••• Coloque seu Email:  '), password = input(' ••• Coloque sua Senha:  '))

print("""


""")

print("\n  " + color +"VOCÊ POSSUI   " + color4 + (f"{int(client.get_wallet_info().totalCoins)}")+ color+ "   COINS!"+ reset)
print("""


""")

idfk = input(' ••• Link do perfil: ')


comId = client.get_from_code(idfk).comId
userId = client.get_from_code(idfk).objectId
sbc = aminofix.SubClient(comId=comId, profile=client.profile)
users = sbc.get_online_users().profile.userId
coin_send = int(input(' ••• Quantidade de moedas que voce quer enviar?  '))/500
bar = IncrementalBar(' × Transerindo...', max=round(coin_send))

for _ in range(round(coin_send)):
    try:
        sbc.subscribe(userId=userId, autoRenew="False")
        bar.next()
    except Exception as i:
        print(f'Error: {i}')
        sbc.subscribe(userId, autoRenew="False")

    
    
print(("\n  " + color+"VOCÊ POSSUI   ") +color4+(f"{int(client.get_wallet_info().totalCoins)}") +color+ "   APÓS ESSA TRANSFERÊNCIA!" + ("\n"))


client.logout()
