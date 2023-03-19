import pygame, random, datetime




def reaction_tester_main():
    pygame.init()

    win = pygame.display.set_mode((1400, 800))
    font = pygame.font.SysFont('Arial', 30)
    pygame.display.set_caption("Reaction Test")

    count = 0

    wait_time = 0
    reaction_sum = 0
    average_reaction = 0

    game_state = "start"

    running = True
    reaction_text = None
    average_reaction_text = None
    count_text = None
    

    start_text = font.render("Press Left-Click to start!", True, "red")




    while running:

        current_time = pygame.time.get_ticks()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
                time = datetime.datetime.now()
                data.write('\n')
                data.write('\n')
                data.write(f"Test from {time}")
                data.write('\n')
                running = False
                
                pygame.display.quit()
                pygame.quit()
                break

            if event.type == pygame.MOUSEBUTTONDOWN:

                if game_state == "wait":
                    game_state = "fail"
                    reaction_text = font.render(("To fast!"), False, "white") 
                    start_text = font.render("Press Left-Click to start!", True, "red")

                if game_state == "start":
                    wait_time = random.randint(2000,6000) + current_time  
                    game_state = "wait" 
                    start_text = None         
                    reaction_text = None

                if game_state == "get_reaction":

                    reaction_time = current_time - wait_time
                    game_state = "start"

                    count += 1
                    reaction_sum += reaction_time
                    average_reaction = reaction_sum / count
                    print(average_reaction)
                    reaction_text = font.render((f"Reaction Time:{reaction_time}"), False, "white") 
                    start_text = font.render("Press Left-Click to start!", True, "red") 
                    average_reaction_text = font.render((f"Average Reaction Time:{average_reaction}"), False, "white")
                    count_text = font.render((f"Count: {count}"), False, "white")

                    data = open('data.txt', 'a')
                    data.write('\n')
                    data.write(f"Count {count} Reaction Time: {reaction_time}")
                    if count % 5 == 0:
                        data.write('\n')
                        data.write(f"Average Reaction Time: {average_reaction}")
                        data.close()


        if game_state == "fail":
            game_state = "start"           

        if game_state == "wait":

            if current_time >= wait_time:
                game_state = "get_reaction"

        if game_state == "get_reaction":
            win.fill(pygame.Color("green"))

        if game_state == "wait":
            win.fill(pygame.Color("black"))

        if start_text:       
            win.fill(pygame.Color("black"))
            win.blit(start_text, start_text.get_rect(center=(700, 300)))

        if reaction_text:       
            win.blit(reaction_text, reaction_text.get_rect(center=(700, 650)))
        if average_reaction_text:
            win.blit(average_reaction_text, average_reaction_text.get_rect(center=(700, 750)))
        if count_text:
            win.blit(count_text, count_text.get_rect(center=(700, 700)))
        pygame.display.flip()
     
    



