from representacaoEstado import inicializar_estado
from auxForMain import imprimir_mensagem_centralizada,definir_tempo_maximo, avaliar_encomenda,processar_encomenda, visualizar_perfil_estafeta

def main():
    saida = -1
    estado_inicial = inicializar_estado()


    imprimir_mensagem_centralizada("BEM-VINDO À HEALTH PLANET")

    while saida != 0:
        print("1- Definições de Cliente ")
        print("2- Informações do estafeta e encomenda")
        print("0- Sair\n")

        try:
            saida = int(input("Introduza a sua opção:\n"))
        except ValueError:
            print("Por favor, insira um valor válido.\n")
            continue 

        if saida == 0:
            print("saindo.......")

        elif saida == 1:
            print("1- Definir tempo máximo de entrega.")
            print("2- Avaliar encomenda (após recebida).")
            print("0- Voltar à página anterior.\n")

            try:
                clienteSaida = int(input("Introduza a sua opção: "))
            except ValueError:
                print("Por favor, insira um valor válido.\n")
                continue 

            if clienteSaida == 0:
                print("Saindo.......") ###################este esta a sair da pagina!!!!
                break
            elif clienteSaida == 1:
                definir_tempo_maximo(estado_inicial)
            elif clienteSaida == 2:
                avaliar_encomenda(estado_inicial)

        elif saida == 2:
            while True:

                print("1- Encomenda a entregar, meio de transporte e caminho")
                print("2- Ver perfil")
                print("0- Voltar à página anterior")

                try:
                    EstafetaSaida = int(input("Introduza a sua opção: "))
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue 

                if EstafetaSaida == 0:
                    break
                if EstafetaSaida == 0:
                    break
                elif EstafetaSaida == 1:
                    processar_encomenda(estado_inicial)
                elif EstafetaSaida == 2:
                    visualizar_perfil_estafeta(estado_inicial)

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            l = input("Prima enter para continuar.")

if __name__ == "__main__":
    main()



