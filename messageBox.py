import pygame
WHITE = (255, 255, 255)

class Button():

    def __init__(self, text1, text2, text3, text4, text5, text6, x=0, y=0, width=100, height=50, command=None):

        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4
        self.text5 = text5
        self.text6 = text6
        self.command = command

        self.image_normal = pygame.image.load("box_nor.png").convert_alpha()

        self.image_hovered = pygame.image.load("box_hov.png").convert_alpha()

        self.image = self.image_normal
        self.rect = self.image.get_rect()

        font = pygame.font.Font('freesansbold.ttf', 11)

        text_image1 = font.render(text1, True, WHITE)
        text_rect1 = text_image1.get_rect(topleft=(self.rect.center[0]-170,self.rect.center[1]-55))

        text_image2 = font.render(text2, True, WHITE)
        text_rect2 = text_image2.get_rect(topleft=(self.rect.center[0]-170,self.rect.center[1]-35))

        text_image3 = font.render(text3, True, WHITE)
        text_rect3 = text_image3.get_rect(topleft=(self.rect.center[0]-170,self.rect.center[1]-15))

        text_image4 = font.render(text4, True, WHITE)
        text_rect4 = text_image4.get_rect(topleft=(self.rect.center[0]-170,self.rect.center[1]+5))

        text_image5 = font.render(text5, True, WHITE)
        text_rect5 = text_image4.get_rect(topleft=(self.rect.center[0]-170, self.rect.center[1] + 25))

        text_image6 = font.render(text6, True, WHITE)
        text_rect6 = text_image6.get_rect(topleft=(self.rect.center[0]-170, self.rect.center[1] + 45))

        self.image_normal.blit(text_image1, text_rect1)
        self.image_normal.blit(text_image2, text_rect2)
        self.image_normal.blit(text_image3, text_rect3)
        self.image_normal.blit(text_image4, text_rect4)
        self.image_normal.blit(text_image5, text_rect5)
        self.image_normal.blit(text_image6, text_rect6)

        self.image_hovered.blit(text_image1, text_rect1)
        self.image_hovered.blit(text_image2, text_rect2)
        self.image_hovered.blit(text_image3, text_rect3)
        self.image_hovered.blit(text_image4, text_rect4)
        self.image_hovered.blit(text_image5, text_rect5)
        self.image_hovered.blit(text_image6, text_rect6)

        # you can't use it before `blit`
        self.rect.topleft = (x, y)

        self.hovered = False
        # self.clicked = False

    def update(self):

        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal

    def draw(self, surface):

        surface.blit(self.image, self.rect)

    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                #print('Clicked:', self.text1)
                if self.command:
                    self.command()