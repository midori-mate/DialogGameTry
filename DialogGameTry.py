# coding: utf-8

'''DialogGameTry

pygameお試し作品。
windowsのみ対応。
ダイアログアプリの習作。TRPGシナリオ『壁に耳あり』のリプレイ。
'''

import pygame, sys, time
from pygame.locals import *
import os
import accept_mouse_click


_DATA_FOLDER = '01_data'
_IMG_FOLDER = '02_img'
_MUSIC_FOLDER = '03_music'

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('MATE TRPG: 壁に耳あり')

# 画像ロード
def img(a):
    return pygame.image.load(_IMG_FOLDER + os.sep + a + '.png').convert_alpha()
black = img('600x150black')
bg_bed = img('bg_bed') # 640x480
bg_skype = img('bg_skype') # 640x480
bg_tatami = img('bg_tatami') # 640x480
m_reading = img('m_reading') # 250x180
mob_oriduru = img('mob_oriduru')
op_hajime = img('op_hajime') # 150x50
op_hajime2 = img('op_hajime2') # 150x200
op_tsuduki = img('op_tsuduki') # 150x50
op_tsuduki2 = img('op_tsuduki2') # 150x200
w_futon = img('w_futon') # 400x430
w_kimono = img('w_kimono') # 200x460
w_pajamas = img('w_pajamas') # 200x420
sheet = img('sheet') # 500x350
m_reading2 = img('m_reading2')
w_futon2 = img('w_futon2')
w_kimono2 = img('w_kimono2')
w_pajamas2 = img('w_pajamas2')

# ログ読み込みと分割
dialog = ''
for line in open(f'{_DATA_FOLDER}{os.sep}Lake District.txt', 'r', encoding='utf-8'):
    dialog += line
dialog_lis = dialog.split('\n\n')

# サウンドロード
se_switch2 = pygame.mixer.Sound(f'{_MUSIC_FOLDER}{os.sep}switch2.ogg')
se_don = pygame.mixer.Sound(f'{_MUSIC_FOLDER}{os.sep}don.ogg')
se_ban = pygame.mixer.Sound(f'{_MUSIC_FOLDER}{os.sep}ban.ogg')
se_switch2.set_volume(0.2)
se_don.set_volume(0.2)
se_ban.set_volume(0.2)

# macではmp3が読めない。
# pygame.mixer.music.load(f'music{os.sep}cave.mp3')
# pygame.mixer.music.set_volume(0.5) # ヴォリュームは0.0から1.0まで
# pygame.mixer.music.play(-1)

# アニメーションに使う
def split_img(img):
    img_lis = []
    y = [0, 50, 100, 150]
    for foo in y: # 0, y最大値, yイチマスぶん
        surface = pygame.Surface((150, 50))
        surface.blit(img, (0,0), (0,foo,150,50))
        surface.convert()
        img_lis.append(surface)
    return img_lis

# 画像を blit() するよ
def img_put(name, a):
    return screen.blit(name, a)

# オープニングの文字アニメーション
def animation(hot, frame):
    if hot == 0: a, b = 'hajime2', (480,340)
    elif hot == 1: a, b = 'tsuduki2', (480,400)
    images = split_img(eval('op_' + a))
    colorkey = images[frame // 6 % 4].get_at((0,0))
    images[frame // 6 % 4].set_colorkey(colorkey, RLEACCEL)
    return screen.blit(images[frame // 6 % 4], b)

def which_section(a): # section ごとの分岐内容
    font = pygame.font.Font(_DATA_FOLDER + os.sep + 'VL-Gothic-Regular.ttf', 20)
    text_lis = dialog_lis[dialog_number].split('\n')

    if a == 0: # opening
        img_put(bg_skype, (0,0))
        img_put(op_hajime, (480,340))
        img_put(op_tsuduki, (480,400))
        clock.tick(60)
        animation(hot, frame)
    elif a == 1: # 背景スカイプ、人いない
        img_put(bg_skype, (0,0))
        img_put(black, (20,320))
        for foo in range(len(text_lis)):
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))
    elif a == 2: # 背景すかいぷ、人いない、Cでシート
        img_put(bg_skype, (0,0))
        img_put(black, (20,320))
        for foo in range(len(text_lis)):
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))
    elif a == 3: # 背景べっど、KP、Cでシート
        img_put(bg_bed, (0,0))
        img_put(black, (20,320))
        img_put(m_reading2, (20,185))
        for foo in range(len(text_lis)):
            if text_lis[0] == '(KP)': img_put(m_reading, (20, 185))
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))
    elif a == 4: # 背景べっど、KP、ぱじゃまえる、Cでシート
        img_put(bg_bed, (0,0))
        img_put(w_pajamas2, (480,100))
        if text_lis[0] == '(エル)': img_put(w_pajamas, (480,100))
        img_put(black, (20,320))
        img_put(m_reading2, (20,185))
        if text_lis[0] == '(KP)': img_put(m_reading, (20, 185))
        for foo in range(len(text_lis)):
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))
    elif a == 5: # 背景畳、KP、着物える、Cでシート
        img_put(bg_tatami, (0,0))
        img_put(w_kimono2, (480,100))
        if text_lis[0] == '(エル)': img_put(w_kimono, (480,100))
        img_put(black, (20,320))
        img_put(m_reading2, (20,185))
        if text_lis[0] == '(KP)': img_put(m_reading, (20, 185))
        for foo in range(len(text_lis)):
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))
    elif a == 6: # 背景畳、KP、布団える、Cでシート
        img_put(bg_tatami, (0,0))
        img_put(w_futon2, (350,130))
        if text_lis[0] == '(エル)': img_put(w_futon, (350,130))
        img_put(black, (20,320))
        img_put(m_reading2, (20,185))
        if text_lis[0] == '(KP)': img_put(m_reading, (20, 185))
        for foo in range(len(text_lis)):
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))
    elif a == 7: # 背景べっど、KP、パジャマえる、Cでシート
        img_put(bg_bed, (0,0))
        img_put(w_pajamas2, (480,100))
        if text_lis[0] == '(エル)': img_put(w_pajamas, (480,100))
        img_put(black, (20,320))
        img_put(m_reading2, (20,185))
        if text_lis[0] == '(KP)': img_put(m_reading, (20, 185))
        for foo in range(len(text_lis)):
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))
    elif a == 8: # 背景スカイプ、人いない
        img_put(bg_skype, (0,0))
        img_put(black, (20,320))
        for foo in range(len(text_lis)):
            text = font.render(text_lis[foo], True, (200,200,200))
            screen.blit(text, (25, 325 + (font.get_linesize() * foo)))

