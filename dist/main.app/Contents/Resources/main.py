import sys, time, pygame
from pygame import Vector2
import marker, messageBox
import player

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1,0.0)

walkingSound = pygame.mixer.Sound('walking.mp3')
pygame.mixer.Sound.set_volume(walkingSound, 0.3)

idle_frame_start = time.time()
walking_frame_start = time.time()

size = width, height = 1225, 900
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# Player
player = player.Player((600, 300), all_sprites)

map = pygame.image.load("beleriand_map.jpg").convert()
map = pygame.transform.scale(map, (1225, 900))
maprect = map.get_rect()

markimg = pygame.image.load("marker_img.png").convert_alpha()
markimg = pygame.transform.scale(markimg, (18, 18))

# First Marker: Doriath
doriath = marker.Marker(markimg, 680, 306)
doriathrect = doriath.pos
mdoriath = messageBox.Button("With the location of her husband unknown, Morwen sent eight-year-old Túrin to",
                             "Doriath, where Thingol took him as a foster. Years passed and Túrin grew into",
                             "a young man. In the marches of Doriath, our hero and Beleg Strongbow defended",
                             "Doriath from orc attacks, winning great favor in the eyes of Thingol. When Túrin",
                             "accidentally caused the death of Saeros, an advisor to Thingol, he decided to",
                             "flee Doriath rather than face punishment. He fled south of the River Teiglin.",
                             323, 630, 578, 152)
#
# Second Marker: Brethil                                                                                       #
brethil = marker.Marker(markimg, 523, 345)  #
brethilrect = brethil.pos
mbrethil = messageBox.Button("Having fled Doriath, Túrin joined a band of outlaws south of the River Teiglin",
                             "He rose through their ranks to eventually become their captain. A year passed as",
                             "they wandered the woods, but Beleg sought after Túrin. Beleg eventually stumbled",
                             "upon Túrin's encampment, and the two reunited. Beleg informed Túrin of Thingol's",
                             "pardon and implored him to return to Doriath, but Túrin refused. As Beleg departed,",
                             'Túrin said to the elf, "Seek for me on Amon Rûdh! Else, this is our last farewell".',
                             323, 630, 578, 152)

# Third Marker: Amon Rudh
amonrudh = marker.Marker(markimg, 498, 352)
amonrudhrect = amonrudh.pos
mamonrudh = messageBox.Button("Túrin led his men westward where they come upon three Dwarves. The outlaws.",
                              "attacked, slaying one and capturing another. Their captive was called Mîm, and",
                              "he offered the location of his hidden halls in Amon Rûdh in exchange for his life.",
                              "Túrin accepted, and settled there with his men, growing close to Mîm. Beleg returned",
                              "and joined Túrin's band. Mîm grew jealous of their bond and betrayed the group to a",
                              "party of orcs, leading to Túrin's capture. Beleg tracked them to Taur-nu-Fuin.",
                              323, 630, 578, 152)

# Fourth Marker: Taur-nu-Fuin
taurnufuin = marker.Marker(markimg, 650, 140)
taurnufuinrect = taurnufuin.pos
mtaurnufuin = messageBox.Button("Beleg tirelessly tracked the band of orcs to Taur-nu-Fuin. He encountered the Elf",
                                "Gwindor, an escaped slave from Angband. They rescued an unconcious Túrin and",
                                "carried him away from danger. Beleg produced Anglachel and cut Túrin's bindings,",
                                "but the blade sliped and pricked Túrin's foot. Túrin awoke, seized the blade and ",
                                "killed Beleg, thinking him to be a foe in confusion and rage. Túrin was overcome",
                                "with grief. After they buried Beleg, Gwindor and Túrin continued to Nargothrond.",
                                323, 630, 578, 152)

# Fifth Marker: Eithil Ivrin
eithil = marker.Marker(markimg, 345, 223)
eithilrect = eithil.pos
meithil = messageBox.Button("Túrin did not speak as he traveled with Gwindor. Gwindor guided him westward",
                            "where they arrived at Eithil Ivrin. Túrin knelt down to drink from the spring.",
                            "As he did, Túrin cast himself to his knees and wept for his friend Beleg.",
                            "There, he wrote a song for Beleg, The Song of the Great Bow, and Gwindor gifted",
                            "him Anglachel. Gwindor then revealed that he was a lord of Nargothrond before",
                            "his enslavement. They traveled south along the banks of the Narog towards the city.",
                            323, 630, 578, 152)

# Sixth Marker: Nargothrond
nargothrond = marker.Marker(markimg, 395, 415)
nargothrondrect = nargothrond.pos
mnargothrond = messageBox.Button("Gwindor and Túrin arrived at the city. Anglachel was reforged into Gurthang, and",
                                 "Túrin gained favor among the Elves of Nargothrond. Finduilas fell in love with",
                                 "Túrin, who had not revealed his true identity, but declined her advances as",
                                 "Gwindor previously loved her. Túrin's true identity was revealed and he became",
                                 "chief counsellor to Orodreth. Túrin built a great bridge before the city's gates",
                                 "and marched an army to Ered Wethrin to confront the amassing agents of Angband. ",
                                 323, 630, 578, 152)

