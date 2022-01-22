import random

List_color = ["rouge","vert","bleu","jaune","blanc","noir"]

def random_combinaison():
    L = []
    for i in range(4):
        color = List_color[random.randint(0, 5)]
        L.append(color)
    return L

def answer_color(L_user_color,L_solution):
    nb_good_place_good_color = 0
    nb_wrong_place_good_color = 0
    L = [False,False,False,False] #list qui permet de vérifier que par exemple si j'ai 2 noir dans user et 1 dans color, noir ne sera compté qu'une fois à la mauvaise place
    L2 = [False,False,False,False]
    for i in range(4):
        for j in range(4):
            if(L_user_color[i] == L_solution[j] and i == j):
                nb_good_place_good_color+=1
            else:
                if(L_user_color[i] == L_solution[j] and i != j and L[j] == False and L_user_color[j] != L_solution[j] and L2[i] == False):
                    nb_wrong_place_good_color+=1
                    L[j] = True
                    L2[i] = True

    return nb_good_place_good_color,nb_wrong_place_good_color

def recup_user_color():
    string_answer = input("what is your combinaison of color ?\n")
    color_string = ""
    L = []
    
    for letter in string_answer:
        if(letter == " " or letter == string_answer[len(string_answer)-1]):
            if(letter == string_answer[len(string_answer)-1]):
                color_string += letter
            for color in List_color:
                if(color == color_string):
                    L.append(color_string)
                    color_string = ""
        else:
            color_string += letter
    return L

def main():
    L_solution = random_combinaison()
    L_answer = []
    nb_of_attemp = 12
    nb_good_place_good_color = 0
    nb_wrong_place_good_color = 0
    #print(L_solution)

    while(nb_of_attemp != 0 and nb_good_place_good_color != 4):
        while(len(L_answer) != 4):
            L_answer = recup_user_color()
        nb_good_place_good_color,nb_wrong_place_good_color = answer_color(L_answer, L_solution)
        print("les couleurs de la bonne couleurs et à la bonne position sont au nombre de: " + str(nb_good_place_good_color))
        print("les couleurs de la bonne couleurs mais à à la mauvaise place sont au nombre de: " + str(nb_wrong_place_good_color))
        L_answer = []
        nb_of_attemp-=1

    if(nb_good_place_good_color == 4):
        print("Bien joué vous avez gagné!")
    else:
        print("Dommage, retentez votre chance !")
        print("La bonne combinaison était :")
        print(L_solution)

main()