def which_line(dialog_number): # ダイアログのナンバーを引数にとり、いまセクションいくつなのか返す
    if 1 <= dialog_number <= 15: return 1
    elif 16 <= dialog_number <= 23: return 2
    elif 24 <= dialog_number <= 26: return 3
    elif 27 <= dialog_number <= 37: return 4
    elif 38 <= dialog_number <= 156: return 5
    elif 157 <= dialog_number <= 254: return 6
    elif 255 <= dialog_number <= 256: return 7
    elif 257 <= dialog_number <= 262: return 8
    elif dialog_number == 0: return 0
    else: pass

def save():
    save_line = str(hot) + ' ' + str(frame) + ' ' + str(if_sheet) + ' a ' + str(dialog_number)
    w = open(f'{_DATA_FOLDER}{os.sep}Auckland Region.txt', 'w')
    w.write(save_line)
    w.close

def pressZ():
    font = pygame.font.Font(_DATA_FOLDER + os.sep + 'VL-Gothic-Regular.ttf', 15)
    text = font.render('press Z to turn the page', True, (200,0,0))
    screen.blit(text, (220, 455))

# --- functions ここまで --------------------------------------------------------------

hot = 0 # hajime or tsuduki 0:h 1:t
frame = 0
clock = pygame.time.Clock()
if_sheet = 1
dialog_number = 0
oriduru_count = 0
oriduru_lis = [(0,30), (100,130), (200,50), (300,100), (400,50)]
while True:
    which_section(which_line(dialog_number)) # dialog_number から現在の section を検索
    if dialog_number == 0: frame += 1 # section0のとき、アニメーションのため frame をいじる
    if dialog_number == 16 and if_sheet != 3: if_sheet = 2 # if_sheet isn't 3 がないとシートが消せない
    if not if_sheet % 2: screen.blit(sheet, (20,20)) # if_sheet が偶数(if_sheet % 2 であまりが出ない)ならシートを出す
    # ふたつの箇所で折り鶴アニメーションを出す if 文
    if dialog_number == 174 or dialog_number == 189:
        if oriduru_count == 0:
            se_don.play()
            img_put(mob_oriduru, (0,30))
            oriduru_count += 1
        elif oriduru_count == 1:
            time.sleep(0.8)
            se_don.play()
            img_put(mob_oriduru, (100,130))
            oriduru_count += 1
        elif oriduru_count == 2:
            time.sleep(0.8)
            se_don.play()
            img_put(mob_oriduru, (200,50))
            oriduru_count += 1
        elif oriduru_count == 3:
            time.sleep(0.8)
            se_don.play()
            img_put(mob_oriduru, (300,100))
            oriduru_count += 1
        elif oriduru_count == 4:
            time.sleep(0.8)
            se_don.play()
            img_put(mob_oriduru, (400,50))
            oriduru_count += 1
        elif oriduru_count == 5:
            time.sleep(0.8)
            se_ban.play()
            oriduru_count += 1
    if dialog_number == 188: oriduru_count = 0
    if dialog_number != 0:
        pressZ()
    for event in pygame.event.get():

        # macでも開くための措置。
        event = accept_mouse_click.switch(event)

        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_F4 and bool(event.mod & KMOD_ALT)):
            sys.exit()
        if not if_sheet % 2: # -------------------------- シートが出ているときCは反応する ----------------------
            if event.type == KEYDOWN:
                if event.key == K_c: if_sheet += 1
        else: # ------------------------------------- シートが出てないときはキー反応する --------------------
            if event.type == KEYDOWN:
                if dialog_number == 0: # section0のとき、上で「はじめから」、下で「つづきから」
                    if event.key == K_UP: hot = 0
                    if event.key == K_DOWN: hot = 1
                if dialog_number >= 16: # section2以降、Cでシートが出るように
                    if event.key == K_c: if_sheet += 1
                if event.key == K_z:
                    if dialog_number >= 1: # section1以降、Zでページ送り
                        dialog_number += 1
                        se_switch2.play()
                    if dialog_number == 0 and hot == 0: # section0かつ「はじめから」のとき、Zでsection1へ
                        dialog_number = 1
                        se_switch2.play()
                    if dialog_number == 0 and hot == 1: # section0かつ「つづきから」のとき、Zで
                        load_line = ''
                        for line in open(f'{_DATA_FOLDER}{os.sep}Auckland Region.txt', 'r'):
                            load_line = line
                        load_line_lis = load_line.split(' a ')
                        dialog_number = int(load_line_lis[1])
                    if dialog_number == 263:
                        dialog_number = 0
                        se_switch2.play()
                if event.key == K_F5:
                    save() # なぜか関数の内容をここに書いたら、セーブ先フォルダの更新がリアルタイムでなされなかったので関数で
                if event.key == K_F12:
                    dialog_number = 0


    pygame.display.update()
