import os

def element_settings():
    global dict_item, root_directory, gif_directory, collectionsGifRoot, tempCOllectionPath, ffmpegPath

    #List1(Production) elements path which cannot be modified by User
    root_directory = 'D:/My Collections/ActionEssentials'    # add root path of the elements/stock footage

    #Production(list1) Collections cache path
    gif_directory ='D:/My Collections/caches'     # add root path of the element/stock 'gif' files

    #custom Collections cache path
    collectionsGifRoot = os.path.join(os.path.expanduser('~'), 'Documents', 'elementsBrowser', 'cache', 'My collections')

    #ffmpeg file path which is downlaoded from internet
    ffmpegPath = 'D:/ffmpeg.exe'  # download ffmpeg from ffmpeg.org

    # add name which u wanna display in list1  and  appropriate folder name of the actual elemnets
	#example: {'Atomsphere':'01.Atomosphere@mov',}     >>> "Atomsphere" is the name gonna display in list1 , "01.Atomsphere" is the actual folder name which contains atomsphere stock elements followed by '@' followed by file_extension 'mov'
    # folder must have files with same file type
    dict_item = {
	'Atmosphere': '01. Atmospheres@mov',
        'Blood': '02. Blood@mov',
        'Charges': '03. Charges@mov',
        'Couch_Hits': '04. Couch_Hits@mov',
        'Debris': '05. Debris@mov',
        'Dirt_Charges': '06. Dirt_Charges@mov',
        'Dust_Elements_A': '07. Dust_Elements_A@mov',
        'Dust_Elements_B': '07. Dust_Elements_B@mov',
        'Explosions': '08. Explosions@mov',
        'Fire': '09. Fire@mov',
        'Glass': '10. Glass@mov',
        'Muzzle_Flashes': '11. Muzzle_Flashes@mov',
        'Particle_Hits': '12. Particle_Hits@mov',
        'Powder_Hits': '13. Powder_Hits@mov',
        'Smoke': '14. Smoke@mov',
        'Smoke_Charges': '15. Smoke_Charges@mov',
        'Shells': '18. Shells@mov',
        'Water': '19. Water@mov',
        'Bullet Holes': '20. Textures/Bullet_Holes@png'
    }


    #no need to modify the path if you are  using windows.
    tempCOllectionPath = os.path.join(os.path.expanduser('~'), 'Documents', 'elementsBrowser/Data/')