# Seventh Marker: Ered Wethrin
eredwethrin = marker.Marker(markimg, 419, 218)
eredwethrinrect = eredwethrin.pos
meredwethrin = messageBox.Button("Túrin, wielding the Black Sword of Nargothrond, went forth with the warriors",
                                 "of Nargothrond to meet the host of Morgoth. They were met with far greater",
                                 "numbers than anticpated, and none save Túrin were able to escape the flames of",
                                 "Glaurung. The Elves were pushed back to the field of Tumhalad where they perished.",
                                 "Orodreth was slain, and the mortally wounded Gwindor commanded Túrin to return to",
                                 'Nargothrond to save Finduilas, for "She alone stands between thee and thy doom."',
                                 323, 630, 578, 152)

# Eighth Marker: Gates of Nargothrond
gatesofnargo = marker.Marker(markimg, 420, 435)
gatesofnargorect = gatesofnargo.pos
mgatesofnargo = messageBox.Button("Mustering what forces he could, Túrin sped back to Nargothrond. Before him,",
                                  "he saw the host of orcs and Glaurung sacking the city and taking captives.",
                                  "Túrin charged forward, striking down all before him. Glaurung met Túrin at the",
                                  "gates, casting a spell on him with a serpent's gaze. Túrin, unable to move, ",
                                  "watched as Finduilas and hundreds of captives were dragged away. Glaurung's ",
                                  "spell sent Túrin to Dor-lómin believing his kin to be in danger. ",
                                  323, 630, 578, 152)

# Ninth Marker: Dor-lómin
dorlomin = marker.Marker(markimg, 320, 195)
dorlominrect = dorlomin.pos
mdorlomin = messageBox.Button("At Dor-lómin, Túrin found the halls of his old home empty. He came to the",
                              "halls of an Easterling named Brodda who took Aerin, a kinswoman to Húrin,",
                              "as his wife. Túrin stromed the hall where Brodda stayed and demanded to",
                              "know where his family went. From Aerin, Túrin learned that his family went",
                              "to Doriath in search of him. Túrin slew Brodda. As Túrin left, Aerin burnt",
                              "herself alive in Brodda's halls. Túrin then sought Finduilas in Brethil.",
                              323, 630, 578, 152)

# Tenth Marker: Woods of Brethil
woodsbrethil = marker.Marker(markimg, 490, 300)
woodsbrethilrect = woodsbrethil.pos
mwoodsbrethil = messageBox.Button("In search of Finduilas, Túrin picked up the trail of her Orcs captives.",
                                  "He reached the forests of Brethil where the woodsmen informed Túrin of",
                                  "Finduilas' death. Túrin donned the name Turambar, Master of Doom, grieving. ",
                                  "the loss. After some time in Brethil, Túrin found a naked woman on Finduilas'",
                                  "grave. He called her Níniel, later taking her as his wife. However, this was",
                                  "actually his own sister, whose memory had been erased by Glaurung.",
                                  323, 630, 578, 152)

# Eleventh Marker: Glaurung
glaurung = marker.Marker(markimg, 470, 310)
glaurungrect = glaurung.pos
mglaurung = messageBox.Button("Túrin maintained a decent life until Glaurung appeared in Brethil, burning",
                              "miles of forest. Túrin tracked Glaurung to the ravine Cabed-en-Aras. He ",
                              "crept below the sleeping beast, took Gurthang and, from the underbelly,",
                              "pierced Glaurung's heart. Túrin passed out from the dragon's blood. Níniel",
                              "came searching for Túrin when Glaurung, in his last words, revealed that",
                              "Túrin is her brother. She threw herself into the ravine before Túrin awoke.",
                              323, 630, 578, 152)

# Twelfth Marker: Túrin's Death
death = marker.Marker(markimg, 472, 290)
deathrect = death.pos
mdeath = messageBox.Button("When Túrin awoke, Brandir the lame told of what had occured. In anger and",
                           "disbelief, Túrin killed him. Only later, when he learned the truth from",
                           "Mablung, was Túrin stricken with grief. Unable to live with his grief, Túrin",
                           "cast himself upon Gurthang. He was buried next to Finduilas' grave with the ",
                           "shards of Gurthang. On his grave, the Elves of Doriath carved: TÚRIN TURAMBAR ",
                           "DAGNIR GLAURUNGA. The elves sang a lament for the doomed Children of Húrin. ",
                           323, 630, 578, 152)

black=(0,0,0)
end_it=False
while (end_it==False):
    screen.fill(black)
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    anotherfont = pygame.font.SysFont("Britannic", 20)
    nlabel=myfont.render("Túrin Turambar: Interactive Summary", 1, (255, 0, 0))
    xlabel=anotherfont.render("~Follow Túrin's tragic path around Beleriand~", 1, (255, 0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            end_it=True
    screen.blit(nlabel,(360,350))
    screen.blit(xlabel,(465, 400))
    pygame.display.flip()



count = 0
while 1:
    if count == 48:
        count = 0
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            walkingSound.play(0, 3500)
            player.goal = Vector2(event.pos)
        # Hover Animation
        mdoriath.handle_event(event)
        mbrethil.handle_event(event)
        mamonrudh.handle_event(event)
        mtaurnufuin.handle_event(event)
        meithil.handle_event(event)
        mnargothrond.handle_event(event)
        meredwethrin.handle_event(event)
        mgatesofnargo.handle_event(event)
        mdorlomin.handle_event(event)
        mwoodsbrethil.handle_event(event)
        mglaurung.handle_event(event)
        mdeath.handle_event(event)

    if player.stopped:
        if count % 8 == 0 or count % 8 == 7:
            player.image = pygame.image.load("player_standing.png")
        elif count % 8 == 1 or count % 8 == 6:
            player.image = pygame.image.load("player_standing2.png")
        elif count % 8 == 2 or count % 8 == 5:
            player.image = pygame.image.load("player_standing3.png")
        elif count % 8 == 3 or count % 8 == 4:
            player.image = pygame.image.load("player_standing4.png")
        if time.time() - idle_frame_start > 0.6:
            count += 1
            #print(count)
            idle_frame_start = time.time()
    else:
        if count % 6 == 0:
            player.image = pygame.image.load("player_walk1.png")
        elif count % 6 == 1:
            player.image = pygame.image.load("player_walk2.png")
        elif count % 6 == 2:
            player.image = pygame.image.load("player_walk3.png")
        elif count % 6 == 3:
            player.image = pygame.image.load("player_walk4.png")
        elif count % 6 == 4:
            player.image = pygame.image.load("player_walk5.png")
        elif count % 6 == 5:
            player.image = pygame.image.load("player_walk6.png")
        if time.time() - walking_frame_start > 0.2:
            count += 1
            #print(count)
            walking_frame_start = time.time()

    pygame.display.update()
    screen.blit(map, maprect)

    screen.blit(doriath.image, doriathrect)
    screen.blit(brethil.image, brethilrect)
    screen.blit(amonrudh.image, amonrudhrect)
    screen.blit(taurnufuin.image, taurnufuinrect)
    screen.blit(eithil.image, eithilrect)
    screen.blit(nargothrond.image, nargothrondrect)
    screen.blit(eredwethrin.image, eredwethrinrect)
    screen.blit(gatesofnargo.image, gatesofnargorect)
    screen.blit(dorlomin.image, dorlominrect)
    screen.blit(woodsbrethil.image, woodsbrethilrect)
    screen.blit(glaurung.image, glaurungrect)
    screen.blit(death.image, deathrect)

    all_sprites.update()
    all_sprites.draw(screen)

    # Event Doriath
    if doriathrect.collidepoint(player.pos):
        mdoriath.update()
        mdoriath.draw(screen)

    # Event Brethil
    elif brethilrect.collidepoint(player.pos):
        mbrethil.update()
        mbrethil.draw(screen)

    # Event Amon Rudh
    elif amonrudhrect.collidepoint(player.pos):
        mamonrudh.update()
        mamonrudh.draw(screen)

    # Event Taur-nu-Fuin
    elif taurnufuinrect.collidepoint(player.pos):
        mtaurnufuin.update()
        mtaurnufuin.draw(screen)

    # Event Eithil Ivrin
    elif eithilrect.collidepoint(player.pos):
        meithil.update()
        meithil.draw(screen)

    # Event Nargothrond
    elif nargothrondrect.collidepoint(player.pos):
        mnargothrond.update()
        mnargothrond.draw(screen)

    # Event Ered Wethrin
    elif eredwethrinrect.collidepoint(player.pos):
        meredwethrin.update()
        meredwethrin.draw(screen)

    # Event Gates of Nargothrond
    elif gatesofnargorect.collidepoint(player.pos):
        mgatesofnargo.update()
        mgatesofnargo.draw(screen)

    # Event Dor-lomin
    elif dorlominrect.collidepoint(player.pos):
        mdorlomin.update()
        mdorlomin.draw(screen)

    # Event Woods of Brethil
    elif woodsbrethilrect.collidepoint(player.pos):
        mwoodsbrethil.update()
        mwoodsbrethil.draw(screen)

    # Event Death of Glaurung
    elif glaurungrect.collidepoint(player.pos):
        mglaurung.update()
        mglaurung.draw(screen)

    # Event Death of Túrin
    elif deathrect.collidepoint(player.pos):
        mdeath.update()
        mdeath.draw(screen)

    pygame.display.update()

    pygame.display.flip()
    clock.tick(30)
